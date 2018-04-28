from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    # i and j declaration
    i = len(a)
    j = len(b)

    # Matrix declaration
    matrix = [[0 for x in range(j + 1)] for y in range(i + 1)]
    matrix[0][0] = (0, None)

    # Rows
    count_j = 0
    for x in range(1, j + 1):
        matrix[0][x] = count_j, None
        count_j += 1

    # Insertion
    count_j = 0
    for x in range(0, j + 1):
        matrix[0][x] = count_j, Operation.INSERTED
        count_j += 1

    # Columns
    count_i = 0
    for y in range(1, i + 1):
        matrix[y][0] = count_i, None
        count_i += 1

    # Deletion
    count_i = 0
    for y in range(0, i + 1):
        matrix[y][0] = count_i, Operation.DELETED
        count_i += 1

    # Calculate the cost and the operations
    # Vertical
    y = 1
    while y < i + 1:

        # Horizontal
        x = 1
        while x < j + 1:

            # Substitutions
            s = 0
            if a[y - 2] == b[x - 2]:
                s = 0
            else:
                s = 1

            # Determine operations value
            delete = matrix[y - 1][x][0] + 1
            insert = matrix[y][x - 1][0] + 1
            substitute = matrix[y - 1][x - 1][0] + s

            # Find the minumal cost
            minimal = min(delete, insert, substitute)

            # Push operation into the matrix
            if delete == minimal:
                matrix[y][x] = delete, Operation.DELETED
            if insert == minimal:
                matrix[y][x] = insert, Operation.INSERTED
            if substitute == minimal:
                matrix[y][x] = substitute, Operation.SUBSTITUTED

            x += 1

        y += 1

    return(matrix)
