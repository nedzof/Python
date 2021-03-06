#!/usr/bin/python3

import crypt


def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('//dictionary.txt', 'r')
    for num, word in enumerate(dictFile.readlines(), start=1):
        print(("[%d] Trying with: " % num) + word)
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
    if (cryptWord == cryptPass):
        print("[+] Found Password: "+ word+ "\n")
        return
    else:
        print("[-] Password not found. \n")
        return


def main():
    passFile = open('/etc/shadow')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password for: " + user)
            testPass(cryptPass)


if __name__ == "__main__":
    main()
