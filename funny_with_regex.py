import re


# Not sure if this masterpiece works on Python 3.7 (which is used for auto-grading tool of FBT)
# Thanks to iluxonchik for this masterpiece: https://iluxonchik.github.io/regular-expression-check-if-number-is-prime/
def is_prime(number):
    return not re.match(r'^.?$|^(..+?)\1+$', '1' * number)


