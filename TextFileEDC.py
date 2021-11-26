# Title:        Caesar Cipher Encryption/Depcryption Machine 
# Authors:      Stephen Shelnutt & Kristian Anderson
# Date:         2/28/21
# Description:  This class has three primary usages. It can intake a file to encrypt the message through the Caesar Shift using the user's cipher key
#               and create a new file with the cipher text, or intake the user's file and the user's cipher key to decrypt it and create a new file
#               with the plaintext, or it can "brute force" a cihper text, meaning it will intake a user's file and display all plaintexts
#               from each and every cipher key. This program must be used through command line arguments.


import sys, getopt, os

    # The encrypt function intakes a requested file and puts all the content in a string.
    # This string is then put into a for loop where all characters are shifted by the 
    # requested shift key amount. The new string is then written into a new file with
    # the requested name by the user.
def encrypt(plaintextfile, key, newfilename):
      #makes sure that the file your are trying to encrypt exists
    try:
        encrypted = ""
    
        file = open(plaintextfile, "r")
        newfile = open(newfilename, "w")

        words = file.read().replace("\n"," ")
        file.close()
        print("Encrypting file %s" % plaintextfile)
        for c in words:
            if c.isupper(): #check if it's an uppercase character
                c.lower()
                c_index = ord(c) - ord('A')
                # shift the current character by key positions
                c_shifted = (c_index + int(key)) % 26 + ord('A')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.islower(): #check if its a lowecase character
                # subtract the unicode of 'a' to get index in [0-25) range
                c_index = ord(c) - ord('a') 
                c_shifted = (c_index + int(key)) % 26 + ord('a')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.isdigit():
                # if it's a number,shift its actual value 
                c_new = (int(c) + int(key)) % 10
                encrypted += str(c_new)
            else:
                # if its neither alphabetical nor a number, just leave it
                encrypted += c

        newfile.write(encrypted)
        newfile.close()
        print("File Encrypted!")
    except FileNotFoundError:
        print("File does not exist")
    except:
        print("Error unknown")
    


    # This function takes in all content from a requested txt document and puts it into a string.
    # The string is then put into a for loop, shifting every character by the requested shift key.
    # Once fully through the for loop, this string is then put into a new file with the name 
    # requested by the user.
def decrypt(ciphertextfile, key, newfilename):
      #makes sure that the file your are trying to decrpyt exists
    try:
        decrypted = ""
        file2 = open(ciphertextfile, "r")
        newfile2 = open(newfilename, "w")
        cipher = file2.read().replace("\n"," ")# pulls the encrypted words into a string to decrypt.
        file2.close()
        print("decrypting file %s" % ciphertextfile)
        for d in cipher:
            if d.isupper():
                d.lower()
                d_index = ord(d) - ord('A')
                # shift the current character to left by key positions to get its original position
                d_og_pos = (d_index - int(key)) % 26 + ord('A')
                d_og = chr(d_og_pos)
                decrypted += d_og
            elif d.islower():
                d_index = ord(d) - ord('a') 
                d_og_pos = (d_index - int(key)) % 26 + ord('a')
                d_og = chr(d_og_pos)
                decrypted += d_og
            elif d.isdigit():
                # if it's a number,shift its actual value 
                d_og = (int(d) - int(key)) % 10
                decrypted += str(d_og)
            else:
                # if its neither alphabetical nor a number, just leave it like that
                decrypted += d
        newfile2.write(decrypted)
        newfile2.close()
        print("File Decrypted!")
    except FileNotFoundError:
        print("File does not exist")
    except:
        print("Error unknown")

    # This function intakes an encrpyted document and puts all the content into a string.
    # The string is then decrypted, similarly to the decrypt function above, and 
    # produces a result for every possible key, 1-26, and each result is then split into
    # a list of strings to compare to a dictionary text document. If all strings are 
    # found (only accepting 100% threshold), the correct result will be displayed. 
