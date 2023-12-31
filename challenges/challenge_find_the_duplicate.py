def find_duplicate(nums):
    if not nums or not isinstance(nums, list):
        return False

    double_nums = set()

    for num in nums:
        if not isinstance(num, int) or num <= 0:
            return False
        if num in double_nums:
            return num
        double_nums.add(num)

    return False
