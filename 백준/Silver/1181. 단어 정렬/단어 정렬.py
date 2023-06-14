N = int(input())
lst = set(input() for _ in range(N))
lst = list(lst)
lst.sort()
lst.sort(key=len)
for word in lst:
    print(word)