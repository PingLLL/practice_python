import subprocess
import sys
import random
from string import ascii_letters, digits
def add_user(username, randpass, fname):
    while 1:
        check_user = subprocess.run('id %s' % username, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check_user.returncode == 0:
            print('user exist! Please imput another name')
        subprocess.run('useradd %s' %username, shell=True)

def gen_randpass():
    allstr = ascii_letters + digits
    randpass = ''
#    n = sys.argv[2]
    for i in range(8):
        result = random.choice(allstr)
        randpass += result
    return randpass


if __name__ == '__main__':
    username = sys.argv[1]
    randpass = gen_randpass()
    fname = '/tmp/userlist'
    add_user(username, randpass, fname)
