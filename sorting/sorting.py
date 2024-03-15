import sys, heapq
key, k = map(int, input().split())
n = int(input())
arr = [int(input()) for _ in range(n)]
def f(l, r):
    global k, arr
    if k <= 0 or l >= r: return
    pivot = arr[l]
    right = []
    cnt = r + 1
    for i in range(l, r + 1):
        if arr[i] > pivot:
            for j in range(r, i, -1):
                if arr[j] < pivot:
                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp
                    break
    for i in range(l + 1, r + 1):
        if arr[i] > pivot:
            cnt = i
            break
    tmp = arr[cnt - 1]
    arr[cnt - 1] = arr[l]
    arr[l] = tmp
    k -= 1
    f(l, cnt - 2)
    f(cnt, r)
    return
if key == 1:
    ans = 0
    for i in range(1, k + 1):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        ans += i - max(j, 0)
        arr[j + 1] = v
    print(ans)

elif key == 2:
    for i in range(k):
        mn, ps = arr[i], i
        for j in range(i + 1, n):
            if arr[j] < mn:
                mn, ps = arr[j], j
        tmp = arr[i]
        arr[i] = arr[ps]
        arr[ps] = tmp
    print(*arr, sep = "\n")
elif key == 3:
    heapq.heapify(arr)
    while k > 0:
        heapq.heappop(arr)
        k -= 1
    for i in arr: print(i)
else:
    f(0, n - 1)
    print(*arr, sep = "\n")
