lst = []
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        lst.append(num)
if len(lst) >= 1:
    print(sum(lst))
    print(min(lst))
else:
    print('-1')