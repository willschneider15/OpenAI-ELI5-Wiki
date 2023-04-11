# Call Stack

**Call Stack**

A call stack is an essential component of the computer programs that tracks the execution of multiple functions or methods. It is a data structure management mechanism that follows the Last In First Out (LIFO) principle. Imagine that you are taking a nap: you place a pillow (function) as a base, and begin building a stack with more pillows (functions) on top of it. The next pillow (function) is placed over the previous pillow (function), and when you wake up (terminate the function) you remove the latest pillow (function) and continue working on the previous one underneath.

More accurately, here are the steps involved in a call stack:

- Each time a function is called, it is added to the call stack.
- The most recently added function is on the top of the stack.
- When a function is finished, it is removed from the top of the stack (similar to removing the pillow from the top of the stack).
- This process keeps repeating until the program has finished execution. 

The call stack is very helpful when it comes to debugging as it can help you identify exactly where an error occurred in a program.
