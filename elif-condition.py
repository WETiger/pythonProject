##if else if of elif

mark = int(input("Enter your marks :"))

if mark < 0 or mark > 100:
    print("Invalid mark !!! please enter currect mark ")
elif mark >=80 :
    print(" you have got A+")
elif mark >=70 :
    print(" you have got A")
elif mark >=60 :
    print(" you have got A-")
elif mark >=50 :
    print(" you have got B")
elif mark >=40 :
    print(" you have got C")
elif mark >=33 :
    print(" you have got D")
else:
    print("you have got F or fail")