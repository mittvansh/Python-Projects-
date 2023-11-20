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
    for x in range(0, len(rle_data),2):
        num += rle_data[x]
    return num

def decode_rle(rle_data):
    list_4 = []
    for x in range(0, len(rle_data),2):
        multiplier = rle_data[x]
        number = rle_data[x+1]
        for y in range(multiplier):
            list_4.append(number)
    return list_4

def string_to_data(data_string):
    list_new = []
    for i in data_string:
        list_new.append(int(i, 16))
    return list_new
