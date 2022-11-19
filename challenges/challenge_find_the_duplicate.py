from statistics import mode


def find_duplicate(nums):
    if not nums or not isinstance(nums, list):
        return False

    _nums = list(dict.fromkeys(nums))

    result = mode(nums)

    if not isinstance(result, int) or result < 0:
        return False

    if len(nums) != len(_nums):
        return mode(nums)
    else:
        return False
