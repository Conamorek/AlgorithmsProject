import os
import shutil
import errno
import time

newpath = r'C:/Users/Maciej_Papurzynski/Documents/Lg/IEBootfileCreation/Script/PrefixCut'
if not os.path.exists(newpath):
    os.makedirs(newpath)

listOfFiles = open("ListOfAllFilesToATF.txt", "r")  # opening text file with list of files needed
oneFileFromList = listOfFiles.readlines()

for decodedFile in oneFileFromList:  # for every FILE IN FILE LIST

    infile = open('OUT' + decodedFile.rstrip('\n'))  # opening one file from file list

    # a = ['SnmpMibObject dot11ApplySettings.0 Integer 1; /* true */', 'GenericTLV TlvCode 11 TlvLength 25 TlvValue 0x301706122b06010401a23d020202010504010e010221020102;', 'GenericTLV TlvCode 11 TlvLength 21 TlvValue 0x3013060e2b06010401a23d02020201056400020101;', 'SnmpMibObject dot11BssEnable.33 Integer 2;']
    # b = ['SnmpMibObject cgHttpAltAccessUsername.0 String "thomson" ;', 'SnmpMibObject cgHttpAltAccessUsername.0 String "thomson";']
    c = ['NetworkAccess 1;', 'NetworkAccess 0;']
    outfile = "ATF" + infile.name
    fout = open(outfile, "w+")
    for line in infile:
        # for wordb in b:
        # line = line.replace(wordb, wordb + '\n\tSnmpMibObject 1.3.6.1.4.1.2863.205.10.1.30.100.0 Integer 1; /* MODIFICATION SEE JIRA TC7200-106, 120 */\n\tSnmpMibObject 1.3.6.1.4.1.2863.205.10.1.45.0 Integer 2;')
        # for word in a:
        # line = line.replace(word, "/* Line removed: " + word.rstrip('/* true */') + " */")
        for wordc in c:
            line = line.replace(wordc,
                                wordc + '\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.7.2 Integer 1;\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.7.1 Integer 1;\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.3.2 String "70,20,0,10,0,0,0,0";\n\t\tSnmpMibObject .1.3.6.1.4.1.35604.2.3.8.1.1.1.3.1 String "70,20,0,10,0,0,0,0";')

        fout.write(line)

    fout.close()
    infile.close()

listOfFiles.close()


source = 'C:/Users/Maciej_Papurzynski/Documents/Lg/IEBootfileCreation/Script/'
dest1 = 'C:/Users/Maciej_Papurzynski/Documents/Lg/IEBootfileCreation/Script/PrefixCut/'

thoseFiles = os.listdir(source)
thoseAnotherFiles = os.listdir(dest1)

for f in thoseFiles:
    if f.startswith("ATFOUT"):
        shutil.move(source+f, dest1)

for data in os.listdir('C:/Users/Maciej_Papurzynski/Documents/Lg/IEBootfileCreation/Script/PrefixCut/'):
    if data.startswith("ATFOUT"):
        os.rename(os.path.join(dest1, data), os.path.join(dest1, data[6:]))



