import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
arrHap = [0 for _ in range(N+1)]
 
for i in range(1, N+1):
    arrHap[i] = numbers[i-1] + arrHap[i-1]
 
for _ in range(M):
    i, j = map(int, input().split())    
    print(arrHap[j] - arrHap[i-1])