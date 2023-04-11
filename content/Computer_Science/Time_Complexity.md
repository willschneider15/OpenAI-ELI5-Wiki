# Time Complexity

- **What is it?**

  Time complexity is the measure of how many steps or operations an algorithm takes as the size of the input grows.

- **Why it matters?**
  
  Evaluating the time complexity of an algorithm allows us to compare different algorithms for the same problem and choose the most efficient one which will complete faster.

- **How is it measured?**

  We use a Big O notation to measure time complexity.
  
- **What is Big O notation?**

  Big O notation is a mathematical representation of time complexity. It tells us how an algorithm's execution time increases as the size of the input grows. It describes the worst-case scenario of the algorithm's time complexity.
  
- **How to read Big O notation?**

  Big O notation is written as `O(n)` where `n` is the size of the input. The `O` represents the order of magnitude, and it tells us how fast the algorithm grows. In general, we want `O(n)` or smaller complexity because it means that the algorithm's execution time will increase linearly or slower as the size of the input grows.

- **Examples of Big O notation**:

  - The following are examples of Big O notations arranged in order from smallest to largest:
    - O(1) - constant time complexity
    - O(log n) - logarithmic time complexity
    - O(n) - linear time complexity
    - O(n log n) - linearithmic time complexity
    - O(n^c) - polynomial time complexity
    - O(c^n) - exponential time complexity
