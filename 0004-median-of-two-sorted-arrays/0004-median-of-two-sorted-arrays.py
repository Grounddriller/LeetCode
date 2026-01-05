class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        m, n = len(nums1), len(nums2)
        x, y = 0, 0
        def get_min():
            nonlocal x, y
            if x < m and y < n:
                if nums1[x] < nums2[y]:
                    ans = nums1[x]
                    x += 1
                else:
                    ans = nums2[y]
                    y += 1
            elif y == n:
                ans = nums1[x]
                x += 1
            else:
                ans = nums2[y]
                y += 1
            return ans
        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m + n) // 2):
                _ = get_min()
            return get_min()
        