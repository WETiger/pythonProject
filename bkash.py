bkashCode = input("Enter Bkash(*247#) code :")

password = '12345'

if bkashCode == '*247#':
    print("bKash \n"
          "1. Send Money \n"
          "2. Mobile Recharge \n"
          "3. Payment \n"
          "4. Cash Out \n"
          "5. Pay bill \n"
          "6. My Balance \n"
          "7. Helpline"
          )
###1 . send money start
    code1 = input()
    if code1 == '1':
        sendNumber = input('Enter Receiver bKash Account No: \n')
        sendReferance = input('Enter Reference : \n')
        amountSend = input('Enter Amount \n')
        print('Send Money.\n'
              'To:'+sendNumber+'\n'
              'Amount Tk'+amountSend +'\n'
              'Reference:'+sendReferance+'\n')

        passwordMoney = input('Enter Menu PIN to confirm : \n')
        if passwordMoney == password :
            print('Send Money Tk '+ amountSend +' to successful.')
        else:
            print('invalid password')
### 1. send money end
    elif code1 == '2' :
        print()
else:
    print("invalid input")