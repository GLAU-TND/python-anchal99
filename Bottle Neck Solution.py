def min_visible_bottles(arr, n):
    m = dict()
    ans = 0
    for i in range(n):
        m[arr[i]] = m.get(arr[i], 0) + 1
        ans = max(ans, m[arr[i]])
        print(ans)


n = 8
arr = [1, 1, 2, 3, 4, 5, 5, 4]