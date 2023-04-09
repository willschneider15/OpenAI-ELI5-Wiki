# CAP Theorem

The CAP theorem is a concept in computer science that states that it is impossible for a distributed computer system to simultaneously provide more than two of the following three guarantees:

1. Consistency: All nodes see the same data at the same time
2. Availability: Every request receives a response about whether it was successful or failed
3. Partition tolerance: The system continues to operate despite arbitrary message loss or failure of part of the system

In other words, you can only have two out of three of these guarantees at the same time. For example, if you want your system to be consistent and available, then it cannot be partition tolerant.
