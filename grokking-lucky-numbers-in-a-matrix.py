def lucky_numbers(matrix):
    result = []

    row_mins = [min(row) for row in matrix]
    col_maxs = [max(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == row_mins[r] and matrix[r][c] == col_maxs[c]:
                result.append(matrix[r][c])

    return result
