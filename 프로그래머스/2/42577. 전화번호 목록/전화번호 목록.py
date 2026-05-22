def solution(phone_book):
    phone_dict = {i:1 for i in phone_book}

    for phone in phone_book:
        phone_list = list(phone)

        for i in range(len(phone_list)-1):
            if ''.join(phone_list[:i+1]) in phone_dict:
                return False

    return True