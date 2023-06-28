

n = int(input())
s = input()
from math import pow

zs = s.count("0")
os = len(s)-zs


for i in range(int(pow(2, os)), int(pow(2, os+zs))-int(pow(2,zs))+2):
    print(i, end=" ")

