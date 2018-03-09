PYTHON AS A CALCULATOR
=======================

FOR A FULL LIST OF MATHEMATICAL OPERATIONS IN PYTHON SEE: https://www.tutorialspoint.com/python/python_basic_operators.htm
This will be useful later, so only skip it if you know it already

QUESTION 1
----------
 ```python
 3, 56, 6, 3, 44, 5, 6, 7775, 32353, 34534, 345
 ```
 
    - For the numbers above find:
      - the largest
      - the smallest
      - the sum of all the numbers
     
    - Use the statistics module to compute:
      - the mean
      - the median
      - the variance
      - and standard deviation

    - Use the math module to calculate the following:
      - the value of pi rounded down to the nearest whole number
      - the value of pi rounded up to nearest whole number
      - the square root of pi
      - the log of pi


```python 
import math 
pi = math.pi
```


    - Calculate: 
      - pi squared divided by pi cubed
      - generate some random numbers
      - what is sine(pi/2), sine(pi/4), sine(pi/8)
      - if the result is in radians, convert it to degrees
      - cast your result from a float into a string


VARIABLE ASSIGNMENT
===================

QUESTION 2
----------

Complete the following

    - assign the number 3 to a variable called width, and the number 110 to a variable called height
    - calculate the area and assign it to a new variable called area
    - turns out you got the width and height mixed up, see if you can swap them without re-declaring the width and height variables
    - assign the width and height variables in a single statement



CONTROL FLOW - USING STATEMENTS
===============================

QUESTION 3
----------

Complete the following:

    - write a simple for loop that counts up to 10 and prints the value
    - use an if statement to print 4 if the value is 4
    - add an else clause to print 'the number is not 4' when it is not 4
    - use an if statement to print if the value is anything other than 4
    - rewrite this using a while loop (HINT: try out using the += operation)



STRING MANIPULATION
===================

IMPORTANT: if you are uncertain what is meant by built-in method, have a look here (https://docs.python.org/3/library/stdtypes.html) # at the different functionality that is built-in to each data type


QUESTION 4
----------

```python
secret_message = 'S1R3E2!!3@4T2R3AT23@@!S2Y3pbO1T3!@@!!4b1E@M134O13C1L3@@Ew41@23!!'
```

For the secret_message variable:

    - remove all digits and special characters from the secret message
    - replace all every letter b with an empty space 
    - if you wrote your answer as a loop, try with a list comprehension
    - reverse the capitalisation
    - reverse the order of the letters
    - use built in string methods to do the following

Do what the strings tell you do do:
```python
s1 = '              please remove the space around me           '
s2 = '               please remove the space on my right           '
s3 = 'please add the same number of spaces on my left as on my right             '
```
    - combine strings s1 and s2
        - do it with and without using built-in string methods
    
    - for a and b (below), compute the following:
        - a + b
        - a * b
```python
a = '3.1' 
b = '22.323'    
```
    - if your result is just one long string, try to cast a and b into integers and try again

    - replace the {}s below with the value of pi using string methods, for 0, 2 and 5 decimal places respectively
```python
print('the value of pi is: {}, {}, {}')
```
    - print the following string: '23\42\34\23\\\//'
    - think about what is going on, google it and see why it doesn't work as expected


WORKING WITH TEXT FILES
=======================
QUESTION 5
----------    

Complete the following:

    - load the example dataset '/resources/strings_example_1.txt'
    - change the vowels back to normal characters
    - locate the hidden substring (HINT: the it starts and ends with __)
    - remove this substring and save the modified text in a new variable. Show that this is no longer the same as the original
    - find the counts of each letter in the text such that:
        - 'aaAabb dddDD hhcc' >>> [('d',5), ('a',4), ('b',2), ('c',2), ('h', 2)]
    - make a separate list for alphabetical, numeric and special characters
        - HINT: you may want to use sets to solve this


QUESTION 6
----------

Complete the following:

    - load the dataset '/resources/strings_example_2.txt'
    - clean the text and create a flat list containing every word    
    - produce a dictionary containing each word as a key and that word's count as the value
    - find the average length of the unique words in the text
    - find the weighted average word lengths


QUESTION 7
----------

Complete the following:

    - modify this code to ensure that email addresses follow the following rules:
        - all lower case
        - takes the first letter of the first name and combines with with the whole last name
        - it removes any extra spaces/unwanted characters
        - it creates multiple email addresses for all the groups in groups_that_need_emails

```python
first_name = input('please enter your first name:')
surname = input('please enter your surname:')
email = first_name + '.' + surname + '@pystarters.co.uk'

print(email)

groups_that_need_emails =  ('pystarters', 'pyclub', 'UCL', 'SWC', 'gatsby')
```


APPLIED QUESTION - DEALING WITH LOTS OF FILES
=============================================

QUESTION 8
----------


You have a folder of serial two photon microscope images ('/resources/tissue_vision_files/') 
containing many (empty) .tif images. The image filenames are of the format mmddyyyy-hhmm-image_index-channel_number.tif

    - generate a list of all the file names
    - sort the lists in a human readable way 
        - HINT: the file names are not zero-padded, which messes up the sorting
    - separate images 100-200 into three separate lists, one for each channel
        - insert 'modified' into all file names: e.g. '02162018-1620-0_01_modified.tif'
        - do not include any files that end with .txt
    - save these files to separate folders
    - what do you think is wrong with these file names? what would you do to make them nicer?


BONUS QUESTION
==============
This is extra, but can be extremely useful for parsing non-standardised messy strings
    - Read about regular expressions here: https://developers.google.com/edu/python/regular-expressions
    - do the baby names exercise on there


