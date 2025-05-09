def merge(nums1, m, nums2, n):
    # Initialize pointers
    i = m - 1  # Pointer for the last valid element in nums1
    j = n - 1  # Pointer for the last element in nums2
    k = m + n - 1  # Pointer for the last position in nums1

    # Merge the arrays from the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]  # m = 3 elements to merge
m = 3
nums2 = [2, 5, 6]           # n = 3 elements
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output will be [1, 2, 2, 3, 5, 6]