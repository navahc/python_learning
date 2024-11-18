'''
32: Spiral Matrix
https://leetcode.com/problems/spiral-matrix/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100
'''

# matrix_rows=int(input('Input the number of rows in the matrix: '))
# matrix_columns=int(input('Input the number of columns in the matrix: '))

# if matrix_rows>=1 and matrix_columns<=10:
#     print(f'User has selected {matrix_rows} Rows and {matrix_columns} Columns')
# else:
#     pass

orig_matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

left, right=0,len(orig_matrix[0])
top, bottom=0,len(orig_matrix)

while left<right and top<bottom:
    result_matrix=[]
    for i in range(left,right):
        result_matrix.append(orig_matrix[top][i])
    top+=1
    for i in range(top,bottom):
        result_matrix.append(orig_matrix[i][right-1])
    right-=1
    for i in range(right,left,-1):
        result_matrix.append(i)
    bottom-=1
    for i in range(bottom,top,-1):
        result_matrix.append(i)
    print (result_matrix)