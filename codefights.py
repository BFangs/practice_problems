def matrixElementsSum(matrix):
    """ghost hotel matrix sum problem"""
    count = sum(matrix[0])
    if len(matrix) > 1:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i-1][j]==0:
                    matrix[i][j]=0
                    count += 0
                else:
                    count += matrix[i][j]
    return count
