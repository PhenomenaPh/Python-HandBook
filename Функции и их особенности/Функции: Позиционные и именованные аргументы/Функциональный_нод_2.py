def gcd(*nums: int) -> int:
    if isinstance(nums, int):
        return nums
    else:
        initial_num = nums[0]

        for i in nums[1:]:
            while initial_num != 0 and i != 0:
                if initial_num > i:
                    initial_num %= i
                else:
                    i %= initial_num
            initial_num += i
    return initial_num
