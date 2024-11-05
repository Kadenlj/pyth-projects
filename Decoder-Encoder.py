def variable_encoder(input_string, start_key, key_increment):
    key = start_key
    output_string = ''
    for char in input_string:
        encoded_char = chr(ord(char) + key)
        output_string += encoded_char
        key += key_increment
    return output_string

def encoder(input_string, key = 200):

    output_string = ''
    for char in input_string:
        encoded_char = chr(ord(char) + key)
        output_string += encoded_char
    return output_string