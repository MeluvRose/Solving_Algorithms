def searchPage(arr):
    P = arr[0]
    A = arr[1]
    B = arr[2]

    arr_page = list(range(1, P + 1))
    searchA = binarySearch(arr_page, A)
    searchB = binarySearch(arr_page, B)
    if searchA < searchB:
        return 'A'
    elif searchA > searchB:
        return 'B'
    return 0
        

def binarySearch(arr, user, cnt=1):
    mid = int((arr[0] + arr[len(arr) - 1]) / 2)
    idx_mid = arr.index(mid)

    if mid > user:
        cnt = binarySearch(arr[:idx_mid + 1], user, cnt + 1)
    elif mid < user:
        cnt = binarySearch(arr[idx_mid:], user, cnt + 1)
    else:
        return cnt
    return cnt


cnt_test = int(input())
for c in range(cnt_test):
    arr_input = list(map(int, input().split()))
    print(searchPage(arr_input))