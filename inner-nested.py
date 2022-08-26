press = int(input("Enter 121 for check somthing :"))

if press == 121:
    print(" 0 - for balance \n 1 - withdraw \n 2 - cashout")
    press1 = int(input("enter 0 or 1 or 2 :"))
    if press1 == 0:
        print('balance')
    elif press1 ==1 :
        print('withdraw')
    elif press1 == 2:
        print('cashout')
    else:
        print(press1 ,' out')
else:
    print('wrong input')
