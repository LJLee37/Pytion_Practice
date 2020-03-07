nums = list(map(int,input().split()))
average = 0
for i in nums:
    average += i
print(average/len(nums))