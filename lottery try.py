######THIS IS A REPRESENTATION OF A TRIAL FOR A LOTTERY MACHINE OR SLOT MACHINE AS USED IN CASINOS.


while True:
    i=input('Input any random number between 0 and 16:_')
    item=['lost','lost','lost','won','lost','lost','lost','won','lost','lost','won','won','won','lost','lost','lost','won']

    if i=='0':
        print(item[0])
    elif i=='1':
        print(item[1])
    elif i=='2':
        print(item[2])
    elif i=='3':
        print(item[3])
        print('You are a winner!!')
    elif i=='4':
        print(item[4])
        continue
    else:
        print('Out of parameter!')
        

    
    

    
    
