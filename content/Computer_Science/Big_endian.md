# Big endian

Big endian is a way of storing data in a computer's memory. 

* It means the most significant byte (the byte that carries the most weight or importance) is stored first. 
* In other words, the leftmost byte is the most significant byte. 
* This is like reading a book from left to right. 

For example, the number 1234 in big endian is stored as:

```
Byte 1: 00000000 00000000 00000100 11010010
Byte 2: 00000000 00000000 00000000 00001100
```

* The first byte contains the most significant digits (12), while the second byte contains the least significant digits (34). 
* In big endian, the most significant byte is stored first, so the first byte contains the digits 1 and 2. 
* This is different from little endian, where the least significant byte is stored first. 

Big endian is used in some computer architectures, including the Motorola 68000 and Sparc processors. It is also used in network protocols such as TCP/IP.
