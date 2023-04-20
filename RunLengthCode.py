# Run Length Code

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # if the prev and current characters
        # don't match ...
        if char != prev_char:
            # ... then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char

            count = 1
            prev_char = char
        else:
            # or increment our counter
            # if the characters do match
            count +=1
    # else:
        # Finish off the encoding
    encoding += str(count) + prev_char
    return encoding

def rle_decode(data):
    decode = ''
    for char in data:
        # If the character is numerical ...
        if char.isdigit():
            # ... appand it to our count
            count = int(char)
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * count
    return decode


enoded_val = rle_encode('AAAAAFDDCCCCCCCCCCCAEEEEEEEEE')
print(enoded_val)

decoded_val = rle_decode('5A1F2D11C1A9E')
print(decoded_val)
