import random

def password(length):
    pw = str()
    characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"
    for i in range(length):
        pw = pw + random.choice(characters)
    print(pw)
    return pw


password(10)

    
