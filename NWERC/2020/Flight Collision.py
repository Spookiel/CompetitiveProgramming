


import heapq as hp
from fractions import Fraction
n = int(input())

drones = [list(map(int, input().split()))+[i-1,i+1, 1] for i in range(n)]

### Drone info plus how far next left / right is
crashes = []
hp.heapify(crashes)

### Only consider the adjacent drones
### Keep priority queue of the crashes as crash events
### (time, drone_ind1, drone_ind2)


def check_col(ind1, ind2):
    posdif = drones[ind2][0]-drones[ind1][0]
    veldif = drones[ind1][1]-drones[ind2][1]

    ### Calculates the time when the first drone will catch up with the second drone

    if veldif == 0:
        return float("inf")
    res = Fraction(posdif, veldif)
    if res < 0:
        return float("inf") ### Moving away so can never collide
    return res


### Calculate all the initial crashes
for i in range(1, len(drones)):

    hp.heappush(crashes, (check_col(i-1, i), i-1, i))
#print(crashes)


while crashes:
    time, leftdrone, rightdrone  = hp.heappop(crashes)
    if not drones[leftdrone][-1] or not drones[rightdrone][-1]:
        ### One of the drones is already dead
        continue
    if time == float("inf"):
        ### All the others don't collide
        break
    drones[leftdrone][-1] = 0
    drones[rightdrone][-1] = 0
    nleftalive = drones[leftdrone][2]
    if nleftalive < 0:
        continue
    nrightalive = drones[rightdrone][3]
    if nrightalive >= n:
        continue
    drones[nrightalive][2] = drones[leftdrone][2]
    drones[nleftalive][3] = drones[rightdrone][3]
    ### Add a collision between these two
    hp.heappush(crashes, (check_col(nleftalive, nrightalive), nleftalive, nrightalive))

#print(drones)
ans = []
for j in range(1, len(drones)+1):
    if drones[j-1][-1]:
        #print("DEBUG:", drones[j-1])
        ans.append(j)
print(len(ans))
print(*ans)



