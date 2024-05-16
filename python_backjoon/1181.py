import sys
n = int(sys.stdin.readline())

word_list = [sys.stdin.readline().strip() for _ in range(n)]
word_list = list(set(word_list))

word_list = sorted(sorted(word_list), key=lambda x : len(x))

for word in word_list:
    print(word)