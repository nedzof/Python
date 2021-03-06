import optparse
import os
import sys
import time
from pathlib import Path
from threading import Thread


def extract_file(password, z_file, s_time):
    try:
        z_file.extractall(pwd=password)
        t_t = time.time() - s_time
        print("[+] Took %f seconds to crack the password. %i attempts per second." % (t_t, i / t_t))
        return True
    except Exception as e:
        print("[-]")
        return False


def get_cmd_arguments():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='Specify Zip File')
    parser.add_option('-d', dest='dname', type='string', help='specify Dictionary File')
    (options, args) = parser.parse_args()
    if options.zname is None:
        answer = input("Default to evil.zip? (Y/N):\t").lower()
        if answer.startswith("y"):
            options.zname = "evil"
        else:
            parser.error("Please specifiy ZipFile to crack!")
    if options.dname is None:
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
i = 0
for guess in dictionary.readlines():
    chance = guess.strip('\n')
    print("[*] Cracking Password for: \t" + chance)
    i += 1
    t = Thread(target=extract_file, args=(chance, zip_file, start))
    t.start()
# delta = time.gmtime(time.time() - start)
# print(time.strftime("%H:%M:%S", delta))

sys.exit(1)
