'''
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
'''

def mergeSortedArray(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    '''
    My raw Solution
    implementation logic is having list functions like pop and insert
    Since the requirement has explcitly provided that the nums1 array will have m+n elements it was easier to have a for statement with the range starting with m and ending at m+n
    Using indexing

    Time Complexity:    O(n)
    Space Complexity:   O(1)
    '''
    nums2_index=0
    for i in range(m,m+n,1):
        nums1.pop(i)
        nums1.insert(i,nums2[nums2_index])
        nums2_index+=1
    nums1.sort()
    print(nums1)

nums1 = [1]
m = 1
nums2 = [0]
n = 0
mergeSortedArray(nums1,m,nums2,n)