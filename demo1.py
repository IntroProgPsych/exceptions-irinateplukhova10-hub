#1.try if its brake the code , then  2.exept  3.else 4.finally


try:
   number = int(input("Type a number: "))
   1/number
except ZeroDivisionError:
    print("You cant devide by zero")
except:
    print("There was something wrong")
else:
    print("There were no errors")
finally:
    print("This is the and!")