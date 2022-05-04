# Pyton-Projects

### VUT University : ISJ_2022

# Description

Some projects included only code completion, others - a completely written program. The tasks of the projects can be found below.

## Project 1

1. First function **camel_to_snake_case**: add a definition for the regular expression to match the positions to be inserted in the camelCaseName names _ when converting to snake_case_name.
2. Second function **not_both_titles**: write the definition of a regular pat to match either the name preceded by the title [Pp]rof. or [Dd]oc. and is followed by ", Ph.D.", or another case.

## Project 2

1. First function **she_says_he_says**: replaces y/i, removes spaces, returns reversed.
2. Second function **solfege**: partitions the input string to (an optional) title, ': ', and the hymn, takes a sublist starting from the first string, skipping always two other strings, and ending 3 strings from the end, returns the result as a string with ', ' as a separator.

## Project 3

1. First function **first_odd_or_even**: returns 0 if there is the same number of even numbers and odd numbers in the input list of ints, or there are only odd or only even numbers.<br />
   Returns the first odd number in the input list if the list has more even numbers.<br />
   Returns the first even number in the input list if the list has more odd numbers.
2. Second function **to_pilot_alpha**: returns a list of pilot alpha codes corresponding to the input word.

## Project 4

1. First function **all_permutations_substrings**: generates all permutations of all substrings of the input string and returns a set of input words that match one of the permutations.
2. Second function **match_permutations_substrings**: returns the input sequence unified and sorted (according to the values).
3. Third function **uniq_srt**: returns the input sequence, items ordered by the order of their first appearance.

## Project 5

Define the **gen_quiz** function that can be called with 4 parameters:<br />
**qpool** - list of question pairs and list of answers<br />
any number of indexes in the qpool list<br />
**altcodes** - a sequence through which the for construct can be passed and which returns the strings to be preceded (along with ':') before each of the answers<br />
**quiz** - an input form of quiz in the form of a list of question pairs and a list of formatted answers.<br />

If any of the indexes in the qpool list is out of range, or another error occurs while processing a specific index, it should print:<br />
**Ignoring index \<number\> - \<exception text\>**<br />
(somewhat pointless to standard output, not to standard error output to make doctest work)

If the sequence of altcodes is shorter than the list of possible answers in one of the lists, only the given number will be added to the final quiz (the zip construction (altcodes, answers) can be used). By default, the answers are marked with letters and there are a maximum of 6 possible answers, ie altcodes = 'ABCDEF')

If the input form of the quiz is not specified, a new quiz will be created with items according to the defined indexes. The default value is therefore an empty quiz.
  
### Tests:

````
    >>> test_qpool1 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> existing_quiz1 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
    >>> gen_quiz(test_qpool1, -2, 0, altcodes = ('10', '20', '30'), quiz = existing_quiz1)
    [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2']), ('Question3', ['10: Answer1', '20: Answer2', '30: Answer3']), ('Question1', ['10: Answer1', '20: Answer2', '30: Answer3'])]

    >>> test_qpool2 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> existing_quiz2 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
    >>> not_used = gen_quiz(test_qpool2, -2, 0, altcodes = ('1', '2', '3'), quiz = existing_quiz2)
    >>> existing_quiz2
    [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2']), ('Question3', ['1: Answer1', '2: Answer2', '3: Answer3']), ('Question1', ['1: Answer1', '2: Answer2', '3: Answer3'])]

    >>> test_qpool3 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> existing_quiz3 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
    >>> not_used1 = gen_quiz(test_qpool3, 0, 2, altcodes = ('i', 'ii', 'iii'), quiz = existing_quiz3)
    >>> not_used2 = gen_quiz(test_qpool3, 1, altcodes = ('i', 'ii', 'iii'), quiz = existing_quiz3)
    >>> existing_quiz3
    [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2']), ('Question1', ['i: Answer1', 'ii: Answer2', 'iii: Answer3']), ('Question3', ['i: Answer1', 'ii: Answer2', 'iii: Answer3']), ('Question2', ['i: Answer1', 'ii: Answer2', 'iii: Answer3'])]

    >>> test_qpool4 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> gen_quiz(test_qpool4, 0, 1, -1)
    [('Question1', ['A: Answer1', 'B: Answer2', 'C: Answer3', 'D: Answer4']), ('Question2', ['A: Answer1', 'B: Answer2', 'C: Answer3']), ('Question4', ['A: Answer1', 'B: Answer2'])]

    >>> test_qpool5 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> not_used = gen_quiz(test_qpool5, 0, altcodes = '123456')
    >>> gen_quiz(test_qpool5, 0, altcodes = '123456')
    [('Question1', ['1: Answer1', '2: Answer2', '3: Answer3', '4: Answer4'])]
    
    >>> test_qpool6 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> existing_quiz6 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
    >>> gen_quiz(test_qpool6, quiz = existing_quiz6)
    [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]

    >>> test_qpool7 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> gen_quiz(test_qpool7, 0, 4, 2, altcodes = ['101','201']) 
    Ignoring index 4 - list index out of range
    [('Question1', ['101: Answer1', '201: Answer2']), ('Question3', ['101: Answer1', '201: Answer2'])]

````

## Project 6

Implement a Polynomial class that will work with polynomials represented by lists. For example, 2x ^ 3 - 3x + 1 will be represented as [1, -3,0,2] (the list starts with the lowest order, although polynomials are usually written in reverse).

It will be possible to instantiate a class in several different ways:<br />
**pol1 = Polynomial ([1, -3,0,2])**<br />
**pol2 = Polynomial (1, -3,0,2)**<br />
**pol3 = Polynomial (x0 = 1, x3 = 2, x1 = -3)**<br />

Calling the print () function prints the polynomial in the usual format:<br />
**\>\>\> print (pol2)**<br />
**2x ^ 3 - 3x + 1**

It will be possible to compare vectors to compare:<br />
**\>\>\> pol1 == pol2**<br />
**True**<br />

It will be possible to add and exponentiate polynomials with non-negative integers:<br />
**\>\>\> print (Polynomial (1, -3,0,2) + Polynomial (0, 2, 1))**<br />
**2x ^ 3 + x ^ 2 - x + 1**<br />
**\>\>\> print (Polynomial (-1, 1) ** 2)**<br />
**x ^ 2 - 2x + 1**

And the methods derivative () - derivative and at_value () - the value of the polynomial for the given x will work - both only return the result, it does not change the polynomial itself:<br />
**\>\>\> print (pol1.derivative ())**<br />
**6x ^ 2 - 3**<br />
**\>\>\> print (pol1.at_value (2))**<br />
**11**<br />
**\>\>\> print (pol1.at_value (2,3))**<br />
**35**<br />
(if 2 values are entered, the result is the difference between the value of at_value () of the second and first parameter - it can be used to calculate a certain integral, but it should not be implemented)

### Tests:

````
def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
````

## Project 7

Implement the function (decorator factory) **log_and_count**, which allows the use of a decorator specifying the key (key in the Counter structure) under which the call to the function is to be counted, or uses the following function name as the key. The second parameter that will need to be specified with the counts key name will be the name of the Counter structure in which the count is to be stored.

### Tests:

#### INPUT
````
import collections

my_counter = collections.Counter()

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)

print(my_counter)
````
#### OUTPUT
````
called f1 with (2,) and {}
called f2 with (2,) and {'b': 4}
called f1 with () and {'a': 2, 'b': 4}
called f2 with (4,) and {}
called f2 with (5,) and {}
called f3 with (5,) and {}
called f3 with (5, 4) and {}

Counter({'basic functions': 5, 'f3': 2})
````
