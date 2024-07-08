

def get_matrix(n, m, value):
    matrix = []

    for i in range(0,n):
        matrix.append([])

        for j in range(0, m):

            matrix[i].append(value)

    return matrix
result1 = get_matrix(3,2, 12)
print(result1)
