import os
    
ida32wFilePath = "D:\\IDA_6.8\\idaq.exe"
#    ida64wFilePath = "\"D:\IDA 6.8\idaw64.exe\""
#    filepath = sys.argv[1]
#    logPath = r"C:\Users\1\Desktop\dlls\log.log"
pluginPath = "C:\\Users\\1\\Desktop\\ClassKnown\\classinformer.py"
filePath = r"C:\Users\1\Desktop\dlls"

for root, dirs, files in os.walk(filePath):
    for file1 in files:
        file_path = os.path.join(root, file1)
        cmd = ida32wFilePath + " -c -A -S" + pluginPath + " " + file_path
#        cmd = ida32wFilePath + " -L" + logPath + " -c -A -S" + pluginPath + " " + file_path
        os.system(cmd)
