


n = int(input())

def encode(num):
    return (num <<  1) ^ num

nums = list(map(int, input().split()))
for i in nums:
    for j in range(256):
        if encode(j)&(pow(2, 8)-1) == i:
            print(j, end=" ")
            break
