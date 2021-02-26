def read_minips_file(file_path: str) -> list[bytes]:

    with open(file_path, "rb") as f:
        data = f.read(4)
        bytes_list = []

        while data:
            bytes_list.append(data)
            data = f.read(4)

    return bytes_list


def parse_bytes_to_hex(data: bytes) -> str:

    # using from_bytes trick to read little endian:
    # https://docs.python.org/3/library/stdtypes.html#int.from_bytes

    little_endian_hex = hex(int.from_bytes(data, 'little'))

    # leading zeros trick https://stackoverflow.com/a/55089765

    removed_prefix = little_endian_hex.lstrip('0x')
    fixed_size = '0' * (8 - len(removed_prefix)) + removed_prefix

    return fixed_size


def hex_to_binary(hex_string: str) -> str:

    binary_string = bin(int(hex_string, base=16))

    removed_prefix = binary_string.lstrip('0b')
    fixed_size = '0' * (32 - len(removed_prefix)) + removed_prefix

    return fixed_size


def parse_binary_to_miips(bit_string: str) -> str:

    opcode = bit_string[:6]

    if opcode == "000000":
        operation = get_r_format_op(bit_string)
        data = get_r_format_data(bit_string)
    elif opcode == "000011":
        operation = "JAL"
        data = hex(int(bit_string[6:], base=2))
    elif opcode == "000010":
        operation = "J"
        data = hex(int(bit_string[6:], base=2))
    else:
        operation = get_i_format_op(bit_string)
        data = get_i_format_data(bit_string)

    return operation + ', ' + data


raw = read_minips_file("resources/01.soma.text")
processed = [parse_bytes_to_hex(x) for x in raw]
binary = [hex_to_binary(x) for x in processed]
print(binary)
