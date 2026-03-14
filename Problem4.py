#MISSING NUMBER IN AN ARRAY
n = int(input().strip())
arr = list(map(int,input().split()))

expected_sum = n*(n+1)//2
actual_sum = sum(arr)

print(expected_sum-actual_sum)