nums = [1,2,2,3,3,3]
k = 2

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0)+1

bucket = [[] for _ in range(len(nums)+1)]

for num, f in freq.items():
    bucket[f].append(num)

res = []
for i in range(len(bucket)-1, -1, -1):
    for num in bucket[i]:
        res.append(num)
        if len(res)==k:
            print(res)
            break