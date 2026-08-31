def productExceptSelf(nums: list[int]) -> list[int]:
    output = []
    prefix = 1
    sufix = 1
    for n in range(len(nums)):
        output.append(prefix)
        prefix = prefix * nums[n]
    for s in range(len(nums) - 1, -1, -1):
        output[s] = output[s] * sufix
        sufix = sufix * nums[s]
    return output


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
