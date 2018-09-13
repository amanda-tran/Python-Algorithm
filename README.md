# Python Algorithm Assignment 1
Algorithm that calculates the day Easter Sunday was on a specific year.

Algorithm:

This algorithm was originally invented by the mathematician Carl Friedrich Gauss:

Ask the user for the year (such as 2001). Save the year in y.
Divide y by 19 and call the remainder a. Ignore the quotient.
Divide y by 100 to get a quotient b and a remainder c.
Divide b by 4 to get a quotient d and a remainder e.
Divide 8 * b + 13 by 25 to get a quotient g. Ignore the remainder.
Divide 19 * a + b - d - g + 15 by 30 to get a remainder h. Ignore the quotient.
Divide c by 4 to get a quotient j and a remainder k.
Divide a + 11 * h by 319 to get a quotient m. Ignore the remainder.
Divide 2 * e + 2 * j - k - h + m + 32 by 7 to get a remainder r. Ignore the quotient.
Divide h - m + r + 90 by 25 to get a quotient n. Ignore the remainder.
Divide h - m + r + n + 19 by 32 to get a remainder p. Ignore the quotient.