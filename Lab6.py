def add_three_to_digits(number):
    number_str = str(number)
    modified_number_str = ""
    for digit in number_str:
        modified_digit = str((int(digit) + 3) % 10)
        modified_number_str += modified_digit
    modified_number = int(modified_number_str)
    return modified_number

get_num = input("What is your number: ")
password = add_three_to_digits(get_num)
print(password)