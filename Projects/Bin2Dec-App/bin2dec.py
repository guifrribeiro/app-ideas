def bin2dec(binNumber):
    return int(binNumber, 2)

def num_digits(bin):
    if len(bin) > 8:
        return False
    return True

def is_binary_number(bin):
    valid_digits = '01'

    for char in bin:
        if char not in valid_digits:
            return False
        else:
            pass
    return True

def main():
    while True:
        binNumber = input('Enter the binary number to convert: ')
        if is_binary_number(binNumber) == False:
            print('The value entered is not a binary number.')
        else:
            if num_digits(binNumber) == False:
                print('Your binary number must contain a maximum of 8 digits.')     
            else:
                break
        
    decNumber = bin2dec(binNumber)
    print(decNumber)

main()