#check if single letter that is ascii
def check_ascii():
    print("Program Started!\nPlease enter a letter:")
    letter = input()
    if len(letter) == 1:
        ascii_letter = ord(letter)
        print("Ascii for {} is {}".format(letter, ascii_letter))
    else:
        print("Not a single letter")
    print("Program Ended")

check_ascii()