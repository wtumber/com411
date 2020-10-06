# Ask user for book details
print("cover type?")
cover_type = input()

# Display appropriate message
if (cover_type == "soft"):
    print("perfect-bound?")
    perfect_bound = input()

    if (perfect_bound == "yes"):
        print("this is popular")
    else:
        print("coils or stitches are good for short books") 
else:
    print("hard covers are more expensive")