def crack(ciphertextfile):
      # makes sure that the file your are trying to crack exists
    try: 
        f = open(ciphertextfile, "r")
        f2 = open('dictionary.txt', 'r')
        dic = f2.read().replace("\n", " ") # pulls all the words in dictionary into a string to compare against the decrypted possible solutions.
        cipher = f.read().replace('\n', ' ')# pulls the encrypted words into a string to decrypt.
        f2.close()
        f.close()
        result = ''
        correct = 0
        y = dic.split()
        trash = ""
        for key in range(1,27):
            decrypted = ''
            for d in cipher:
                if d.isupper():
                    d_index = ord(d) - ord('A')
                    # shift the current character to left by key positions to get its original position
                    d_og_pos = (d_index - int(key)) % 26 + ord('a') #
                    d_og = chr(d_og_pos)
                    decrypted += d_og
                elif d.islower():
                    d_index = ord(d) - ord('a')
                    d_og_pos = (d_index - int(key)) % 26 + ord('a')
                    d_og = chr(d_og_pos)
                    decrypted += d_og
                elif d.isdigit():
                    # if it's a number,shift its actual value
                    d_og = (int(d) - int(key)) % 10
                    decrypted += str(d_og)
                elif d.isspace():
                    decrypted += d
                else:
                    # if its not alphabetical, a number, or a space, moves it to the trash. special
                    # characters must be removed, along with capital letters replaced to lowercase
                    # so when decrypted is .split() and compared to the words in the dictionary, 
                    # it will compare only the alphabetical and numerical characters.
                    trash += d
            x = decrypted.split()
            tokens = 0
            words = len(x)
            # scans each decrypted word against every word in the dictionary.
            # If a decrypted word matches one in the dictionary, a token is 
            # earned. If the number of tokens match the number of words in 
            # the decrypted list, that decryption is correct and will be displayed.
            for line1 in y:
                for line2 in x:
                    if line1 == line2:
                        tokens += 1
                    else:
                        tokens += 0
            if tokens == words:
                result = decrypted
                correct = key
        print("Key value", str(correct),":", result)
    except FileNotFoundError:
        print("File does not exist")
    #except:
     #   print("Error unknown")
    







def main():
    # our main includes that ability to select the options of -e \ -c \ -d to encrypt,decrypt,crack   
    print("")
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:] 
    # Options
    options = "edc:"
    # Long options
    long_options = ["Encrypt", "Decrypt", "Crack"]
    nf = ""
  
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
 
            if currentArgument in ("-e", "--Encrypt"):
                 #Makes sure that you have the right syntax for the program
                if len(sys.argv) < 5:
                    print("Invlaid syntax for encryption try again")
                    sys.exit(1)
                #Makes sure that you type in between the max and min key you can use
                is_between = (int(sys.argv[3]) in range(0,26))
                if(is_between == False):
                    print("Error key is out of range")
                    sys.exit(1)
                #makes sure that the file you are encrypting is a txt file
                try:
                    sys.argv[2].index(".txt")
                except ValueError:
                    nf = "notfound"
                
                if (nf == "notfound"):
                    print("File must be .txt file")
                    sys.exit(1)
                #makes sure that your ouput file is a txt file
                try:
                    sys.argv[4].index(".txt")
                except ValueError:
                    nf = "notfound"
                if (nf == "notfound"):
                    print("File must be .txt file")
                    sys.exit(1)
                print("Encrypting file")
                #handles arguments
                file = sys.argv[2]
                key = sys.argv[3]
                ofile = sys.argv[4]
                
                #print ("Encrypting File (%s)" % (file))
                encrypt(file,key,ofile)
            elif currentArgument in ("-d", "--Decrypt"):
                #Makes sure that you have the right syntax for the program
                if len(sys.argv) < 5:
                    print("Invlaid syntax for encryption try again")
                    sys.exit(1)
                #Makes sure that you type in between the max and min key you can use
                is_between = (int(sys.argv[3]) in range(0,26))
                if(is_between == False):
                    print("Error key is out of range")
                    sys.exit(1)
                #Makes sure that your first file is a txt and can only use txt files to encrypt
                try:
                    sys.argv[2].index(".txt")
                except ValueError:
                    nf = "notfound"
                if (nf == "notfound"):
                    print("File must be .txt file")
                    sys.exit(1)
                #Makes sure that your  outputfile is a txt file
                try:
                    sys.argv[4].index(".txt")
                except ValueError:
                    nf = "notfound"
                if (nf == "notfound"):
                    print("File must be .txt file")
                    sys.exit(1)
                print("Decrpyting file")
                #takes in the arguments
                file = sys.argv[2]
                key = sys.argv[3]
                ofile = sys.argv[4]
                #print ("Decrpyting file (%s)" % (file))
                decrypt(file,key,ofile)
            elif currentArgument in ("-c", "--Crack"):
                #makes sure that you are cracking a txt file
                if len(sys.argv)< 3:
                    print("Invlaid syntax for encryption try again")
                    sys.exit(1)
                
                try:
                    sys.argv[2].index(".txt")
                except ValueError:
                    nf = "notfound"
                
                
                if (nf == "notfound"):
                    print("File must be .txt file")
                    sys.exit(1)
                print("Cracking file")
                file = sys.argv[2]
                #print ("Cracking file  (%s)" % (file))
                crack(file)
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))




if __name__ == "__main__":
    main()
    # runs the code

    
