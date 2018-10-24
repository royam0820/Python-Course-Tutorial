def collatz(number):
    if number % 2 == 0:
        # print (number // 2)
        return number // 2
    else:
        # print (3 * number + 1)
        return 3 * number + 1

if __name__ == '__main__':
    print ('Enter number:')
    try:
        number = int(input())
        while True:
            if number != 1:
                number = collatz(number)
                print (number)
            else:
                break
    except:
        print ('Error: Invalid Value. You did not enter an integer.')
