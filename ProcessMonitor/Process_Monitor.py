import psutil

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass   

    return listprocess

def main():
    
    print("Process Monitor")
    
    listprocess = ProcessDisplay()
    
    for i in listprocess:
        print(i)
    
    
if __name__ =="__main__":
    main()    