def display_ladder(steps):
    print("| |\n---\n"*steps)
display_ladder(5)

def create_ladder():
    print("Enter steps")
    remaining = int(input())
    print("| |\n---\n"*remaining)
create_ladder()