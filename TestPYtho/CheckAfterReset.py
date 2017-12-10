import os
import time

a = open("IpList.txt", "r")
ListOfIp = a.readlines()
b = open('DidntBootAfterReset.txt', 'a+')
counter = 0

for ip in ListOfIp:
    cmd1 = "./edmt.pl c_poll %s" % ip.strip()
    print(cmd1)
    process1 = os.popen(cmd1, "r")
    time.sleep(3)
    outputFromConsole = process1.read()
    word = "SNMPv2"
    if word not in outputFromConsole:
        b.write("%s" % ip.strip())
        b.write("\n")
process1.close()
a.close()
b.close()
