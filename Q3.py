nums = [2, 7, 11, 15] 
target = 9
num_index = {}
result = []

for i, num in enumerate(nums):
    x = target - num
    if x in num_index:
        result = [num_index[x], i]
        break
    num_index[num] = i

print(result)