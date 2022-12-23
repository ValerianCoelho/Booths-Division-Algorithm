def left_shift(number, LSB): # 'number' is an string, 'LSB' is the bit to be replaced at the LSB
    MSB = number[0]
    number = number[1:] + LSB
    return number, MSB

def add(A, M):
    result = format(int(A, 2) + int(M, 2), 'b')
    return result[len(result)-len(A):]

def twos_complement(number):
    result = format(((2**len(number)-1)-int(number, 2)+1), 'b')
    return result