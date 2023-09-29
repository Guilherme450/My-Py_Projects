import math
from time import sleep

while True:
    try:
        coefficient_A = int(input('Type a value to coefficient \u001b[34ma\u001b[0m: '))
        coefficient_B = int(input('Type a value to coefficient \u001b[33mb\u001b[0m: '))
        coefficient_C = int(input('Type a value to coefficient \u001b[36mc\u001b[0m: '))
    except ValueError:
        print('\u001b[31mInteger numbers only\u001b[0m')
        continue

    if coefficient_A != 0:
        Delta = coefficient_B**2 - 4*coefficient_A*coefficient_C
        if Delta >= 0:
            first_Root = ((-coefficient_B + (math.sqrt(Delta))) / (2*coefficient_A))
            second_Root = ((-coefficient_B - (math.sqrt(Delta))) / (2*coefficient_A))
            if first_Root == second_Root:
                single_root = first_Root
                sleep(1.5)
                print(f'The root of equation will be: X=\u001b[32m{"%.2f"%single_root}\u001b[0m')
                break
            else:
                sleep(1.5)
                print(f'The roots of equation will be: X1=\u001b[32m{"%.2f"%first_Root}\u001b[0m e X2=\u001b[32m{"%.2f"%second_Root}\u001b[0m')
                break
        else:
            sleep(1.5)
            print('\u001b[31mThere are no values to X!\u001b[0m')
            break
    else:
        print('\u001b[32mO coefficient a can not be zero!\u001b[0m')
        continue
