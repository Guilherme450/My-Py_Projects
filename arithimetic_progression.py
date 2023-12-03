sequence_of_numbers = []
index = 0

print('*'*40)
print('Arithmetic Progression Algorithm')
print('*'*40)

def general_term_of_pa(first_term, index_of_term, ratio_of_pa):
    nth_term = first_term + (index_of_term - 1) * ratio_of_pa
    return nth_term

def ratio_of_pa(first_term, second_term):
    ratio = second_term - first_term
    return ratio

while True:
    while True:
        index += 1
        try:
            data_to_sequence = float(input(f'Type the value to a{index}: '))
            sequence_of_numbers.append(data_to_sequence)
            if len(sequence_of_numbers) == 2:
                break
        except(ValueError):
            print('ERROR! Only numbers.')
            index -= 1
            continue
    while True:
        show_the_an_term = str(input('Do you wanna find a term?[y/n]: '))
        if show_the_an_term == 'y' or show_the_an_term == 'n':
            break
        else:
            print('Try Again! Only "y" or "n"')
            continue

    if show_the_an_term == 'y' or show_the_an_term == 'Y':
        n_term = int(input('Type the term you wanna find: '))
        ratio_of_the_sequence = ratio_of_pa(sequence_of_numbers[0], sequence_of_numbers[1])
        general_term = general_term_of_pa(sequence_of_numbers[0], n_term, ratio_of_the_sequence)

        print(f'Your sequence: {sequence_of_numbers}')
        print(f'The ratio of your PA is: {ratio_of_the_sequence}')
        print(f'The value of A{n_term}: {general_term}')
        break

    elif show_the_an_term == 'n' or show_the_an_term == 'N':
        print(f'Your sequence: {sequence_of_numbers}')
        ratio_of_the_sequence = ratio_of_pa(sequence_of_numbers[0], sequence_of_numbers[1])
        print(f'The ratio of your PA is: {ratio_of_the_sequence}')
        break
