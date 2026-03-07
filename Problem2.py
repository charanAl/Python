#Leader in an Array

def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    for i in range(n-2,-1,-1):
        if arr[i]>=max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
    return leaders[::-1] #Reverse to maintain order

n = int(input().strip())
arr = list(map(int,input().split()))
result = findLeaders(arr)
print(*result)