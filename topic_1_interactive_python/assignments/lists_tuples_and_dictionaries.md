LIST BASICS
===========


QUESTION 1
----------


    - make replicate_me 10 times longer i.e. [1] >> [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

```python
replicate_me = [1]
```

    - combine the newly extended replicate_me with replicate_me

```python
combine_me = [2,2,2,2,2,2]
```

    - replace the 4th number in the list with the variable substitute_me
    	- do it again with a different method

```python
substitute_me = ['surprise!']
```

    - replace every other element in the list with the number 5
    	- HINT: you can do this in a single command
    
    - delete elements 5-8 from the list
    - add the numbers 8, 13 and the string 'hello' to the end of your list
    	- do it again with a different method
    - reverse the order of the list
    - in one statement, return the 5th element of your list and remove it from the list
    - assign your list to a new variable called 'copy_of_list'
    - change all the elements in this new list to zeros
    - print out the original list (not the copy)
    - what happens? did you expect that? find a way to copy the list properly
    	- think about or read about why this is the case in python


NESTED LISTS
============

QUESTION 2
----------

You have some experimental data (trials_1 and trials_2) which contain a sub-list for each experimental trial. Each number is the number of spikes for a single cell, an empty sublist means no spikes were detected during the trial


```python

experiment_1_trials =   [[1, 2, 3, 6],
		         [],
		         [],
		         [4, 5, 6, 7, 8, 3, 12, 2],
		         [2],
		         [9, 10, 11, 63],
		         [123, 2, 2],
		         [199, 2, 24, 5, 66],
		         [],
		         [2, 3, 5, 6], 
			 [4]
		        ]

experiment_2_trials =   [[12, 43, 2, 2],
		         [2],
		         [],
		         [],
		         [1, 2, 3, 5]
		        ]
```

    - make one list called all_trials that contains all of experiment_1_trials and experiment_2_trials
   	 - see if you can do this in three different ways
    - calculate the sum of the 2nd and 3rd cells of the 1st and 4th trials
    - if you did this with a loop, do it again by indexing
    - print the number of cells firing in each trial
    - how many of the trials contain the number 2?


Because you, the experimenter, used an outdated form of note taking, consisting of writing things down on tissues instead of a lab book or database you forgot that you actually did a trial in between experiment_1_trials and experiment_2_trials:

```python
new_trial = [1, 3, 5, None, 5, 6, float('NaN')]
```

    - clean the new_trial to remove any non-numeric elements
    - insert new_trial into the main list in between experiment_1_trials and experiment_2_trials
    - ideally do this on the list you have already, don't rebuild the list from the original components
    - something went wrong on your last trial, but you want to keep the data somewhere in case you need it again
    	- obtain and remove it from the list
    	- do the same for the 4th trial
	- do so using a built-in list method

    - find out the number of trials where no cells fired
    - remove any empty trials from your list
    - if you do this with a simple for loop, do you get the result you expect? if not, why not?
    - if you didn't already, try these again using built-in list methods (where applicable)

    - remove all trials that contain less than 3 elements
    - create a list containing the number of spikes of the second cell of each of the remaining trials

    - flatten the list (i.e. remove the nesting, but keep the values) to make one list of all spike counts
    - put the numbers in descending order - with and without changing the original list 


CASTING AND LIST COMPREHENSIONS
===============================

QUESTION 3
----------

    - use `range()` to create a list of numbers 1-100
    - check the type of your result
    - make a list of all numbers up to 100 squared 
    - make a list of all the numbers in the list of squared numbers that are multiples of 9
    - reverse the order of each sublist in the list_of_x_y_coordinates (i.e. [1,2], [3,5] >> [2,1], [5,3])

```python
list_of_x_y_coordinates = [[1, 2], [3, 5], [5, 6], [10, 20]]
```

TUPLE BASICS
============

QUESTION 4
----------

```python
x = 10
y = 10
z = 5
coordinates = x, y, z
```

    - check if the number 5 is in the coordinates tuple
    - try to change the y coordinate to 15
    	- note that you can't do this - tuples are immutable
    	- think about why/when that might be useful
	- think about when it might not be useful
    - if you first cast the tuple into a different type (one that you know is mutable) then you can change the coordinate - try this now

    - in this example, you only care about x and y together, but not z
    - try to use something called tuple unpacking to separate coordinates into the variables loc_2d and z

```python
example_tuple = 'this', 'is', 'quite', 'stringy', {'dictionary': 100, 'stuff': 340, 'here': 23424}
```

    - use the same principle to put all the first 4 string variables into a single variable, and the dictionary in its own variable such that:
```python

variable_1 = 'this', 'is', 'quite', 'stringy'
variable_2 = {'dictionary': 100, 'stuff': 340, 'here': 23424}
```


STRINGS LISTS TUPLES AND DICTIONARIES COMBINED
==============================================

QUESTION 5
----------


    - read the stimulus_starts and stimulus_ends from the stimulus_parameters.txt file
    - put them into a dictionary such that anything to the left of '=' is a key, and anything to the right is a value
    - save your dictionary to a file for later on
    - load your dictionary from earlier
    - loop over and print the following: 
    	- all the keys in the dictionary
    	- all values in the dictionary
	- both

    - get the stimulus starts and ends and put them into the following variables:
    	- do this using the dictionary key
    	- do this in a way that both returns the values, and also removes them from the dictionary (HINT: look at built-in dictionary methods)
    	- make sure that each entry in the list is an integer type, not a string

```python
stimulus_starts =
stimulus_ends =
```

    - loop through the starts and ends simultaneously and print them out

    - if you didn't already, use the built in function zip
    - to understand how this works, cast your zipped lists into a list and print it to the console
    - what happens if the two lists are of different lengths?
    - use zip and print out the start and end of the third stimulus

    - HINT/BONUS (recommended): you could try using a package called configobj for a 1 line solution to the first 4 parts of this question


DICTIONARY COMPREHENSION
========================

QUESTION 6
----------

Imagine a (quite stupid because the keys don't do much) hypothetical dictionary like the one below to store postsynaptic events that contains the name of the event as a key and the time start, time end and amplitude as a tuple.
	
	- Using dictionary comprehension, return a dictionary (of the same not very smart format) that contains only events with
		 - an amplitude > 20
		 - a duration of 1
		 - a duration between 2 and 4

```python
synaptic_events = {
    'e1': (10, 12, 22),
    'e2': (15, 17, 12),
    'e3': (20, 21, 25),
    'e4': (25, 27, 32),
    'e5': (30, 32, 5),
    'e6': (35, 38, 7),
    'e7': (40, 45, 48),
    'e8': (46, 47, 12),
    'e9': (49, 50, 47),
    'e10': (51, 53, 22)
}
```




