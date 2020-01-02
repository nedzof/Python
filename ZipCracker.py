import zipfile as zi
import os
import time
from threading import Thread
import optparse


def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='Specify Zip File')
    parser.add_option('-d', dest='dname', type='string', help='specify Dictionary File')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    start = time.time()
    path = os.path.dirname(__file__) + ("/%s.zip" % zname)
    zip = zi.ZipFile(path)
    dictionary = open('/home/caruk/PycharmProjects/Python/{}.txt'.format(dname))
    for guess in dictionary.readlines():
        chance = guess.strip('\n')
        print("[*] Cracking Password for: " + chance)
        try:
            t = Thread(target=extractFile, args=(chance, zip))
            t.start()
        except Exception as e:
            print("[-] Found Bad: " + chance + "\n")
            print(e)
            continue
    zip.close()
    print(time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))


def extractFile(chance, zip):
    password = str.encode(chance)
    zip.extractall(pwd=password)
    print("[+] Found Password: " + chance + "\n")


if __name__ == "__main__":
    main()
