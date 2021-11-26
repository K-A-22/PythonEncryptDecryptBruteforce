Read Me
This class has three primary usages. It can intake a file to encrypt the message through the Caesar Shift using the user's cipher key and create a new file with the cipher text, or intake the user's file and the user's cipher key to decrypt it and create a new file with the plaintext, or it can "brute force" a cihper text, meaning it will intake a user's file and display all plaintexts from each and every cipher key. This program must be used through command line arguments.

How to run program

Encrypt text file
python3.8 TextFileEDC.py -e {textfile name} {shift amount} {new textfile name}

Decrypt text file
python3.8 TextFileEDC.py -d {textfile name} {shift amount} {new textfile name}

Crack text file
python3.8 TextFileEDC.py -c {textfile name}
