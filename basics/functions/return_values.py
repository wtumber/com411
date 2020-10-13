def sum_weights(bot_1_weight, bot_2_weight):
    total_weight = bot_1_weight + bot_2_weight
    return total_weight 

def calc_avg_weight(bot_1_weight, bot_2_weight):
    total_bot_weight = sum_weights(bot_1_weight, bot_2_weight)
    avg_weight = total_bot_weight / 2
    return avg_weight

def run():
    print("Enter bot 1 weight")
    bt_1_wght = int(input())
    print("Enter bot 2 weight")
    bt_2_wght = int(input())
    print("sum or avg")
    to_do = input()

    if to_do == "sum":
        to_do_sum = sum_weights(bt_1_wght,bt_2_wght)
        return to_do_sum
    elif to_do == "avg":
        to_do_avg = calc_avg_weight(bt_1_wght,bt_2_wght)
        return to_do_avg
    else:
        print("enter sum or avg next time")

run()

