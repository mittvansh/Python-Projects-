from console_gfx import ConsoleGfx      #Import Library
def to_hex_string(data):
    str_hex = ""
    for i in data:
        str_hex += hex(i)[2:]
    return str_hex


def count_runs(flat_data):
    if not flat_data:
        return 0

    num_changes = 1
    consecutive_count = 0
    prev_number = flat_data[0]

    for number in flat_data:
        if number != prev_number:
            num_changes += 1
            prev_number = number
            consecutive_count = 0
        else:
            consecutive_count += 1
            if consecutive_count == 15:
                num_changes += 1
                consecutive_count = 0

    return num_changes


def encode_rle(flat_data):
    count = 1
    prev_num = flat_data[0]
    result = []

    for num in flat_data[1:]:
        if num == prev_num and count < 15:
            count += 1
        else:
            while count > 15:
                result.extend([15, prev_num])
                count -= 15
            result.extend([count, prev_num])
            prev_num = num
            count = 1

    while count > 15:
        result.extend([15, prev_num])
        count -= 15
    result.extend([count, prev_num])

    return result


def get_decoded_length(rle_data):
    num = 0
    for x in range(0, len(rle_data), 2):
        num += rle_data[x]
    return num


def decode_rle(rle_data):
    list_4 = []
    for x in range(0, len(rle_data), 2):
        multiplier = rle_data[x]
        number = rle_data[x + 1]
        for y in range(multiplier):
            list_4.append(number)
    return list_4


def string_to_data(data_string):
    list_new = []
    for i in data_string:
        list_new.append(int(i, 16))
    return list_new


def to_rle_string(rle_data):
    data = []
    x = 0
    while x < len(rle_data):
        run_time = rle_data[x]
        value = rle_data[x+1]
        data.append(f"{run_time}{value:x}")
        x += 2
    return ":".join(data)

def string_to_rle(rle_string):
    rle_data = []
    pairs = rle_string.split(':')

    for pair in pairs:
        run_length_str = pair[:-1]
        run_value_hex = pair[-1]

        run_length = int(run_length_str)
        run_value = int(run_value_hex, 16)

        rle_data.extend([run_length, run_value])

    return rle_data
def menu_display():     #function that prints the basic menu that repeatedly prints. 
    print("")
    print("RLE Menu")
    print("--------")
    print("0. Exit ")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print("")

def main():         #Main Function that does all the conversions and the main program. 
    image_data, rle_string, hex_string, flat_data = None, None, None, None      #setting them to none to change them further in the program. 
    print("Welcome to the RLE image encoder!")  
    print("")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)       #Prints rainbow graphic. 
    print("")
    while True:
        menu_display()      #Calls back the menu display that repeatedly prints which is why its in loop. 
        user_input = int(input("Select a Menu Option: "))       #get user input with which menu option to use. 
        if user_input == 0:     #End Program. 
            break

        elif user_input == 1:       #Load a file. 
            file_name = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(file_name)

        elif user_input == 2:           #Load the test image. 
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")

        elif user_input == 3:           #RLE string decoder. 
            rle_string = input("Enter an RLE string to be decoded: ")

        elif user_input ==4:        #Hex String in RLE Data. 
            hex_string = input("Enter the hex string holding RLE data: ")

        elif user_input == 5:       #Hex String in Flat data.. 
            hex_string = input("Enter the hex string holding flat data: ")
            flat_data = hex_string

        elif user_input == 6:      #Display the image data loaded in either 1 or 2. 
            print("Displaying image...")
            if len(image_data) == 0:
                print("(no data)")
            else:
                ConsoleGfx.display_image(image_data)

        elif user_input == 7:       #Convert Hex_string to RLE
            if hex_string:
                print(f"RLE representation: {to_rle_string(string_to_data(hex_string))}\n")
            else:
                print("RLE representation: (no data)")

        elif user_input == 8:       #Convert RLE string to RLE hex. 
            if rle_string:
                print(f"RLE hex values: {to_hex_string(string_to_rle(rle_string))}\n")
            else:
                print("RLE hex values: (no data)")

        elif user_input == 9:           #display flat hex data in easy to read format. 
            if rle_string:
                flat_data = decode_rle(string_to_rle(rle_string))
                hex_flat_data = to_hex_string(flat_data)
                print(f"Flat hex values: {hex_flat_data}\n")
            elif hex_string and flat_data:
                print(f"Flat hex values: {flat_data}\n")
            elif hex_string:
                flat_data = decode_rle(string_to_data(hex_string))
                print(f"Flat hex values: {to_hex_string(flat_data)}\n")
            else:
                print("Flat hex values: (no data)")

            rle_string, hex_string, flat_data = None, None, None

if __name__ == '__main__':
    main()
