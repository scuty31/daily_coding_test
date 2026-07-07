def solution(files):
    answer = []
    files_list = []
    idx = 0

    for file in files:
        file_list = [[], [], [], []]
        classification_idx = 0
        number_cnt = 0

        for s in file:
            if s.isnumeric():
                if classification_idx == 0:
                    classification_idx = 1
                elif classification_idx == 2:
                    classification_idx = 2

                if number_cnt >= 5:
                    classification_idx = 2

                file_list[classification_idx].append(s)
                number_cnt += 1
            else:
                if classification_idx == 1:
                    classification_idx = 2

                file_list[classification_idx].append(s)

        file_list[0] = ''.join(file_list[0]).upper()
        file_list[1] = int(''.join(file_list[1]))
        file_list[2] = ''.join(file_list[2])
        file_list[3] = idx
        idx += 1

        files_list.append(file_list)

    files_list.sort(key=lambda x: (x[0], x[1]))


    for i in range(len(files_list)):
        answer.append(files[files_list[i][3]])

    return answer


files_input = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files_input))