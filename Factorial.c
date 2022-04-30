////////////////////////////////////////////////////////////////////////
// Sean King                                                          //
// Structure of Programming Languages Project: Finding the paradigms  //  
// of a factorial program in C. This is one file of the project,      //
// the other being the same program but in Python.                    //    
// Authored: 4-29-22                                                  //
////////////////////////////////////////////////////////////////////////

#include <stdio.h>  // Importing the correct library.


int main() {  // Start of main function.

    int number;  // Declare the number the user will enter and set the
    long int factorial = 1;  // default factorial to 1.

    printf("Please enter a number: ");
    scanf("%d", &number);  // User enters the number.

    if (number < 0) {  // If the number is less than 0, it does not have
                       // a factorial.
        printf("That number does not have a factorial.");
    }
    else if (number == 0) {  // If the number is 0, its factorial is 1.
        printf("The factorial of 0 is: %ld", factorial);
    }
    else {  // If the number is greater than 0, calculate its factorial.
        for (int i = 1; i <= number; ++i) {
            factorial *= i;
        }
        printf("The factorial of %d is: %ld", number, factorial);  // Print
                                                                   // out the
                                                                   // number's
                                                                   // factorial.
    }

    printf("\n");
    return 0;  // End the program.
}
