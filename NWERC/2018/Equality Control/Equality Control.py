

from collections import deque

s1 = input()
s2 = input()



def find_end(string, ind):

    depth = 1
    for i in range(ind, len(string)):

        if depth == 0:
            return i
        if string[i] == "(":
            depth += 1
        elif string[i] == ")":
            depth -= 1
    return len(string)
    #raise Exception()


def eat_list(string, start):
    nums = []
    cint = ""
    for ind in range(start, len(string)):
        if string[ind].isdigit():
            cint += string[ind]
        elif string[ind] == "]":
            if cint:
                nums.append(int(cint))
            return nums, ind
        else:
            if cint:
                nums.append(int(cint))
            cint = ""
    if cint:
        nums.append(int(cint))
    return nums, len(string)
def extract_ints(string, start, end):
    cint = ""
    nums = []

    for ind in range(start, end):
        if string[ind].isdigit():
            cint += string[ind]
        else:
            if cint:
                nums.append(int(cint))
            cint = ""
    if cint:
        nums.append(int(cint))
    return nums



def solve(string):
    res = [(0, 0)] ### 0 for shuffled, 1 for sorted

    i = 0
    while i < len(string):
        ###print(i, string[:i])
        ##print(res)
        if string[i] == "[":
            nums, j = eat_list(string, i)

            if res[-1][1] == 1:
                res[-1][0].extend(nums)
            else:
                res.append((nums, 1))
            i = j
            #print(res, "RAW LIST")
        elif string[i] == "s":
            r = i+len("sorteda")+int(string[i+1] == "h")
            ####print("SKIP", r, string[r])
            j = find_end(string, r)
            ####print(j, "END OF", )
            nums = sorted(extract_ints(string, r, j))
            ###print(nums, "READING")
            sec = int(string[i+1] == "o")
            if nums[0] == nums[-1]:
                ###
                sec = 1
            ##print(res, "INSIDE SHUFFLE")
            ##print(nums, sec)
            if sec == 1 and sec == res[-1][1]:
                res[-1][0].extend(nums)
            else:
                res.append((nums, sec))

            i = j
        else:
            i += 1


    return res


a = solve(s1)
##print()
b = solve(s2)

#print(a)
#print(b)
##print(a[:2])
##print(b[:2])
if a == b:
    print("equal")
else:
    print("not equal")