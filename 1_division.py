# Exercise 1: Safe division with try / except / else / finally
# ------------------------------------------------------------
# Ask the user for two numbers and attempt to divide them.
# If the user enters invalid values or tries division by zero,
# display an error message.
# If division succeeds, print the result inside the else block.
# The finally block should always print: "Operation finished."

# Sample Input:
# Enter the numerator: 12
# Enter the denominator: 3
#
# Sample Output:
# Division successful! Result: 4.0
# Operation finished.
#


# Sample Input (Error):
# Enter the numerator: 10
# Enter the denominator: zero
#
# Sample Output:
# Error: You must enter numeric values.
# Operation finished.

# write your code here:


try:
    number1 = int(input("Please write number: "))
    number2 = int(input("Type one more number: "))  
    result = number1 / number2

except:
    print("There was something wrong")
else:
    print("There were no errors")
finally:
       
    print(f"Division successful! Result: {result}")
    print("Operation finished.")

    