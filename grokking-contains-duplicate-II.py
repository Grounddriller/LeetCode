def contains_nearby_duplicate(nums, k):
    window = set()

    for i in range(len(nums)):
        if nums[i] in window:
            return True

        window.add(nums[i])

        if len(window) > k:
            window.remove(nums[i - k])

    return False
