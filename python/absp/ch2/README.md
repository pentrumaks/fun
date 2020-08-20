# Chapter 2: Flow Control

## Questions / Problems

1. Enumerate the values a Boolean variable can have.

2. Which operator is used to compare:
  - two strings for equality
  - two numbers for non-equality
  - if one number is smaller than other
  - if one string comes alphabetically after another
  - if one number is smaller or equal than the other

3. Enumerate Boolean operators

4. What's the result of:
  - True and <any other value>
  - True or <any other value>
  - False and <any other value>
  - False or <any other value>
  - not True
  - not False

5. If `a` and `b` are boolean variables, write the truth table of
   the expression `a and not b`, i.e. complete this table:

    a  |  b  | Result |
   --- | --- | --- |
    True | True | ...| 
    True | False | ...
    False | True | ...
    False | False | ...
    
    How would you describe with your own words when the above expression
    evaluates to True?

6. Write a program that prompts user to enter two boolean
  variables `a` and `b` and prints the result of expression
  `a and not b`. Use this program to validate the Truth table
  from previous problem. Use an `if` statement.
  
7. Same as 6, but do not use an `if` statement.

8. What is the maximum value a variable of type `int` can hold in Python? Also google what's the max value a variable
   type `int` can hold in Java.
   
9. Write a program to prompt user for their age, and then print how many years they have left until 100.

10. What happens if a person over 100 years old enters his age when running program 9.
    Modify program 9 so that if a person over 100 years old enters his age, the program would print
     "you are already X years over 100".

11. Same as 10, but handle the case when somebody enters a fractional age, e.g. for 99.5 the program should print
    "You have 0.5 years until 100".

12. Write a program that would infinitely prompt the user for his name. Which key combination do you use to
   stop the execution of such a program?

13. Modify program 12, if user enters "stop it", the program should terminate.

14. Write a program to print numbers 0 to 9.

15. Write a program to print numbers 1 to 10.

16. Write a program to print numbers 4 to 14.

17. Write a program to compute the sum of first 100 numbers.

18. Write a program that prompts the user for numbers `a` and `b` and computes the sum of numbers `a`, `a+1`, ..., `b`.

19. Modify program from 18, so that an error would be printed if `a >= b`.

20. Write a program to prompt user for a number, if user enters `0` the execution should exit the loop.
    Compute the sum of those numbers.   

21. Same as 20, only compute the product of entered numbers.

22. Same as 20, only compute the min and max of entered numbers.

23. Write a program that prompts for a number. Compute the sum of odd number 1, 3, ... N.

24. Same as 23, only compute teh product of even numbers 2, 4, ..., N.

25. Write a program that prompts for a number. Print `odd` or `even` depending on whether the entered number was odd or
    even.
    
26. Write a program that prints 100, 99, 98, ..., 50.

27. Write a program that prints 100, 90, 80, ..., 50.  

28. Write a program that prompts user for a number N, then generates and prints N random numbers and their sum.

29. Write a program that prompts user for a number N, then generates and prints N random numbers and the value of
    expression   x1 - x2 + x3 - x4, ...

30. Write a program that prompts user for a file name, then opens that file and prints it to the screen.
    When running this program, try experimenting with:
      a. absolute paths:  /etc/hosts   /etc/issue  /proc/cpuinfo
         You can validate the output printed by program by viewing the content of these files from command line - for
         that start a console, and use the `cat` command. E.g. `cat /etc/hosts`
      c. relative paths.
         E.g. if your program's running directory is /home/max/PyCharmProjects, then you'd specify ../../../etc/hosts
         
31. Write a program that has two python files:
    module1.py containing `N=2`
    module2.py needs to import module1 and print `module1.N`                  

Solve practice questions at the end of each chapter. Solutions to those should be in the form of practiceQ.py, e.g.
practice4.py would be the solution to question 4 at the end of chapter 2.          

For each flow chart from chapter 2, write a program that would implement that flow chart. Solutions should be named
flowN.py. E.g. flow21.py - the program implementing flowchart 2.1.

Run some of the programs you wrote using built-in PyCharm
  debugger (set some breakpoints).
