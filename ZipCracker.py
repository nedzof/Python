import zipfile as zi
import os

def main():
    path = os.path.dirname(__file__) + "/evil.zip"
    zip = zi.ZipFile(path)
    password = str.encode("1234")
    zip.extractall(pwd=password)
    zip.close()

if __name__ == "__main__":
    main()
