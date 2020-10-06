print("pick 1,2, or 3")
pick = int(input())

if pick == 1:
    print("pick a or b")
    pick_a_b = input()
    if pick_a_b == "a":
        print("foo")
    else:
        print("bar")
elif pick == 2:
    print("pick c or d")
    pick_c_d =input()
    print("pick e or f")
    pick_e_f =input()

    if pick_c_d == "c" and pick_e_f == "e":
        print("and operator")
    elif pick_c_d == "d" and pick_e_f == "f":
        print("and operator 2")
    else:
        print("boo")
else:
    print("you picked 3")

