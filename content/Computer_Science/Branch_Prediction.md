# Branch Prediction

**Branch Prediction** is like guessing what will happen next in a choose your own adventure story. When we write code, sometimes our program needs to make a decision on what to do next. It is like a fork in the road - we can go left or right. We don't want to waste time going down one path only to find out later it was the wrong choice. So, we try to guess which path the program will take before it actually happens.

Here's how it works:
- The computer will keep track of which choice the program took last time it reached the fork in the road.
- Based on this history, the computer will make an educated guess on which path the program will take next time.
- By predicting the choice, the computer can start working on that code path before it is actually needed, saving valuable time.

Branch Prediction is like a game of 20 questions, but instead of guessing an object, we are guessing which way the program will go. The better our guesses, the faster our program will run.
