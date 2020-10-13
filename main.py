import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.ascii_art as ascii_art

import basics.input.ascii_robot as ascii_robot
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input
import basics.repetition.for_loop.range as range_operator
import basics.repetition.nested_loop.nesting as nesting
import basics.repetition.while_loop.ascii as charging_ascii
import basics.decisions.review as decision_review
import basics.functions.function_calls as function_calls

def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if (response == "simple_message"):
        simple_message.run()
    elif (response == "multiline_message"):
        multiline_message.run()
    elif (response == "ascii_art"):
        ascii_art.run()
    elif (response == "ascii_robot"):
        ascii_robot.run()
    elif (response == "string_operators"):
        string_operators.run()
    elif (response == "user_input"):
        user_input.run()
    elif (response == "range_operator"):
        range_operator.run()  
    elif (response == "nesting"):
        nesting.run()  
    elif (response == "charging_ascii"):
        charging_ascii.run()
    elif (response == "decision_review"):
        decision_review.run()
    else:
        function_calls.run()    
    


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()