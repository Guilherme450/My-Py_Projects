from time import sleep

capital_list = []
fee_tax_list = []
time_list = []

entrance_phrase = "Calculator of fees"

def show_welcome(phrase):
    print("-" * len(phrase))
    print(phrase)
    print("-" * len(phrase))

def show_help():
    print('*' * 30)
    print('1) sp ----> simple fee command')
    print('2) cmp ----> compost fee command')
    print('3) help ----> open help command')
    print('4) quit ----> finish program command')
    print('*' * 30)

def simple_fee_calc(capital, fee_tax, time):
    total = capital + (capital * (fee_tax / 100) * time)
    return total

def compost_fee_calc(capital, fee_tax, time):
    total = capital * (1 + (fee_tax / 100))**time
    return total

def get_float_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_float_input(prompt)

def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_int_input(prompt)

def user_data_input():
    capital_list.append(get_float_input('Type the capital($): '))
    fee_tax_list.append(get_float_input('Type the fee tax in percentage(%): '))
    time_list.append(get_int_input('Type the time: '))

show_welcome(entrance_phrase)
show_help()

while True:
    if len(capital_list) >= 1 and len(fee_tax_list) >= 1 and len(time_list) >= 1:
        capital_list.clear()
        fee_tax_list.clear()
        time_list.clear()
    else:
        type_keyword = str(input('> '))
        if type_keyword == "help":
            show_help()
        elif type_keyword == "quit":
            user_confirm_quit = str(input('Are you sure you want to quit the program?[y/n]: '))
            if user_confirm_quit == 'y':
                print('Bye')
                break
        elif type_keyword == 'sp':
            user_data_input()
            result_simple_fees = simple_fee_calc(capital_list[0], fee_tax_list[0], time_list[0])
            sleep(0.5)
            print(f'You will have: {"%.2f" % result_simple_fees}$ in simple fee at the end.')
        elif type_keyword == 'cmp':
            user_data_input()
            result_compost_fees = compost_fee_calc(capital_list[0], fee_tax_list[0], time_list[0])
            sleep(0.5)
            print(f'You will have: {"%.2f" % result_compost_fees}$ in compost fee at the end.')