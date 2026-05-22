def solution(phone_book):
    phone_dict = {i:1 for i in phone_book}

    for phone in phone_book:
        phone_list = list(phone)

        for i in range(len(phone_list)):
            if ''.join(phone_list[:i+1]) in phone_dict:
                return False

    return True


phone_book_input = ["119", "97674223", "1195524421"]

print(solution(phone_book_input))