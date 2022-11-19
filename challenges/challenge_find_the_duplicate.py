from statistics import mode


def find_duplicate(nums):
    if not nums or not isinstance(nums, list):
        return False

    _nums = []

    for n in nums:
        if n not in _nums:
            _nums.append(n)

    result = mode(nums)

    if not isinstance(result, int) or result < 0:
        return False

    if len(nums) != len(_nums):
        return mode(nums)
    else:
        return False
