def fizzbuzz(n):
    response = ''
    if n % 3 == 0:
        response += 'fizz'
    if n % 5 == 0:
        response += 'buzz'

    if not response:
        response = n
    return response

for n in range(100):
    print fizzbuzz(n)
