# Digital Signatures

A digital signature is a way to show that a digital document is authentic or real. It's like when you write your name on a piece of paper to show that you wrote it. But instead of writing your name, you create a special code that represents your signature that only you can produce. Here's how it works:

* First, a special formula is used on the digital document to create a one-of-a-kind code called a "hash".
* Next, this hash code is encrypted using a private key that only the author of the document has access to.
* Finally, the encrypted hash is attached to the digital document, creating a digital signature.

This digital signature can be checked by anyone who has the author's public key. When they check the digital signature, they can be sure that:

* the document really came from the author
* the document was not altered after it was signed.
