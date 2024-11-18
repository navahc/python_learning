# Given a number N. The task is to find the number of set bits in its binary representation using recursion.
# https://instabyte.io/p/interview-master-100
# 25: Number of 1 Bits https://leetcode.com/problems/number-of-1-bits/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Tests to check:
# 1 Since the numbers are taken as an input are int we should always keep that as a int.
# 2 We should always get an input which is greater than 0

'''
My solution where it is is not obeying the recursive function.
there could be errors in handling of the input scenarios
What if the inputs are hexadecimal values?
bin function to convert the Int to Binary is something that is not a good strategy because the output is a string
'''
# def countOne(a):
#     bin_a=bin(a)
#     print(type(bin_a))
#     count=0
#     bin_a_sliced=bin_a[2:]
#     print(len(bin_a_sliced))
#     i=0
#     count=0
#     while (i<len(bin_a_sliced)): #10101
#         print(bin_a[2+i:2+i+1])
#         if (bin_a[2+i:2+i+1])=='1':#
#             '''
#             Comparing it with string one. How can I compare it with value of 1
#             '''
#             count+=1
#         else:
#             pass
#         i=i+1
#     return count

# a=int(input('Input a number: '))
# if a>0:
#     print(countOne(a))
# else:
#     print('input the value of a greater than 0')

######################################
'''
My solution where it is is not obeying the recursive function. >> the output is obeying the recursive nature of the function
There could be errors in handling of the input scenarios. What if the inputs are hexadecimal values? >> That is being taken care as there is not further function which is converting the input value of the USER to string like INT to BIN (bin) function.
Good logic as the
'''
def countSetBits(n:int):
    # Base case: when n is 0, there are no set bits
    if n == 0:
        return 0
    else:
        # Recursively count the set bits
        shift_logic=n >> 1
        print(shift_logic)
        return (n & 1) + countSetBits(shift_logic)

# Input from the user
a = int(input('Input a number: '))
if a > 0:
    print(bin(a))
    print(countSetBits(a))
else:
    print('Please input a value greater than 0')
