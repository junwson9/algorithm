N, M = map(int, input().split())
trees = list(map(int, input().split()))
s = 1
e = max(trees)
while s <= e:
    m = (s+e)//2
    sm = 0
    for tree in trees:
        if tree > m:
            sm += (tree-m)
    if sm < M:
        e = m-1
    else:
        s = m+1
print(e)