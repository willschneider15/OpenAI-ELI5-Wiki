# Memoization

Memoization is a way to remember something so you don't have to do it again, like how you remember 2+2 is 4. 

In computer science, it's when a program remembers the result of a calculation so it can be used again later without having to do the calculation again.

Here's an example of how memoization works:

- Imagine you have a program that needs to calculate the 10th Fibonacci number (a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1).
- The program starts by calculating the 9th Fibonacci number, which requires calculating the 8th and 7th Fibonacci numbers, and so on.
- As you can imagine, this can take a lot of time and resources if you keep recalculating the same numbers over and over again.
- With memoization, the program remembers the result of each calculation as it goes along, so it only has to calculate each number once.

Overall, memoization is a tool used to increase efficiency by saving previously computed results.
