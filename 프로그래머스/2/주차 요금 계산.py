def change_time(time):
   hour = int(time[:2])
   minute = int(time[3:])

   return hour*60 + minute


def solution(fees, records):
   answer = []
   park = {}
   normal_time, normal_fee, after_time, after_fee = fees
   car = {}

   for record in records:
      time, car_num, state = record.split()

      # 입차 입력
      if state == 'IN':
         in_time = change_time(time)
         park[car_num] = in_time

         if not car.get(car_num):
            car[car_num] = 0

      # 출차 시간 계산
      else:
         out_time = change_time(time)
         total_time = out_time - park[car_num]
         park[car_num] = -1

         car[car_num] += total_time

   # 남아있는 차 모두 빼기
   for car_num, in_time in park.items():
      if in_time != -1:
         out_time = change_time('23:59')
         total_time = out_time - in_time

         car[car_num] += total_time

   for car_name, time in sorted(car.items()):
      if time <= normal_time:
         answer.append(normal_fee)
      else:
         if (time - normal_time) % after_time:
            answer.append(normal_fee + ((time-normal_time)//after_time + 1) * after_fee)
         else:
            answer.append(normal_fee + (((time-normal_time)//after_time) * after_fee))

   return answer


input_fees = [1, 461, 1, 10]
input_records = ["00:00 1234 IN"]
print(solution(input_fees, input_records))