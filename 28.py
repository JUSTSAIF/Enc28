###########################
#  Coded By SAIF => Mr28  #
#        2020-5-14        #
###########################
from colored import fg, bg, attr
from bs4 import BeautifulSoup
import urllib.parse
import urllib
import hashlib
import requests
import random
import string
import base64
import os
import codecs
from Crypto import Random
from Crypto.Cipher import AES
import os.path
from os import listdir
from os.path import isfile, join
import time
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

print('%s =============================================================%s' % (fg(25), attr(0)))
print('%s = 8888888888                 .d8888b.  .d8888b.             =%s' % (fg(25), attr(0)))
print('%s = 888                       d88P  Y88bd88P  Y88b            =%s' % (fg(25), attr(0)))
print('%s = 888                              888Y88b. d88P d888b  d88 =%s' % (fg(25), attr(0)))
print('%s = 8888888   88888b.  .d8888b     .d88P "Y88888" d888888888P =%s' % (fg(25), attr(0)))
print('%s = 888       888 "88bd88P"    .od888P" .d8P""Y8b.88P  Y888P  =%s' % (fg(25), attr(0)))
print('%s = 888       888  888888     d88P"     888    888            =%s' % (fg(25), attr(0)))
print('%s = 888       888  888Y88b.   888"      Y88b  d88P            =%s' % (fg(25), attr(0)))
print('%s = 8888888888888  888 "Y8888P888888888  "Y8888P"             =%s' % (fg(25), attr(0)))
print('%s =                || instagram.com/qq_iq ||                  =%s' % (fg(1), attr(0)))
print('%s =============================================================%s' % (fg(25), attr(0)))
print()
print("%s 1 - Encrypt & Decrypt => Files .%s" % (fg(62), attr(0)))
print("%s 2 - Encrypt & Hashing & Decrypt => Text  .%s" % (fg(62), attr(0)))
print("%s 3 - Contact Me :) .%s" % (fg(52), attr(0)))
print("%s 0 - Exit .%s" % (fg(62), attr(0)))

print()
AnswerQ = input("%s Enter Option : %s" % (fg(5), attr(0)))
if AnswerQ == "1":
# def Files():
    print()
    print("%s 1 - Encrypt .%s" % (fg(62), attr(0)))
    print("%s 2 - Decrypt .%s" % (fg(62), attr(0)))
    print("%s 0 - Exit    .%s" % (fg(62), attr(0)))
    print()
    Answer = input("%s Enter (1 or 2?) : %s" % (fg(5), attr(0)))

    if Answer == "1":

        def randomString(stringLength=8):
            letters = "123456789028FUCKS"
            return ''.join(random.choice(letters) for i in range(stringLength))

        # File Input
        G_File = input("%sEnter File Path : %s" % (fg(2), attr(0)))
        C_File = os.path.exists(G_File)
        C2_File = os.path.isfile(G_File)
        if C_File == True or C2_File == True:
            #  Open File ==>
            f = open(G_File, 'rb')
            File = f.read()
            f.close()
            # key = input("%sEnter Passwd : %s" % (fg(2), attr(0)))
            key = random.randrange(1, 256, 1)
            with open("key.txt", 'w') as fkey:
                Gkey = str(key)
                fkey.write(str(base64.b64encode(Gkey.encode("utf-8")), "utf-8"))
                fkey.close

            File = bytearray(File)
            for index, value in enumerate(File):
                File[index] = value^key

            Get_ext = os.path.splitext(G_File)
            Name_Fsaved = Get_ext[0] + "_EncryptedByMr28_" + randomString(4) + Get_ext[1]
            f = open(Name_Fsaved , 'wb')
            f.write(File)
            f.close
        else:
            print("%s Error:: Path is Not Exists ! %s" % (fg(1), attr(0)))
    # ================ 2 =================
    elif Answer == "2":

        def randomString(stringLength=8):
            letters = "1234567890fucks"
            return ''.join(random.choice(letters) for i in range(stringLength))

        # File Input
        G_File = input("%sEnter File Path : %s" % (fg(2), attr(0)))
        C_File = os.path.exists(G_File)
        C2_File = os.path.isfile(G_File)
        if C_File == True or C2_File == True:
            #  Open File ==>
            f = open(G_File, 'rb')
            File = f.read()
            f.close()
            key = input("%sEnter Key : %s" % (fg(2), attr(0)))
            try:
                key = int(base64.b64decode(key))
                File = bytearray(File)
                for index, value in enumerate(File):
                    File[index] = value^key
                Get_ext = os.path.splitext(G_File)
                Name_FsavedD = Get_ext[0] + "_DecryptedByMr28_" + randomString(4) + Get_ext[1]
                f = open(Name_FsavedD , 'wb')
                f.write(File)
                f.close
            except:
                print("%s Error:: Check Your Key ! %s" % (fg(1), attr(0)))
        else:
            print("%s Error:: Path is Not Exists ! %s" % (fg(1), attr(0)))
    elif Answer == "0":
        exit()
    elif Answer != "1" or Answer != "2":
        print("%sPlease Enter a Number .. !!%s" % (fg(1), attr(0)))
        exit()
    else:
        print("ERRRRRRRRROR !!!!!!")
