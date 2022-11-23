import psutil
import os
import time
from sys import *
import os


def ProcessDisplay(log_dir = "Marvellous"):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
        
    separator = "_" * 80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous process logger :"+time.ctime()+"\n")
    f.write(separator + "\n")    
    
    for proc in psutil.process_iter():
        
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_full_info().vms/(1024 * 1024)
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass   
    
    for element in listprocess:
        f.write("%s\n" % element)
    
    return listprocess

def main():
    
    print("Process Monitor with memory usage")
    
    listprocess = ProcessDisplay()
    
    for i in listprocess:
        print(i)
    
    
if __name__ =="__main__":
    main()    