def main():
#  File: EasterSunday.py
#  Description: Algorithm that calcultes the date of Easter Sunday on a specific year.
#  Student's Name: Amanda Tran  
#  Student's UT EID: at35245
#  Course Name: CS 303E 
#  Unique Number: 51205
#
#  Date Created: 9/9/2018
#  Date Last Modified: 9/9/2018

    #Asks user for input of year
    # Step 1
    y = eval ( input ( "Enter year: ") )

    # Algorithm start
    # Step 2
    a = y % 19

    # Step 3
    b = y // 100
    c = y % 100
        
    # Step 4
    d = b // 4
    e = b % 4
        
    # Step 5
    g = ( 8 * b + 13 ) // 25
        
    # Step 6
    h = ( 19 * a + b - d - g + 15) % 30
        
    # Step 7
    j = c // 4
    k = c % 4
        
    # Step 8
    m = ( a + 11 * h ) // 319
        
    # Step 9
    r = ( 2 * e + 2 * j - k - h + m + 32 ) % 7
        
    # Step 10
    n = ( h - m + r + 90) // 25
        
    # Step 11
    p = ( h - m + r + n + 19 ) % 32

    # End of Algorithm
        
    if ( n == 3):
        print("In", y, "Easter Sunday is on", p, "March.")
    else:
        print("In", y, "Easter Sunday is on", p, "April.")

main()
