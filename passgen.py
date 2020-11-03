from random import randint
i = 0
pass_length = 10
passw = ""

def rnd(x):
    if(x == 1):
        y = "a"
    elif(x == 2):
        y = "b"
    elif(x == 3):
        y = "c"
    elif(x == 4):
        y = "d"
    elif(x == 5):
        y = "e"
    elif(x == 6):
        y = "f"
    elif(x == 7):
        y = "g"
    elif(x == 8):
        y = "h"
    elif(x == 9):
        y = "i"
    elif(x == 10):
        y = "j"
    elif(x == 11):
        y = "k"
    elif(x == 12):
        y = "l"
    elif(x == 13):
        y = "m"
    elif(x == 14):
        y = "n"
    elif(x == 15):
        y = "o"
    elif(x == 16):
        y = "p"
    elif(x == 17):
        y = "q"
    elif(x == 18):
        y = "r"
    elif(x == 19):
        y = "s"
    elif(x == 20):
        y = "t"
    elif(x == 21):
        y = "u"
    elif(x == 22):
        y = "v"
    elif(x == 23):
        y = "w"
    elif(x == 24):
        y = "x"
    elif(x == 25):
        y = "y"
    elif(x == 26):
        y = "z"
    elif(x == 27):
        y = "0"
    elif(x == 28):
        y = "1"
    elif(x == 29):
        y = "2"
    elif(x == 30):
        y = "3"
    elif(x == 31):
        y = "4"
    elif(x == 32):
        y = "5"
    elif(x == 33):
        y = "6"
    elif(x == 34):
        y = "7"
    elif(x == 35):
        y = "8"
    elif(x == 36):
        y = "9"
    elif(x == 37):
        y = "."
    elif(x == 38):
        y = "!"
    elif(x == 39):
        y = "&"
    elif(x == 40):
        y = "é"
    elif(x == 41):
        y = "µ"
    elif(x == 42):
        y = "*"
    elif(x == 43):
        y = "%"
    elif(x == 44):
        y = ";"
    elif(x == 45):
        y = "?"
    elif(x == 46):
        y = "A"
    elif(x == 47):
        y = "B"
    elif(x == 48):
        y = "C"
    elif(x == 49):
        y = "D"
    elif(x == 50):
        y = "E"
    elif(x == 51):
        y = "F"
    elif(x == 52):
        y = "G"
    elif(x == 53):
        y = "H"
    elif(x == 54):
        y = "I"
    elif(x == 55):
        y = "J"
    elif(x == 56):
        y = "K"
    elif(x == 57):
        y = "L"
    elif(x == 58):
        y = "M"
    elif(x == 59):
        y = "N"
    elif(x == 60):
        y = "O"
    elif(x == 61):
        y = "P"
    elif(x == 62):
        y = "Q"
    elif(x == 63):
        y = "R"
    elif(x == 64):
        y = "S"
    elif(x == 65):
        y = "T"
    elif(x == 66):
        y = "U"
    elif(x == 67):
        y = "V"
    elif(x == 68):
        y = "W"
    elif(x == 69):
        y = "X"
    elif(x == 70):
        y = "Y"
    elif(x == 71):
        y = "Z"
    elif(x == 72):
        y = "-"
    elif(x == 73):
        y = "_"
    elif(x == 74):
        y = "^"
    elif(x == 75):
        y = "~"
    elif(x == 76):
        y = "/"
    elif(x == 77):
        y = "+"
    elif(x == 78):
        y = "="
    elif(x == 79):
        y = "€"
    elif(x == 80):
        y = "<"
    elif(x == 81):
        y = ">"
    elif(x == 82):
        y = "\\"
        
        
    return y
    






while i < pass_length:
    x = randint(1,82)
    y = rnd(x)
    passw = passw + "" + str(y)
    i += 1
print("password: " + str(passw))


