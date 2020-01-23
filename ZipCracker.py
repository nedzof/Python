import zipfile as zi
import os
import time
from threading import Thread
import optparse
from pathlib import Path


def extract_file(password, zip_file):
    try:
        zip_file.extractall(pwd=password)
        print("[+] Found password = " + password)
        return True
    except Exception as e:
        print("[-] Found Bad: " + chance)
        return False


def get_cmd_arguments():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='Specify Zip File')
    parser.add_option('-d', dest='dname', type='string', help='specify Dictionary File')
    (options, args) = parser.parse_args()
    if (options.zname is None):
        parser.error("Please specifiy ZipFile to crack!")
    if (options.dname is None):
        options.dname = "dictionary"
    return options


def get_file(zip_name, extension):
    data_folder = Path(os.path.dirname(__file__))
    zip = data_folder / ("%s.%s" % (zip_name, extension))
    return zip


start = time.time()
option = get_cmd_arguments()
zip_file = get_file(option.zname, 'zip')
dic_file = get_file(option.dname, 'txt')

dictionary = open(dic_file)
for guess in dictionary.readlines():
    chance = guess.strip('\n')
    print("[*] Cracking Password for: " + chance)
    try:
        t = Thread(target=extract_file, args=(chance, zip))
        t.start()
    except Exception as e:
        continue
# zip_file.close()
print(time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
