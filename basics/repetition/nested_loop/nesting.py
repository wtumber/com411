def run():
    print("Please enter a sequence:")
    sequence = input()

    print("Please enter the character for the marker:")
    marker = input()

    # Find markers
    marker1_position = -1
    marker2_position = -1

    for position in range(0, len(sequence), 1):
        letter = sequence[position]

        if (letter == marker):
            if (marker1_position == -1):
                marker1_position = position
            else:
                marker2_position = position

    # Display result
    print("The distance between the markers is", marker2_position - marker1_position - 1)