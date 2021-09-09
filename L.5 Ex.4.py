src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def next_num(nums):
    new_nums = []
    while len(nums) != 2:
        n = nums[0]
        m = nums[1]
        if n < m:
            new_nums.append(m)
        nums.pop(0)

    return new_nums


print(next_num(src))
