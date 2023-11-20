def hex_char_decode(digit):      #Decodes a single hexadecimal digit and returns its value.
    decimal_num = int(digit, 16)        
    return decimal_num

def hex_string_decode(hex_str):     #Decodes an entire hexadecimal string and returns its value.
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    try:
        decimal_num = 0
        for digit in hex_str:
            decimal_num = decimal_num * 16 + hex_char_decode(digit)
        return decimal_num
    except TypeError:
        print("Invalid input")
        return None

def binary_string_decode(binary_str):        #Decodes a binary string and returns its value.
    if binary_str.startswith('0b') or binary_str.startswith('0B'):
        binary_str = binary_str[2:]
    decimal_num = 0
    for digit in binary_str:
        decimal_num = decimal_num * 2 + int(digit)
    return decimal_num

def binary_to_hex(binary_str):      #REally confusing :(
    decimal_num = int(binary_str, 2)
    hex_num = ""
    while decimal_num > 0:
        hex_digit = decimal_num % 16
        hex_num = format(hex_digit, 'X') + hex_num
        decimal_num = decimal_num // 16
    return hex_num

def main():     #Printing menu repeatedly in loop, calling functions from above.
    while True:
        print("\nDecoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit\n")

        choice = input("Please enter an option: ")      #Ask user for what operation they'd like to choose

        if choice == '1':       #Decode Hexadecimal
            hex_str = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(hex_str)
            if result is not None:
                print(f"Result: {result}")
        elif choice == '2':     #Decode Binary
            binary_str = input("Please enter the numeric string to convert: ")
            result = binary_string_decode(binary_str)
            if result is not None:
                print(f"Result: {result}")
        elif choice == '3':     #Convert binary to hexadecimal
            binary_str = input("Enter a binary number: ")
            result = binary_to_hex(binary_str)
            print(f"Hexadecimal representation: {result}")
        elif choice == '4':
            print("Goodbye!")
            break       #End program
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")        #Ask user to input a number between 1-4


if __name__ == "__main__":
    main()
