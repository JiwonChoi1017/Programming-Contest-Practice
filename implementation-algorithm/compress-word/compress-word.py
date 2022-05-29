# 文字列圧縮
def solution(s):
    compressed_word = s
    for i in range(1, len(s) // 2 + 1):
        str_list = []
        for j in range(0, len(s), i):
            str_list.append(s[j:j + i])

        idx = 0
        cnt = 1
        temp = ""
        for k in range(1, len(str_list)):
            if str_list[k] == str_list[idx]:
                cnt += 1
            else:
                temp += str(cnt) + str_list[idx] if cnt > 1 else str_list[idx]
                idx = k
                cnt = 1

            if k >= len(str_list) - 1:
                temp += str(cnt) + str_list[idx] if cnt > 1 else str_list[idx]

        if len(compressed_word) >= len(temp):
            compressed_word = temp

    return len(compressed_word)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
