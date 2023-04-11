# CAP Theorem

**CAP Theorem**
* Imagine a pizza party where a group of kids have to decide between three things: getting a big pizza they can all share, getting the pizza quickly, or getting a pizza that tastes good.
* In computer science, we have a similar problem when designing certain systems. The three things we have to decide between are: consistency, availability, and partition tolerance.
* Consistency means that everyone sees the same version of the data at the same time.
* Availability means that everyone can access the system at all times.
* Partition tolerance means that the system keeps working even if parts of it stop communicating with each other. This can happen, for example, if one server crashes or the network goes down.
* According to the CAP theorem, a distributed system can only have two out of the three: consistency, availability, and partition tolerance.
* This means that if we prioritize consistency and partition tolerance, the system may become unavailable at times. If we prioritize availability and partition tolerance, we may sacrifice consistency. And if we prioritize consistency and availability, the system may not be partition tolerant.
* So when designing a system, we need to decide which two characteristics are most important based on the needs of the users and the system's specific requirements.
