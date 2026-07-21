def solution(phone_book):
    answer = True
    phone_dict = dict(zip(phone_book, [1 for _ in range(len(phone_book))]))

    for phone in phone_book:
        phone_list = list(phone)
        phone_num = ''

        for i in range(len(phone_list)-1):
            phone_num += phone_list[i]
            if phone_dict.get(phone_num):
                return False

    return answer