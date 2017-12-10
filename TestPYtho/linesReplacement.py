listOfFiles = open("ListOfAllFilesToATF.txt", "r")  # opening text file with list of files needed
oneFileFromList = listOfFiles.readlines()

for decodedFile in oneFileFromList:  # for every FILE IN FILE LIST

    infile = open('OUT' + decodedFile.rstrip('\n'))  # opening one file from file list

    # a = ['SnmpMibObject dot11ApplySettings.0 Integer 1; /* true */', 'GenericTLV TlvCode 11 TlvLength 25 TlvValue 0x301706122b06010401a23d020202010504010e010221020102;', 'GenericTLV TlvCode 11 TlvLength 21 TlvValue 0x3013060e2b06010401a23d02020201056400020101;', 'SnmpMibObject dot11BssEnable.33 Integer 2;']
    # b = ['SnmpMibObject cgHttpAltAccessUsername.0 String "thomson" ;', 'SnmpMibObject cgHttpAltAccessUsername.0 String "thomson";']
    c = ['NetworkAccess 1;', 'NetworkAccess 0;']
    atf = ['SnmpMibObject wifiMgmtATMApplicationATM.band24G Integer 1;',
           'SnmpMibObject wifiMgmtATMApplicationATM.band24G Integer 1 ;',
           'SnmpMibObject wifiMgmtATMApplicationATM.band5G Integer 1;',
           'SnmpMibObject wifiMgmtATMApplicationATM.band5G Integer 1 ;',
           'SnmpMibObject wifiMgmtATMBSSWeight.band24G String "70,20,0,10,0,0,0,0" ;',
           'SnmpMibObject wifiMgmtATMBSSWeight.band24G String "70,20,0,10,0,0,0,0";',
           'SnmpMibObject wifiMgmtATMBSSWeight.band5G String "70,20,0,10,0,0,0,0" ;',
           'SnmpMibObject wifiMgmtATMBSSWeight.band5G String "70,20,0,10,0,0,0,0";',
           'SnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.7.2 Integer 1;',
           'SnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.7.1 Integer 1;',
           'SnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.3.2 String "70,20,0,10,0,0,0,0";',
           'SnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.3.1 String "70,20,0,10,0,0,0,0";']
    checkerIfAtf = False
    for line in infile:
        for wordAtf in atf:
            if wordAtf in line:
                print("zmieniam na true wiec atf jest")
                checkerIfAtf = True
    infile.close()
    infile = open('OUT' + decodedFile.rstrip('\n'))
    outfile = "ATF" + infile.name
    fout = open(outfile, "w+")
    for line in infile:
        #outfile = "ATF" + infile.name
        #fout = open(outfile, "w+")
        #for line in infile:

                    # for wordb in b:
                    # line = line.replace(wordb, wordb + '\n\tSnmpMibObject 1.3.6.1.4.1.2863.205.10.1.30.100.0 Integer 1; /* MODIFICATION SEE JIRA TC7200-106, 120 */\n\tSnmpMibObject 1.3.6.1.4.1.2863.205.10.1.45.0 Integer 2;')
                    # for word in a:
                    # line = line.replace(word, "/* Line removed: " + word.rstrip('/* true */') + " */")
        if not checkerIfAtf:
                for wordc in c:
                    line = line.replace(wordc,
                                            wordc + '\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.7.2 Integer 1;\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.7.1 Integer 1;\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.3.2 String "70,20,0,10,0,0,0,0";\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.3.1 String "70,20,0,10,0,0,0,0";')

        fout.write(line)

    infile.close()

listOfFiles.close()
