import os
import time

a = open("ListOfFiles.txt", "r")
binary_list = a.readlines()
counter = 0

for bin in binary_list:
    cmd1 = "docsis -e %s keyfile %s > /tmp/EncodedLastChange1212/%s" % (
    bin.strip(), bin.strip())  # takes bin from bin_list and puts it into command
    print (cmd1)
    process1 = os.popen(cmd1, "r")
    # data1 = process1.read()
    counter += 1
    print
    counter
    time.sleep(1)
    process1.close()

a.close()
