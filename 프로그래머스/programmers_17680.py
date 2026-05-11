# [1차] 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680


"""
문제 해석

데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다.
DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 모른다.
캐시 크기에 따른 실행 시간을 측정하는 프로그램을 작성하여라.
"""

"""
문제 접근

캐시에 데이터가 없을 때의 실행 시간은 5이다.
캐시에 데이터가 있다면 실행 시간은 1이다.
캐시 교체 알고리즘은 LRU이기 때문에 가장 오랫동안 바뀌지 않은 캐쉬 데이터가 교체된다.

캐시에 도시이름 데이터가 없고, 캐시가 가득 차 있다면 가장 오래된 데이터를 지운 후, 캐시에 저장한다.
캐시에 도시이름 데이터가 없고, 캐시가 가득 차 있지 않다면 캐시에 저장한다.
캐시에 도시이름 데이터가 있다면 해당 데이터를 가장 최근 데이터 자리에 놓는다.
"""


def solution(cacheSize, cities):
    cache = []
    answer = 0

    # 캐시크기가 0이라면 총 실행시간 = 도시의 개수 * 5
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        # 캐시에 도시이름 데이터가 없다면
        if city not in cache:
            # 실행시간 5 진행
            answer += 5

            # 캐시의 크기가 다 찼다면 가장 오래된 것 제거
            if len(cache) == cacheSize:
                cache.pop(0)
            # 캐시 저장소에 데이터 저장
            cache.append(city)

        # 캐시에 도시이름 데이터가 있다면
        else:
            # 실행시간 1 진행
            answer += 1
            cache.append(cache.pop(cache.index(city)))

    return answer


cacheSize_ex = 3
cities_ex = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize_ex, cities_ex))
