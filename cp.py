import sys
import subprocess
src = sys.argv[1]
dest = sys.argv[2]

readsrc = subprocess.run('cat %s' %src, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
content = readsrc.stdout
with open(dest, 'w+') as getdest:
    getdest.writelines(str(content))