elif AnswerQ == "2":
    print()
    print("%s 1 - Base64 .%s" % (fg(62), attr(0)))
    print("%s 2 - MD5    .%s" % (fg(62), attr(0)))
    print("%s 3 - ROT13  .%s" % (fg(62), attr(0)))
    print("%s 4 - binary .%s" % (fg(62), attr(0)))
    print("%s 5 - SHA256 .%s" % (fg(62), attr(0)))
    print("%s 6 - AES Encrypt Any File   .%s" % (fg(62), attr(0)))
    print("%s 7 - Generate RSA Private Key and Public Key    .%s" % (fg(62), attr(0)))
    print("%s 8 - URL    .%s" % (fg(62), attr(0)))
    print("%s 0 - Exit    .%s" % (fg(62), attr(0)))
    print()
    AnswerT = input("%s Enter Option : %s" % (fg(5), attr(0)))
    
    if AnswerT == "1":
        print("%s 1 - Encrypt .%s" % (fg(62), attr(0)))
        print("%s 2 - Decrypt .%s" % (fg(62), attr(0)))
        AnswerO = input("%s Enter Option : %s" % (fg(5), attr(0)))
        if AnswerO == "1":
            print()
            Base64 = str(input("%s Type : %s" % (fg(5), attr(0))))
            print("=================================================")
            RESULT = base64.b64encode(Base64.encode("utf-8"))
            print(RESULT.decode("utf-8"))
            print("=================================================")
        elif AnswerO == "2":
            print()
            Base64 = str(input("%s Type Base46 : %s" % (fg(5), attr(0))))
            print("=================================================")
            RESULT = base64.b64decode(Base64)
            print(RESULT.decode("utf-8"))
            print("=================================================")
        else:
            print("ERRRRRRRRROR !!!!!!")

    elif AnswerT == "2":
        print("%s 1 - Encrypt .%s" % (fg(62), attr(0)))
        print("%s 2 - Try To Crack Hash .%s" % (fg(62), attr(0)))
        AnswerO = input("%s Enter Option : %s" % (fg(5), attr(0)))
        if AnswerO == "1":
            print()
            MD5 = str(input("%s Type : %s" % (fg(5), attr(0))))
            print(" =================================================")
            hash_obj = hashlib.md5(MD5.encode())
            print(' ||       ' + hash_obj.hexdigest() + '      ||')
            print(" =================================================")
        elif AnswerO == "2":
            print()
            print("%s You Must Be Connected To Internet, are you Connected ? \n Enter Any Button if U Connected , Type 0 to exit. %s" % (fg(3), attr(0)))
            ckeck_2 = input(" ")
            if ckeck_2 == "0":
                exit()
            MD5 = str(input(" Type MD5 HASH  : "))
            RESULT = "https://md5decrypt.net/Api/api.php?hash=" + MD5 + "&hash_type=md5&email=deanna_abshire@proxymail.eu&code=1152464b80a61728"
            GetRes = requests.post(RESULT).text
            if GetRes == "CODE ERREUR : 005":
                print("%s Not Found in DataBase !! :( %s" % (fg(1), attr(0)))
            else:
                import urllib.request as ur
                s = ur.urlopen(RESULT)
                sl = s.read()
                print("%s =================================================%s" % (fg(5), attr(0)))
                print()
                print("%s || Found ::%s " % (fg(2), attr(0)) + sl.decode("utf-8"))
                print("%s =================================================%s" % (fg(5), attr(0)))
        else:
            print("ERRRRRRRRROR !!!!!!")
    elif AnswerT == "3":
        print("%s 1 - Encrypt .%s" % (fg(62), attr(0)))
        print("%s 2 - Decrypt .%s" % (fg(62), attr(0)))
        AnswerO = input("%s Enter Option : %s" % (fg(5), attr(0)))
        if AnswerO == "1":
            ROT13 = str(input("%s Type : %s" % (fg(5), attr(0))))
            ROT13 = codecs.encode(ROT13, 'rot_13')
            print("%s =================================================%s" % (fg(5), attr(0)))
            print(" %s(%s    "% (fg(2), attr(0)) + ROT13 + "    %s)%s"% (fg(2), attr(0)))
            print("%s =================================================%s" % (fg(5), attr(0)))
        elif AnswerO == "2":
            ROT13 = str(input("%s Type ROT13 HASH: %s" % (fg(5), attr(0))))
            ROT13 = codecs.encode(ROT13, 'rot_13')
            print("%s =================================================%s" % (fg(5), attr(0)))
            print(" %s(%s    "% (fg(2), attr(0)) + ROT13 + "    %s)%s"% (fg(2), attr(0)))
            print("%s =================================================%s" % (fg(5), attr(0)))
        else:
            print("ERRRRRRRRROR !!!!!!")
    elif AnswerT == "4":

        print()
        print("%s You Must Be Connected To Internet, are you Connected ? \n Enter Any Button if U Connected , Type 0 to exit. %s" % (fg(3), attr(0)))
        ckeck_i = input(" ")
        if ckeck_i == "0":
            exit()
        print()
        print("%s 1 - Encode .%s" % (fg(62), attr(0)))
        print("%s 2 - Decode .%s" % (fg(62), attr(0)))
        print("%s 0 - Exit .%s" % (fg(62), attr(0)))
        print()
        AnswerB = input("%s Enter Option : %s" % (fg(5), attr(0)))
        if AnswerB == "1":
            binary_dec = str(input("%s Type : %s" % (fg(5), attr(0))))
            try:
                ######
                url = 'https://roubaixinteractive.com/PlayGround/Binary_Conversion/Binary_To_Text.asp'
                ToBinary = {'ToBinary': binary_dec}
                x = requests.post(url, data = ToBinary)
                x = x.text
                bs = BeautifulSoup(x, 'lxml')
                ToBinary = bs.find('textarea', attrs={'name': 'ToText'}).text
                ######
                print("%s ========================= %s"% (fg(81), attr(0)) + "%s TEXT To Binary %s"% (fg(1), attr(0)) + "%s ========================= %s" % (fg(81), attr(0)))
                print(" " + ToBinary)
                print("%s =============================== End ================================%s" % (fg(81), attr(0)))
            except:
                print("%s Error !! %s" % (fg(1), attr(0)))
                exit()
        elif AnswerB == "2":
            binary_enc = str(input("%s Type Binary Code : %s" % (fg(5), attr(0))))
            try:
                ######
                url = 'https://roubaixinteractive.com/PlayGround/Binary_Conversion/Binary_To_Text.asp'
                ToText = {'ToText': binary_enc}
                x = requests.post(url, data = ToText)
                x = x.text
                bs = BeautifulSoup(x, 'lxml')
                ToTEXT = bs.find('textarea', attrs={'name': 'ToBinary'}).text
                ######
                print("%s ========================= %s"% (fg(81), attr(0)) + "%s TEXT To Binary %s"% (fg(1), attr(0)) + "%s ========================= %s" % (fg(81), attr(0)))
                print(" " + ToTEXT)
                print("%s =============================== End ================================%s" % (fg(81), attr(0)))
            except:
                print("%s Please Enter a Real 'Binary Code' !! %s" % (fg(1), attr(0)))
                exit()
        elif AnswerB == "0":
            exit()
        else:
            print("ERRRRRRRRROR !!!!!!")

    elif AnswerT == "5":
        print("%s 1 - Encrypt .%s" % (fg(62), attr(0)))
        print("%s 2 - Decrypt .%s" % (fg(62), attr(0)))
        AnswerO = input("%s Enter Option : %s" % (fg(5), attr(0)))
        if AnswerO == "1":
            SHA256 = str(input("%s Type : %s" % (fg(5), attr(0))))
            SHA256 = hashlib.sha256(SHA256.encode('utf-8')).hexdigest()

            print("%s =================================================%s" % (fg(5), attr(0)))
            print(" || Result : ",  SHA256) 
            print("%s =================================================%s" % (fg(5), attr(0)))
        elif AnswerO == "2":
            print("%s You Must Be Connected To Internet, are you Connected ? \n Enter Any Button if U Connected , Type 0 to exit. %s" % (fg(3), attr(0)))
            ckeck_i = input(" ")
            if ckeck_i == "0":
                exit()
            print()
            SHA256 = str(input(" Type SHA256 HASH  : "))
            RESULT = "https://md5decrypt.net/Api/api.php?hash=" + SHA256 + "&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728"
            GetRes = requests.post(RESULT).text
            if GetRes == "CODE ERREUR : 005":
                print("%s Not Found in DataBase !! :( %s" % (fg(1), attr(0)))
            else:
                import urllib.request as ur
                s = ur.urlopen(RESULT)
                sl = s.read()
                print("%s =================================================%s" % (fg(5), attr(0)))
                print()
                print("%s || Found ::%s " % (fg(2), attr(0)) + sl.decode("utf-8"))
                print("%s =================================================%s" % (fg(5), attr(0)))
        else:
            print("ERRRRRRRRROR !!!!!!")
    elif AnswerT == "6":

        # =========================================
        class Encryptor:
            def __init__(self, key):
                self.key = key
            def pad(self, s):
                return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
            def encrypt(self, message, key, key_size=256):
                message = self.pad(message)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv)
                return iv + cipher.encrypt(message)
            def encrypt_file(self, file_name):
                with open(file_name, 'rb') as fo:
                    plaintext = fo.read()
                enc = self.encrypt(plaintext, self.key)
                with open(file_name + ".Mr28", 'wb') as fo:
                    fo.write(enc)
                os.remove(file_name)
            def decrypt(self, ciphertext, key):
                iv = ciphertext[:AES.block_size]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                plaintext = cipher.decrypt(ciphertext[AES.block_size:])
                return plaintext.rstrip(b"\0")
            def decrypt_file(self, file_name):
                with open(file_name, 'rb') as fo:
                    ciphertext = fo.read()
                dec = self.decrypt(ciphertext, self.key)
                with open(file_name[:-4], 'wb') as fo:
                    fo.write(dec)
                os.remove(file_name)
            def getAllFiles(self):
                dir_path = os.path.dirname(os.path.realpath(__file__))
                dirs = []
                for dirName, subdirList, fileList in os.walk(dir_path):
                    for fname in fileList:
                        if (fname != 'script.py' and fname != 'data.txt.Mr28'):
                            dirs.append(dirName + "\\" + fname)
                return dirs
            def encrypt_all_files(self):
                dirs = self.getAllFiles()
                for file_name in dirs:
                    self.encrypt_file(file_name)
            def decrypt_all_files(self):
                dirs = self.getAllFiles()
                for file_name in dirs:
                    self.decrypt_file(file_name)
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        enc = Encryptor(key)
        clear = lambda: os.system('cls')
        if os.path.isfile('data.txt.Mr28'):
            while True:
                password = str(input(" %sEnter password:  %s" % (fg(5), attr(0))))
                enc.decrypt_file("data.txt.Mr28")
                p = ''
                with open("data.txt", "r") as f:
                    p = f.readlines()
                if p[0] == password:
                    enc.encrypt_file("data.txt")
                    break
            while True:
                clear()
                print()
                print("%s 1. Press '1' to encrypt file.\n 2. Press '2' to decrypt file.\n 3. Press '3' to Encrypt all files in the directory.\n 4. Press '4' to decrypt all files in the directory.\n 5. Press '5' to exit.\n %s" % (fg(62), attr(0)))
                choice = int(input(" %sEnter Option : %s"% (fg(62), attr(0))))
                clear()
                if choice == 1:
                    enc.encrypt_file(str(input(" %sEnter name of file to encrypt: %s" % (fg(5), attr(0)))))
                elif choice == 2:
                    enc.decrypt_file(str(input(" %sEnter name of file to decrypt: %s" % (fg(5), attr(0)))))
                elif choice == 3:
                    enc.encrypt_all_files()
                elif choice == 4:
                    enc.decrypt_all_files()
                elif choice == 5:
                    exit()
                else:
                    print("%s Please select a valid option! %s" % (fg(1), attr(0)))
        else:
            while True:
                clear()
                password = str(input(" %sEnter a password that will be used for decryption: %s" % (fg(5), attr(0))))
                repassword = str(input(" %sConfirm password: %s" % (fg(5), attr(0))))
                if password == repassword:
                    break
                else:
                    print(" %sPasswords Mismatched!%s"% (fg(1), attr(0)))
            f = open("data.txt", "w+")
            f.write(password)
            f.close()
            enc.encrypt_file("data.txt")
            print("%s Please restart the program to complete the setup%s" % (fg(1), attr(0)))
            time.sleep(5)
            exit()
        # ==============================================================
    elif AnswerT == "7":
        print("%s You Must Be Connected To Internet, are you Connected ? \n Enter Any Button if U Connected , Type 0 to exit. %s" % (fg(3), attr(0)))
        ckeck_i = input(" ")
        if ckeck_i == "0":
            exit()
        try:
            url = 'https://8gwifi.org/rsafunctions.jsp'
            # myobj = {'message': 'Hello'}
            # x = requests.post(url, data = myobj)
            x = requests.post(url)
            x = x.text
            bs = BeautifulSoup(x, 'lxml')
            PUB = bs.find('textarea', attrs={'name': 'publickeyparam'}).text
            PRI = bs.find('textarea', attrs={'name': 'privatekeyparam'}).text
            print("%s ========================= %s"% (fg(81), attr(0)) + "%sPublic Key%s"% (fg(1), attr(0)) + "%s ========================= %s" % (fg(81), attr(0)))
            print(PUB)
            print("%s ========================= %s"% (fg(81), attr(0)) + "%sPrivate Key%s" % (fg(1), attr(0)) + "%s ========================= %s" % (fg(81), attr(0)))
            print(PRI)
            print("%s ============================ End =============================%s" % (fg(81), attr(0)))
        except:
            print("%s ERRRRRRRRROR !!!!!! \n Maybe You Are Not Connect To Internet.%s"% (fg(1), attr(0)))
    elif AnswerT == "8":
        print()
        Q = input("%s Type : %s" % (fg(5), attr(0)))
        print()
        print(urllib.parse.quote(Q))
    elif AnswerT == "0":
        exit()
    else:
        print("ERRRRRRRRROR !!!!!!")
elif AnswerQ == "3":
    print()
    print("%s Instagram      : @qq_iq %s" % (fg(25), attr(0)))
    print("%s Discord        : !S A I F#7415 %s" % (fg(25), attr(0)))
    print("%s Discord Server : https://discord.gg/aunr59K %s" % (fg(25), attr(0)))
    print("%s Github         : https://github.com/JUSTSAIF%s" % (fg(25), attr(0)))
    print()
elif AnswerQ == "0":
    exit()
else:
    print("ERRRRRRRRROR !!!!!!")