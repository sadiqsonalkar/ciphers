import random
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ''.join(random.sample(alpha,len(alpha)))#generates a random shuffle of alphabets
def encrypt(encrypt_msg):
        final_ans = ""
        for char in encrypt_msg:#iterates over every character in text to be encrypted
                num = alpha.find(char)#num = index of character
                final_ans = final_ans + key[num]#append new char from random shuffle of alphabets
        print(final_ans)
def decrypt(decrypt_msg):
        final_ans = ""
        for char in decrypt_msg:#iterates over every character in text to be encrypted
                num = key.find(char)#num = index of character
                final_ans = final_ans + alpha[num]#append new char from alphabets
        print(final_ans)
while True:#Menu driven While loop; goes on untill EXIT option is not selected or program is not killed
        n = int(input("Enter value:: \n1) To Encrypt Text:: \n2) To Decrypt Text:: \n3) See Key:: \n4) To Exit \n"))
        if (n == 1):
             encrypt_msg = str(input("Enter Text:: "))
             encrypt(encrypt_msg.upper())
        elif (n == 2):
             decrypt_msg = str(input("Enter Crypt Text:: "))
             decrypt(decrypt_msg.upper())
        elif (n==3):
                print(key)
        elif (n==4):
                break
        else:
                print("Invalid Input; Enter  Again!!")
