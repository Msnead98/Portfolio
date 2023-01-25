import random
import string


def password(amount, flag):
    "Gives you random password"
    flag = flag
    nu = int(amount)
    alpha = list(string.ascii_letters)
    num = []
    for i in range(10):
        num.append(str(i))

    text = """~-`-!-@-#-$-%-^-&-*-.-?"""
    sym = text.split("-")
    password_reg = [sym, alpha, num]
    password_ns = [alpha, num]
    password = []

    if flag:
        for i in range(nu):
            new = random.choice(password_reg)
            password.append(random.choice(new))

            final = ''.join(password)


    elif not flag:
        for i in range(amount):
            new = random.choice(password_ns)
            password.append(random.choice(new))

            final = ''.join(password)

    return final


def radiobuttonconvert(num):
    "Converts radio button to boolean"
    flag = True
    if num == 0:
        flag = True
    elif num == 1:
        flag = False

    return flag
