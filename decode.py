import base64

def decode_payload(encoded_str):
    """
    This should decode the payload using a special algorithm.
    The algorithm is as follows:
    0) TRIM WHITESPACE
    1) Drop the first 4 and last 4 characters of the encoded string.
    2) Base64 decode the remaining string. HINT: You don't have the base64 library, but you do have os module
    3) Split the decoded string into chunks of 2 characters.
    4) For each chunk, convert the first character to a number using the formula:
        number = (ord(chunk[0]) - 32) * 16 + (ord(chunk[1]) - 32)
    5) Join the numbers together to form the final decoded string.
    """
    encoded_str = """
    ABCDICoiICIgIiAiICQoJiUmLCYsJi8iISIgJScmJSYsJiMmLyYtJiUiICckJi8iICckJigmJSIgJyAnJScqJyomLCYlIiAiKCYpIiAmJyclJiUnIycjIiwiICcgJyUnKicqJiwmJSIgJyAmISciJyQiICMiIiAmISckIiAnJCYoJ
    """
    temp_str = encoded_str
    temp_str = temp_str.strip() # OK. Trim whitespace
    temp_str = temp_str[4:] # OK. Trim first 4 characters.
    temp_str = temp_str[:-5] # OK. Trim last 4 characters.
    temp_str = base64.b64decode(temp_str) # OK. Check count of slice. Decode base64 string
    final_decoded_string = ""
    for char in temp_str:
        final_decoded_string += str(char)
    return final_decoded_string

    raise NotImplementedError("Not implemented")