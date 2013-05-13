"""
Write a program that displays each number as they would look in a led digital clock: For example 2, 4 and 8 will look like:

#### #  # ####
   # #  # #  #
#### #### ####
#       # #  #
####    # ####
Note: Each number must be composed of 4x5 characters '#'.

Output 
Print 0123456789 as they would appear in a digital clock

Yes...this is a strange question...
"""
pretty_print = {
0: [
'####',
'#  #',
'#  #',
'#  #',
'####'],
1: [
'   #',
'   #',
'   #',
'   #',
'   #'],
2: [
'####',
'   #',
'####',
'#   ',
'####'],
3: [
'####',
'   #',
'####',
'   #',
'####'],
4: [
'#  #',
'#  #',
'####',
'   #',
'   #'],
5: [
'####',
'#   ',
'####',
'   #',
'####'],
6: [
'####',
'#   ',
'####',
'#  #',
'####'],
7: [
'####',
'   #',
'   #',
'   #',
'   #'],
8: [
'####',
'#  #',
'####',
'#  #',
'####'],
9: [
'####',
'#  #',
'####',
'   #',
'   #']
}

def print_digital(input):
    digital_words = [pretty_print[c] for c in input]
    for lines in zip(*digital_words):
        print ' '.join(lines)

if __name__ == '__main__':
    print_digital(range(10))
