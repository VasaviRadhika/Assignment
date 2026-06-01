def matrix(m1,m2):
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
      return "matrices must have same dimensions"
    result=[]
    for i in range(len(m1)):
        row=[]
        for j in range(len(m1[0])):
            row.append(m1[i][j]+m2[i][j])
        result.append(row)
    return result
m1=[
    [1,2,3],
     [4, 5, 6],
     [7, 8, 9]
]
m2=[
     [9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]
]

result_matrix = matrix(m1, m2)

if isinstance(matrix, str):
 print(matrix)
else:
     print("Sum of matrices:")

     for row in result_matrix:

       print(row)

    
