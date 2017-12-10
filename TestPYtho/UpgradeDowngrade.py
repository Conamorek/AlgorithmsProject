import os
import time

for i in range(0, 99999):
    a = open("ListOfCompalsIPs.txt", "r")
    ip_list = a.readlines()
    print("Step number:")
    print(i)

    for ip in ip_list:
        cmd1 = "snmpset -v 2c -c g7UfdQ3z %s .1.3.6.1.2.1.69.1.3.1.0 a 62.179.2.164" % ip.strip()
        print(cmd1)
        process1 = os.popen(cmd1, "r")
        time.sleep(1)
        cmd2 = "snmpset -v 2c -c g7UfdQ3z %s .1.3.6.1.2.1.69.1.3.2.0 s firmware/mercury/compal/CH7465LG-4.50.18.23-4-NOSH.p7.newcvc" % ip.strip()
        print(cmd2)
        process2 = os.popen(cmd2, "r")
        time.sleep(1)
        cmd3 = "snmpset -v 2c -c g7UfdQ3z %s .1.3.6.1.2.1.69.1.3.3.0 i 1" % ip.strip()
        print(cmd3)
        process3 = os.popen(cmd3, "r")
        time.sleep(3)
        process1.close()
        process2.close()
        process3.close()

    a.close()
    time.sleep(1800)

    b = open("ListOfCompalsIPs.txt", "r")
    list_ip = b.readlines()

    for anotherIp in list_ip:
        cmd4 = "snmpset -v 2c -c g7UfdQ3z %s .1.3.6.1.2.1.69.1.3.1.0 a 62.179.2.164" % anotherIp.strip()
        print(cmd4)
        process4 = os.popen(cmd4, "r")
        time.sleep(1)
        cmd5 = "snmpset -v 2c -c g7UfdQ3z %s .1.3.6.1.2.1.69.1.3.2.0 s firmware/mercury/compal/CH7465LG-6.12.18.24-4-NOSH.p7.newcvc" % anotherIp.strip()
        print(cmd5)
        process5 = os.popen(cmd5, "r")
        time.sleep(1)
        cmd6 = "snmpset -v 2c -c g7UfdQ3z %s .1.3.6.1.2.1.69.1.3.3.0 i 1" % anotherIp.strip()
        print(cmd6)
        process6 = os.popen(cmd6, "r")
        time.sleep(3)

    b.close()
    time.sleep(1800)
