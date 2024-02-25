# 0(w * h) time | O(w * h) space
def transposeMatrix(matrix):
    transposedMatrix = []

    for col in range(len(matrix[0])): # Since we need the number of columns.
        newRow = []
        for row in range(len(matrix)): # Rows
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)
    return transposedMatrix
