n, m = map(int, input().split())
arr = []
 
for _ in range(n):
    arr.append(input())
    
row = [0] * n
col = [0] * m
 
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            col[j] = 1
            
r_cnt = 0
for i in range(n):
    if row[i] == 0:
        r_cnt += 1
        
c_cnt = 0
for i in range(m):
    if col[i] == 0:
        c_cnt += 1
        
print(max(r_cnt, c_cnt))