''' vowel print program
latter = input('Enter and latter from a to z :')

if latter == 'a' or latter == 'A' or latter == 'e' or latter =='E' or latter == 'o' or latter =='O' or latter == 'i' or latter=='I' or latter == 'u' or latter =='U' :
    print(latter + ' is Vowel ')
else:
    print(latter + " is Consonant")

'''
# leap year program

year = int(input("Enter a year : "))

if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0 :
    print(year ," is a leap year")
else:
    print(year ,' is not a leap year')