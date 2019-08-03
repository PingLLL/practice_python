import random
def gen_passwd():
    counter = 1
    result = ''
    while counter <= 8:
            digit = random.choice('abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*AB')
            result += digit
            counter += 1
    return result

print(gen_passwd())
