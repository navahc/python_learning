# Given a number N. The task is to find the number of set bits in its binary representation using recursion.
# https://instabyte.io/p/interview-master-100
def countOne(a):
    bin_a=bin(a)
    print(type(bin_a))
    count=0
    bin_a_sliced=bin_a[2:]
    print(len(bin_a_sliced))
    i=0
    count=0
    while (i<len(bin_a_sliced)): #10101
        print(bin_a[2+i:2+i+1])
        if (bin_a[2+i:2+i+1])=='1':
            count+=1
        else:
            pass
        i=i+1
    return count

a=int(input('Input a number: '))
if a>0:
    print(countOne(a))
else:
    print('input the value of a greater than 0')