import os
import Binary as binary

no_bits = int(input('Enter the number of bits : '))

print('Enter the Values in the corresponding binary or 2\'s complement form')

dividend = input('Enter the divident  : ')

divisor = input('Enter the divisor : ')

# A, Q, M are the register used in Booth's Algorithm

A = format(0, f'0{no_bits}')

Q = format(int(dividend), f'0{no_bits}')

M = format(int(divisor), f'0{no_bits}')

# Clears the terminal screen
os.system('cls')

# Prints the first line of the output
print(f'{"A": ^{no_bits}} {"Q": ^{no_bits}} {"M": ^{no_bits}}\n')

# Prints what the initial values of A Q and M are
print(A, Q, M, '  Initial Values\n')

for i in range(no_bits):

    # Performs the Left shift
    Q, MSB = binary.left_shift(Q, '0')
    A, MSB = binary.left_shift(A, MSB)

    # Prints the value of registers after Left shift
    print(A, Q, M, '  Shift left A, Q            ─┐')

    # Performs A <- A - M, by taking two's complement of M, and adding it to A
    A = binary.add(A, binary.twos_complement(M))

    # Prints the value of registers after Subtraction
    print(A, Q, M, '  A <- A - M', f'                 ├── Cycle {i+1}')

    # Checks to see if the MSB bit of A is 1 or 0
    if A[0] == '1':
        # Replaces the LSB bit of Q with 0
        Q = Q[:len(Q)-1] + '0'

        # Performs A <- A + M, this restore the original value of A
        A = binary.add(A, M)

        # Prints the value after restoring and setting Q[0] = 0
        print(A, Q, M, '  Restore A, Set Q[0] = 0    ─┘')

    else:
        # Replaces the LSB of Q with 1
        Q = Q[:len(Q)-1] + '1'

        # Prints the value after setting Q[0] = 1
        print(A, Q, M, '  Set Q[0] = 1               ─┘')

    # Prints an extra line after each iteration
    print('')

print('Quotient :', Q, f'\t({int(Q, 2)})')
print('Remainder :', A, f'\t({int(A, 2)})')

os.system('pause')