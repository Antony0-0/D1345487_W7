nums = [10, 20, 30, 40, 50, 60, 70, 80]
ranges = [(1, 4), (3, 6), (5, 8)]
result = set()
for start, end in ranges:
    for i in range(start, end):
        result.add(nums[i])
result_list = sorted(result)
print(result_list)