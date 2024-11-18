# https://leetcode.com/problems/range-sum-query-immutable/description/

'''
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
'''

# def PrefixSum(NumArray:list[int]):
#     print(NumArray)
#     arrlen=len(NumArray)
#     PrefixSumArray=[]
#     presum=0
#     for arr_value in NumArray:
#         presum+=arr_value
#         PrefixSumArray.append(presum)
    
#     print(PrefixSumArray)
#     return PrefixSumArray

# def SumRange(NumArray,l,r):
#     if l==0:
#         NumArray_=[0]
#         return PrefixSum(NumArray)[r]-PrefixSum(NumArray_.append(NumArray))[l-1]
#     else:
#         return PrefixSum(NumArray)[r]-PrefixSum(NumArray)[l-1]

# NumArray=[-2, 0, 3, -5, 2, -1]
# PrefixSum(NumArray)
# sum_02=SumRange(NumArray,0,2)
# print(sum_02)
# # sum_25=SumRange(NumArray,2,5)
# # sum_05=SumRange(NumArray,0,5)

def PrefixSum(NumArray: list[int]):
    # Display the input array
    print("Original Array:", NumArray)
    
    # Calculate prefix sum array
    arrlen = len(NumArray)
    PrefixSumArray = []
    presum = 0
    
    for arr_value in NumArray:
        presum += arr_value
        PrefixSumArray.append(presum)
    
    # Display the calculated prefix sum array
    print("Prefix Sum Array:", PrefixSumArray)
    
    return PrefixSumArray

def SumRange(NumArray: list[int], l: int, r: int):
    # Get the prefix sum array
    prefix_sum_arr = PrefixSum(NumArray)
    
    # For the case when l == 0, return the sum up to index r
    if l == 0:
        return prefix_sum_arr[r]
    else:
        # General case: sum from index l to r
        return prefix_sum_arr[r] - prefix_sum_arr[l - 1]

# Example usage
NumArray = [-2, 0, 3, -5, 2, -1]
PrefixSum(NumArray)
sum_02 = SumRange(NumArray, 0, 2)
print("Sum from index 0 to 2:", sum_02)
