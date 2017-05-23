__author__ = 'Thiago do Prado'

#region HEADER
def header():
    print("######################################################################################################")
    print("################################  CONVERTER FOR BASES 2, 7, 10 and 16 ################################")
    print("######################################################################################################")
    print("")
    print("######################################################################################################")
    print("# THIS PROGRAM WAS MADE FOR FUNDAMENTALS OF COMPUTER ARCHITECTURE AT UNIVERSIDADE FEDERAL FLUMINENSE #")
    print("######################################################################################################")
    print("")
    print("######################################################################################################")
    print("######################################## I HOPE YOU ENJOY IT #########################################")
    print("######################################################################################################")
    print("")

    init()
#endregion

#region MAIN STRUCTURE
def init():
    print("")
    input_temp = raw_input("Enter as: N I O, where N is a real number, I is the input basis and O is the output basis: ")
    input = format(input_temp)

    verifying(input)


def convert(input):
    total = 0

    if(input[2] == "2"):
        total = to_binary(input)
    elif(input[2] == "7"):
        total = to_heptal(input)
    elif(input[2] == "10"):
        total = to_decimal(input)
    elif(input[2] == "16"):
        total = to_hexadecimal(input)

    answer(input[0], input[1], input[2], total)


def answer(number, initial_base, final_base, result):
    print("Converting " + number + " in the base " + initial_base + " to the base " + final_base + " you get " + str(result))

    restart()


def restart():
    print("")
    again = raw_input("Do you want to convert another number? Y for yes, other keys will close the application: ")

    if(again.upper() == "Y"):
        init()
    else:
        print("See you soon!")
#endregion

#region UTILITIES
def format(input):
    input = input.upper()
    input_formated = input.split(" ")

    return input_formated


def verifying(input):
    if(len(input) != 3):
        return try_again()
    elif(input[1] != "2" and input[1] != "7" and input[1] != "10" and input[1] != "16"):
        return try_again()
    elif(input[2] != "2" and input[2] != "7" and input[2] != "10" and input[2] != "16"):
        return try_again()

    verifying_base(input)


def verifying_base(input):
    if(input[1] == "2"):
        for i in range(0, len(input[0])):
            if(input[0][i] != "0" and input[0][i] != "1"):
                return try_again()

    if(input[1] == "7"):
        for i in range(0, len(input[0])):
            if(input[0][i] != "0" and input[0][i] != "1" and input[0][i] != "2" and input[0][i] != "3" and input[0][i] != "4" and input[0][i] != "5" and input[0][i] != "6"):
                return try_again()

    if(input[1] == "10"):
        for i in range(0, len(input[0])):
            if(input[0][i] != "0" and input[0][i] != "1" and input[0][i] != "2" and input[0][i] != "3" and input[0][i] != "4" and input[0][i] != "5" and input[0][i] != "6" and input[0][i] != "7" and input[0][i] != "8" and input[0][i] != "9"):
                return try_again()

    if(input[1] == "16"):
        for i in range(0, len(input[0])):
            if(input[0][i] != "0" and input[0][i] != "1" and input[0][i] != "2" and input[0][i] != "3" and input[0][i] != "4" and input[0][i] != "5" and input[0][i] != "6" and input[0][i] != "7" and input[0][i] != "8" and input[0][i] != "9" and input[0][i] != "A" and input[0][i] != "B" and input[0][i] != "C" and input[0][i] != "D" and input[0][i] != "E" and input[0][i] != "F"):
                return try_again()

    convert(input)


def try_again():
    print("")
    print ("YOU DID NOT ENTER AS THE EXAMPLE.")
    print ("PLEASE, TRY AGAIN.")
    init()
#endregion

#region CONVERSIONS
def to_binary(input):
    temp = to_decimal(input)
    inter = ""
    total = ""

    while(temp != 0):
        rest = temp % 2
        temp = temp // 2

        inter = inter + str(rest)

    for i in range(0, len(inter)):
        total = total + inter[len(inter) - (i + 1)]

    return int(total)


def to_heptal(input):
    temp = to_decimal(input)
    inter = ""
    total = ""

    while(temp != 0):
        rest = temp % 7
        temp = temp // 7

        inter = inter + str(rest)

    for i in range(0, len(inter)):
        total = total + inter[len(inter) - (i + 1)]

    return int(total)


def to_decimal(input):
    total = 0

    if(input[1] == "2"):
        for i in range(0, len(input[0])):
            current = int(input[0][i]) * 2 ** (len(input[0]) - (i +1))
            total = total + current

        return total

    elif(input[1] == "7"):
        for i in range(0, len(input[0])):
            current = int(input[0][i]) * 7 ** (len(input[0]) - (i +1))
            total = total + current

        return total

    elif(input[1] == "16"):
        for i in range(0, len(input[0])):
            if(input[0][i] == "A"):
                current = 10 * 16 ** (len(input[0]) - (i +1))
            elif(input[0][i] == "B"):
                current = 11 * 16 ** (len(input[0]) - (i +1))
            elif(input[0][i] == "C"):
                current = 12 * 16 ** (len(input[0]) - (i +1))
            elif(input[0][i] == "D"):
                current = 13 * 16 ** (len(input[0]) - (i +1))
            elif(input[0][i] == "E"):
                current = 14 * 16 ** (len(input[0]) - (i +1))
            elif(input[0][i] == "F"):
                current = 15 * 16 ** (len(input[0]) - (i +1))
            else:
                current = int(input[0][i]) * 16 ** (len(input[0]) - (i +1))

            total = total + current

        return total

    elif(input[1] == "10"):
        return int(input[0])


def to_hexadecimal(input):
    temp = to_decimal(input)
    inter = ""
    total = ""

    while(temp != 0):
        rest = temp % 16
        temp = temp // 16

        if(rest == 10):
            inter = inter + "A"

        elif(rest == 11):
            inter = inter + "B"

        elif(rest == 12):
            inter = inter + "C"

        elif(rest == 13):
            inter = inter + "D"

        elif(rest == 14):
            inter = inter + "E"

        elif(rest == 15):
            inter = inter + "F"

        else:
            inter = inter + str(rest)

    for i in range(0, len(inter)):
        total = total + inter[len(inter) - (i + 1)]

    return total
#endregion

header()