#T##########_______THIS IS A SAMPLE CODE TO ACT AS A CALCULATOR_______##########

#STEP 1

while True:
    print('Options for calculating:')
    print('Insert "add" for addition')
    print('Insert "sub" for subtraction')
    print('Insert "mul" for multiplication')
    print('Insert "div" for division')
    print('Insert "rem" for finding remainder of ')
    print('Insert "dib" for number of times a number is divisible by')
    print('Insert "per" for percentage')
    print('Insert  "quit" to stop calculator')
    i = input(':')

##STEP 2

    if i == 'quit':
        break

    elif  i == 'add':
        n1 = float(input('Insert number;'))
        n2= float(input('Insert another number:'))
        r=str(n1 + n2)
        print('Answer is:_ ' + r)

    elif  i == 'sub':
        n1 = float(input('Insert number;'))
        n2= float(input('Insert another number:'))
        r=str(n1 - n2)
        print('Answer is:_ ' + r)

    elif  i == 'mul':
        n1 = float(input('Insert number;'))
        n2= float(input('Insert another number:'))
        r=str(n1 * n2)
        print('Answer is:_ ' + r)

    elif  i == 'div':
        n1 = float(input('Insert number;'))
        n2= float(input('Insert another number:'))
        r=str(n1 / n2)
        print('Answer is:_ ' + r)

    else:
        print('invalid input')
        

    
    
