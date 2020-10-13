def ascii_character():
    print("Program Started!\nPlease enter an ascii code:")
    code = abs(int(input()))
    if code in range(32,127,1):
        letter = chr(code)
        print("Ascii code {} is letter {}".format(code, letter))
    else:
        print("Did not input valid code")
    print("Program ended")

ascii_character()