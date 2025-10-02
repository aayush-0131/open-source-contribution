t = int(input())
for _ in range(t):
    n = int(input())
    a_i = list(map(int, input().split()))
    neg_count = 0
    zero_count = 0
 
    for x in a_i:
        if x == -1:
            neg_count += 1
        elif x == 0:
            zero_count += 1
 
    if neg_count % 2 == 0:
        print(zero_count)
    else:
        if zero_count > 0:
            print(zero_count + 2)
        else:
            print(2)
