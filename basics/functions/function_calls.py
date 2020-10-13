def display_box(word):
    print("[",word,"]")

def display_lower_case(word):
    print(word.lower())

def display_upper_case(word):
    print(word.upper())

def display_mirrored(word):
    print(word," | ",word[::-1])

def repeat_word(word):
    repeat_no = int(input())
    for repeat in range(repeat_no):
        if repeat % 2==0:
            print(word.lower())
        else:
            print(word.upper())

def run_program():
    print("choose a word")
    word= input()
    print("1) Display in a Box – display the word in an ascii art box\n2) Display Lower-case – display the word in lower-case e.g. hello\n3) Display Upper-case – display the word in upper-case e.g. HELLO\n4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH\n5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
    num_chosen = int(input())
    if num_chosen == 1:
        display_box(word)
    elif num_chosen == 2:
        display_lower_case(word)
    elif num_chosen == 3:
        display_upper_case(word)
    elif num_chosen == 4:
        display_mirrored(word)
    else:
        repeat_word(word)

   # attempt_select = {1:display_box(word),
   #                     2:display_lower_case(word),
   #                     3:display_upper_case(word),
   #                     4:display_mirrored(word),
   #                     5:repeat_word(word)}
   # attempt_select[num_chosen]

run_program()