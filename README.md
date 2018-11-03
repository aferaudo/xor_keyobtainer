# Xor Key Obtainer
This is a python script that return the key of a xor cipher.

It takes two parameters in input:
- plain text;
- hide text.
In this way the script can obtain the key without repetition.

N.B. If you want reuse the key, you have to extend the length of the key. For example in python:
key_repeated = previous_key * length
