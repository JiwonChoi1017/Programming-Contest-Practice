# 文字列圧縮
def compress(text, tok_len):
    words = [text[i:i + tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    # zip(): forループの中で複数のリテラブルオブジェクト（リストやタプルなど）の要素を同時に取得して使いたい場合は、zip()関数の引数にそれらを指定する。
    # 3つ以上でも同様
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution(text):
    # List Comprehension（リストの内包表記）を使うとメモリ不足にならないらしい。
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text) / 2) + 1)) + [len(text)])


test_str = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in test_str:
    print(solution(x))
