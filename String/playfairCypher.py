key = "MONARCHY"
matrix = []
clean_key = ""


def createMatrix(matrix, key, clean_key):
    # Step 1: clean key, remove duplicates, replace J with I
    for c in key:
        if c == 'J':
            c = 'I'
        if c not in clean_key:
            clean_key += c

    # Step 2: fill remaining alphabet (J removed)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for c in alphabet:
        if c not in clean_key:
            clean_key += c

    # Step 3: build 5x5 matrix
    k = 0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(clean_key[k])
            k += 1
        matrix.append(row)


createMatrix(matrix, key, clean_key)


# --- Pair Creation ---
pairs = []
message = input("Enter message: ").upper().replace(" ", "")


def createPairs(message, pairs):
    i = 0
    while i < len(message):
        substring = []
        if i == len(message) - 1:
            substring.append(message[i])
            substring.append('X')
            pairs.append(substring)
            break

        elif message[i] == message[i + 1]:
            substring.append(message[i])
            substring.append('X')
            pairs.append(substring)
            i += 1

        else:
            substring.append(message[i])
            substring.append(message[i + 1])
            pairs.append(substring)
            i += 2


createPairs(message, pairs)
print(pairs)


# --- Position Finder ---
def findPosition(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


# --- Encryption ---
def encryption(matrix, pairs):
    encrypted = ""
    for pair in pairs:
        a, b = pair

        if a == 'J': a = 'I'
        if b == 'J': b = 'I'

        r1, c1 = findPosition(matrix, a)
        r2, c2 = findPosition(matrix, b)

        if r1 == r2:  # same row
            encrypted += matrix[r1][(c1 + 1) % 5]
            encrypted += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:  # same column
            encrypted += matrix[(r1 + 1) % 5][c1]
            encrypted += matrix[(r2 + 1) % 5][c2]

        else:  # rectangle rule
            encrypted += matrix[r1][c2]
            encrypted += matrix[r2][c1]

    return encrypted


print(encryption(matrix, pairs))
