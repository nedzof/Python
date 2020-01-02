import zipfile as zi
import os
import time



def main():
    start = time.time()
    path = os.path.dirname(__file__) + "/evil.zip"
    zip = zi.ZipFile(path)
    dictionary = open('/home/caruk/PycharmProjects/Python/dictionary.txt')
    for guess in dictionary.readlines():
        chance = guess.strip('\n')
        password = str.encode(chance)
        print("[*] Cracking Password for: " + chance)
        try:
            zip.extractall(pwd=password)
            print("[+] Found Password: " + chance + "\n")
        except Exception as e:
            print("[-] Found Bad: " + chance + "\n")
            print(e)
            continue
    zip.close()
    end = time.time()
    elapsed = end - start
    vrjeme = time.strftime("%H:%M:%S", time.gmtime(elapsed))
    print(vrjeme)


if __name__ == "__main__":
    main()
