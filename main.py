A_ = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
B_ = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matmul(A_,B_) == [[70, 80, 90], [158, 184, 210], [246, 288, 330]]

def matmul(A,B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])

    row = rowA if rowA > rowB else rowB
    col = colA if colA > colB else colB
    C = [[0]*col for i in range(row)]
    for rows in range(0, row):
      for cols in range(0, col):
        res = 0
        for i in range(0, colA):
          res += A[rows][i] * B[i][cols]
        C[rows][cols] = res

    print(A)

    return C