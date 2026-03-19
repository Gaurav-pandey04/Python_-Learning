def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return (a*b)//gcd(a, b)

# nums = [3, 5, 10, 20]
nums = [7, 11, 13]
result = nums[0]
for num in nums[1:]:
    result = lcm(result, num)

print(result)