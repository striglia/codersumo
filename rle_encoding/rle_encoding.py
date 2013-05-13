import sys

def rle_encoding(string):
    """Take a string and return the RLE encoding of it."""
    encoded_str = ''
    letter_count = 0
    last_letter = string[0]
    for letter in string:
        if last_letter != letter:
            encoded_str += '%d%s' % (letter_count, last_letter)
            letter_count = 1
            last_letter = letter
        else:
            letter_count += 1
    encoded_str += '%d%s' % (letter_count, last_letter)
    return encoded_str


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        print rle_encoding(line.strip())
