def construct_2D_array(original, m, n):
    if len(original) != m * n:
        return []

    result = []
    index = 0

    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(original[index])
            index += 1
        result.append(row)

    return result
