# Booths Division Algorithm

This program implements Booth's algorithm to perform division of two numbers. The algorithm is used to perform multiplication or division of binary numbers.

## Prerequisites
- Python 3.10.2 or above
- Binary.py module (included)

## How to use
Run the program.
- Enter the number of bits for the registers.
- Enter the dividend and divisor values in the corresponding binary or 2's complement form.
- The program will output the intermediate steps for each cycle and the final quotient and remainder.

## Inputs
The program accepts the following inputs:

- no_bits: Number of bits for the registers.
- dividend: Dividend value in binary or 2's complement form.
- divisor: Divisor value in binary or 2's complement form.

## Outputs
The program outputs the following:
- Intermediate steps for each cycle.
- Final quotient and remainder.

## Example
**Input:**
```
Enter the number of bits : 12
Enter the Values in the corresponding binary or 2's complement form
Enter the divident  : 110101101
Enter the divisor : 1101
```

**Output:**
```
     A            Q            M

000000000000 000110101101 000000001101   Initial Values

000000000000 001101011010 000000001101   Shift left A, Q            ─┐
111111110011 001101011010 000000001101   A <- A - M                  ├── Cycle 1
000000000000 001101011010 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000000 011010110100 000000001101   Shift left A, Q            ─┐
111111110011 011010110100 000000001101   A <- A - M                  ├── Cycle 2
000000000000 011010110100 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000000 110101101000 000000001101   Shift left A, Q            ─┐
111111110011 110101101000 000000001101   A <- A - M                  ├── Cycle 3
000000000000 110101101000 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000001 101011010000 000000001101   Shift left A, Q            ─┐
111111110100 101011010000 000000001101   A <- A - M                  ├── Cycle 4
000000000001 101011010000 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000011 010110100000 000000001101   Shift left A, Q            ─┐
111111110110 010110100000 000000001101   A <- A - M                  ├── Cycle 5
000000000011 010110100000 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000110 101101000000 000000001101   Shift left A, Q            ─┐
111111111001 101101000000 000000001101   A <- A - M                  ├── Cycle 6
000000000110 101101000000 000000001101   Restore A, Set Q[0] = 0    ─┘

000000001101 011010000000 000000001101   Shift left A, Q            ─┐
000000000000 011010000000 000000001101   A <- A - M                  ├── Cycle 7
000000000000 011010000001 000000001101   Set Q[0] = 1               ─┘

000000000000 110100000010 000000001101   Shift left A, Q            ─┐
111111110011 110100000010 000000001101   A <- A - M                  ├── Cycle 8
000000000000 110100000010 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000001 101000000100 000000001101   Shift left A, Q            ─┐
111111110100 101000000100 000000001101   A <- A - M                  ├── Cycle 9
000000000001 101000000100 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000011 010000001000 000000001101   Shift left A, Q            ─┐
111111110110 010000001000 000000001101   A <- A - M                  ├── Cycle 10
000000000011 010000001000 000000001101   Restore A, Set Q[0] = 0    ─┘

000000000110 100000010000 000000001101   Shift left A, Q            ─┐
111111111001 100000010000 000000001101   A <- A - M                  ├── Cycle 11
000000000110 100000010000 000000001101   Restore A, Set Q[0] = 0    ─┘

000000001101 000000100000 000000001101   Shift left A, Q            ─┐
000000000000 000000100000 000000001101   A <- A - M                  ├── Cycle 12
000000000000 000000100001 000000001101   Set Q[0] = 1               ─┘

Quotient : 000000100001         (33)
Remainder : 000000000000        (0)
```

## Credits
This program was developed by Valerian Coelho. It uses the Binary Library, which were developed by the same author.
