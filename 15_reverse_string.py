orig_str='rehan'

def strReverseIndexing(orig_str):
    '''
    Using indexing

    Time Complexity:    O(n)
    Space Complexity:   O(1)
    '''
    reverse_str=orig_str
    for i in range(len(orig_str)):
        # print(i)
        print(reverse_str[-i-1])
# strReverseIndexing(orig_str)

def strReverseTwoPointer(orig_str:list[str]) -> None:
    '''
    Using two pointer approach
    Time Complexity:    O(n)
    Space Complexity:   O(n)
    '''
    orig_str_l=0
    orig_str_r=len(orig_str)-1
    while orig_str_l<orig_str_r:
        orig_str[orig_str_r],orig_str[orig_str_l]=orig_str[orig_str_l],orig_str[orig_str_r]
        orig_str_l+=1
        orig_str_r-=1
    print(orig_str)
    result = "".join(orig_str)
    print(result)

# strReverseTwoPointer(list(orig_str))

def strReverseRecursive(orig_str: list[str], orig_str_l: int, orig_str_r: int) -> None:
    '''
    Recursive approach to reverse the list.
    Time Complexity:    O(n)
    Space Complexity:   O(n) (due to recursive call stack)
    '''
    # Base case: If the left pointer crosses the right pointer, stop recursion
    if orig_str_l >= orig_str_r:
        return
    
    # Swap the elements at the left and right pointers
    orig_str[orig_str_r], orig_str[orig_str_l] = orig_str[orig_str_l], orig_str[orig_str_r]
    
    # Recursive call with updated pointers
    strReverseRecursive(orig_str, orig_str_l + 1, orig_str_r - 1)

# Wrapper function to initialize the recursive process
def strReverseSlicing(orig_str: list[str]) -> None:
    strReverseRecursive(orig_str, 0, len(orig_str) - 1)
    print(orig_str)

orig_str = ["h", "e", "l", "l", "o"]
strReverseSlicing(orig_str)