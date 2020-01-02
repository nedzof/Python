import zipfile as zi
import os


def main():
    path = os.path.dirname(__file__) + "/evil.zip"
    zip = zi.ZipFile(path)
    file = open('/home/caruk/PycharmProjects/Python/dictionary.txt')
    for guess in file.readlines():
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


if __name__ == "__main__":
    main()
