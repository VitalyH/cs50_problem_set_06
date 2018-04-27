from cs50 import get_string
import sys

# Check how many comand line arguments provided
# if 0 or more than 1 - exit
if len(sys.argv) != 2:
    print("Error!")

# Gain access to cipher key provided by user
key = int(sys.argv[1])

# Ask user for a text
plaintext = get_string("plaintext: ")

# Start printing output
print("ciphertext: ", end="")

# Execute cipher
for c in plaintext:
  #  print(c, end="")

 # Check if char is letter
    if c.isalpha():
        # Check if letter is uppercase or lowercase
        # Then convert
        if c.islower():
            c = (((ord(c) + key) - ord("a")) % 26) + ord("a")
            print(chr(c), end="")
        elif c.isupper():
            c = (((ord(c) + key) - ord("A")) % 26) + ord("A")
            print(chr(c), end="")

    # If not print right away
    else:
        print(c, end="")
# EOF
print()