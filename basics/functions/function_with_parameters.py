def climb_ladder(remaining,crossed):
    if remaining > crossed:
        print("still some way to go")
    else:
        print("almost there")

climb_ladder(5,2)
climb_ladder(2,5)