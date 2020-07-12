# Chapter 0 - Introduction

You'll encounter some unknown words and concepts, don't worry and move on.

From this chapter let's skip:
- *Downloading and installing Python* - you already have it installed
- *Downloading and installing Mu* - you have a better IDE - PyCharm
- *The Interactive Shell* - you have interactive shell in PyCharm. To start the interactive shell (a.k.a. REPL) in PyCharm: Tools -> Python or Debug Console.
- *Installing Third-Party Modules* - skip this, we'll cover that later.

The book mentions a couple of websites that allow sharing code. Let's use <https://gist.github.com/>.

Don't go thru all the links the authoer provides to <https://reddit.com> etc - just skim thru the chapter and move on to more interesting stuff (Chapter 1).

## Problems

### Problem 1
Try to write yourself the slightly altered password program shown in Chapter 0 that would:
1. Open a file containing a password
2. Prompt the user for a password
3. Compare the password from the file with the one entered by the user
4. If passwords don't match, print "Access Denied"
5. Else print "Access Granted" and compare the password to "123", "1234" and "12345" -
   if any of these match then print "That's quite a silly password"
 
 ### Problem 2
 Same as problem 1, but don't hardcode the file name. First prompt the user for the password file name, then open that file and proceed same as in Problem 1.
