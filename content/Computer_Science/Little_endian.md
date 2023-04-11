# Little endian

Little endian and big endian are two ways of storing multi-byte data types in the memory of a computer. In little endian, the smaller value bytes are stored at the lower addresses while the bigger ones are stored at higher addresses.

* Imagine you have a row of five blocks, and you want to store the number 12345.
* First, you put the digit 5 in the first block, because it's the smallest digit.
* Then you put the digit 4 in the second block, because it's the next smallest.
* And you keep going until all the digits are in the blocks.
* In little endian, the least significant byte (the 5 in our example) is stored at the first block, which has the smallest address.

This way of organizing bytes can be very useful because it allows for efficient manipulation of multi-byte data types. However, it can also be confusing when different systems (or programs) use different conventions, as it can cause problems with data compatibility.
