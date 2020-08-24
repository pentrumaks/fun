# Chapter 3. Functions

A good analogy to function is what you know from math.

E.g. in math you could have the square function:

    y = x * x

which can also be written as:

    f(x) = x * x

To define this function using Python syntax, you'd have to add `def` and `return`:

    def f(x):
      return x * x

`x` is called the function parameter. And you pass `arguments` as values when evaluating a function, e.g.:

    y = f(2)
    print(f"Square of 2 is {y}")

Or, you could do:

    x = 2
    y = f(x)
    print(f"Square of {x} is {y}")

Note that your entire Python program actually translates to a function. In other languages, like C, you have to explicitely write your program as a function:

    void main() {
        ....
    }


## Exception Handling

Example:

    try:
        ...
    except ZeroDivisionError:
        ...

*IMPORTANT*: keyboard interrupt won't work when running the program from PyCharm -  you'll have to run it from command line, e.g. `python3 indents.py` (assuming the file was named indents.py).

    try:
        ...
    except KeyboardInterrupt:
        ...

        

# Homework

1. Write a program that infinitely prompts the user for two numbers a and b and then prints
   a / b. The program must handle properly zero division errors.
   In order to quit the program, the user should press Ctrl+C

2. Modify solution to program 1: extract the code that computes and prints a/b to a function named
   divide(x, y) - this function would compute x/y, print the output and handle zero division errors.

3. Modify solution to program 2: move `divide(x, y)` to a different module named my_functions.py, import
   that module and use the function.

4. Write a program that prompts the user for a file name, then prints the content of the specified file.
   This program must handle the case when the file does not exist. To find out which error you need to
   catch google for "python file not found exception".

5. Write a function that accepts parameters `a`, `b` and `x` and returns the result of `a*x+b`.

6. Write a function that accepts parameters `a` and `b` and returns the solution to equation `a*x+b`. After the program prints the solution, also print the result of `a*x+b` using the function from problem 5.

7. Write a function that accepts parameters `a`, `b`, `c` and `x` and returns the result of `a*x^2+b*x+c`.

