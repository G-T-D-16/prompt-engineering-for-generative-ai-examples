def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets

input = [1, 2, 3, 4, 5, 6]

output = create_staircase(input)
print(output)