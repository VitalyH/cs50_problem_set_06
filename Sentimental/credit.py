from cs50 import get_float

# Asking user for card number which is > 0
while True:
    number = get_float("Number: ")
    if number >= 0:
        break

# Counting digits in number
checkNumber = number
count = 0
while (checkNumber > 0):
    checkNumber = checkNumber // 10
    count = count + 1

# Define variables
checksum = 0
amexCheck = 0
masterCheck = 0
visaCheck = 0

# Main calculations
# Runnung it eight times (max number lenght / 2)
for i in range(9):
    # Extracting every first and second digit from the end
    everyFirstNumber = number % 10
    everySecondNumber = (number // 10) % 10

    # Card number losing two last digits
    number //= 100

    # First step of checksum calculation
    checksumNow = everySecondNumber * 2
    if checksumNow > 9:
        checksumNow = ((checksumNow // 10) % 10) + (checksumNow % 10)

    # Checking company identifiers
    if (number >= 4 and number <= 999):
        amexCheck = (number // 10)              # American Express: 15, should start from 34 or 37
        masterCheck = number                    # Master Card: 16, should start from 51, 52, 53, 54 or 55
        if (count == 16):
            visaCheck = (number // 10) % 10     # Visa: 16...
        else:
            visaCheck = number % 10             # ..or 13, should start from 4
    # Second step of checksum calculation
    checksum = checksum + checksumNow + everyFirstNumber

# Validate and print results
valid = checksum % 10                                           # Should be zero
if (valid == 0 and amexCheck == 37):                            # Checks for American Express
    print("AMEX")
elif (valid == 0 and masterCheck >= 51 and masterCheck <= 55):  # Checks for Master
    print("MASTERCARD")
elif (valid == 0 and visaCheck == 4):                           # Checks for Visa
    print("VISA")
else:
    print("INVALID")
