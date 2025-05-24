class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_sorted_nums = []
        index1, index2 = 0, 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                combined_sorted_nums.append(nums1[index1])
                index1 += 1
            else:
                combined_sorted_nums.append(nums2[index2])
                index2 += 1
        if index1 == len(nums1):
            combined_sorted_nums += nums2[index2:]
        else:
            combined_sorted_nums += nums1[index1:]
        len_combined = len(combined_sorted_nums)
        if len_combined % 2 == 0:
            return (combined_sorted_nums[len_combined // 2 - 1] + combined_sorted_nums[len_combined//2]) /2
        else:
            return combined_sorted_nums[len_combined // 2]