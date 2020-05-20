import string, random

def genPass(num):
    password = ''

    for n in range(num):
        x = random.randint(0,94)
        password += string.printable[x]
    return password
print genPass(16)

    

 
