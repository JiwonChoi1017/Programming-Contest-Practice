# 文字列圧縮
def solution(s):
    # 文字数を格納
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if prev == s[j:j + i]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j + i]
                cnt = 1
        compressed += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compressed))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
