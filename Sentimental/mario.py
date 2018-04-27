from cs50 import get_int

# Asking user for height and checking it's range
while True:
    h = get_int("Height: ")
    if h < 24 and h >= 0:
        break

# Building the piramide
for i in range(h):

    # Printing spaces
    for j in range(h - i - 1):
        print(" ", end="")

    # Printing # - left row
    for j in range(i + 1):
        print("#", end="")

    # Printing two spaces between rows
    for j in range(2):
        print(" ", end="")

    # Printing # - right row
    for j in range(i + 1):
        print("#", end="")

    # New row
    print("")