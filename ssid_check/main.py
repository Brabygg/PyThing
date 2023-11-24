import os
import datetime as dt

def main():
    print("Swedish Social Security Number Validator")
    print("Developed by Nils K // Brabygg")
    print("---\n")
    
    while True:
        request_value()
        cls()

def request_value():
    val_array = []

    try:
        value = list(input("Input an SSN (YYMMDD-XXXX): ").strip())

        if len(value) != 11:
            raise Exception

        for char in value:
            if char == "-" or char == "+":
                val_array.append(char)
                continue

            val_array.append(int(char))

    except:
        cls()
        input("The entered value was invalid.\n(check its length, and for spaces or accidental letters!)\n")
        return

    validate(val_array)
    
def validate(digit_array):
    org_array = digit_array
    dash = digit_array[6]
    checksum = digit_array[10]

    # Discard the dash and the checksum digit
    digit_array.pop(6)
    digit_array.pop(9)

    # Multiply all odd digits by 2
    i = 0
    while i < 9:
        digit_array[i] *= 2
        i += 2

    # Split the results into individual digits
    for i in range(9):
        digit_array[i] = str(digit_array[i])

    digit_array = ''.join(digit_array)
    digit_array = list(digit_array)

    i = 0
    for digit in digit_array:
        digit_array[i] = int(digit_array[i])
        i += 1

    # Add the results
    digit_sum = 0
    for digit in digit_array:
        digit_sum += digit
        
    # f(x) = (10 - [x % 10]) % 10
    final_sum = (10 - (digit_sum % 10)) % 10

    # Compare to checksum digit
    if final_sum == checksum:
        input("Social security number is VALID")
        doxx(org_array, dash)
    else:
        input("Social security number is INVALID")

def doxx(ssn, dash):
    cur_date = dt.datetime.today().date()
    cur_year = cur_date.year
    cur_month = cur_date.month
    cur_day = cur_date.day

    year = str(ssn[0]) + str(ssn[1])

    input()

def cls():
    os.system(f"{'cls' if os.name == 'nt' else 'clear'}")

main()