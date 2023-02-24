lst = []
for _ in range(10):
    N = int(input())
    mod = N % 42
    if mod not in lst:
        lst.append(mod)
print(len(lst))