#######################################################################
# Sean King                                                           #
# Structure of Programming Languages Project: Finding the paradigms   #
# of a factorial program in Python. This is one file of the project,  #
# the other being the same program but in C.                          #
# Authored: 4-29-22                                                   #
#######################################################################

class Factorial:  # Declaring a class 'Factorial' which allows for object-oriented programming.

    def factorial(self, int):  # Making a method 'factorial' which takes the factorial of a given
                               # number.
        factorial = 1  # Set the default factorial to 1.

        if int < 0:  # If the number is negative, then it will not find the factorial.
            print("Sorry, the entered integer must be positive.")
        elif int == 0:  # If the number is 0, then its factorial will be 1.
            print("The factorial of 0 is: " + str(factorial))
        else:  # If the number is greater than 0, calculate the factorial.
            for i in range(1, int + 1):
                factorial = factorial * i  # Increases the factorial for every integer between the
                                           # one entered and 1.
            print("The factorial of " + str(int) + " is: " + str(factorial))  # Prints out the factorial.


##################### Creating Factorial objects to find their factorials.
number = Factorial()
number.factorial(-10)

number2 = Factorial()
number2.factorial(10)

number3 = Factorial()
number3.factorial(0)
