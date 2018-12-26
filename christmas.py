import sys
import time

string="!!MERRY CHRISTMAS!!\n     *\n    ***\n   *****\n  *******\n *********\n    ***   \n    ***   \n"
          
for j in string:
    #sys.stdout.write("\r{0}".format(j))
    sys.stdout.write(j)
    sys.stdout.flush()
    time.sleep(0.5)












"""for j in range(15,1,-1):
    print(15*" "+j*" "+(15-(j-1))*"*"+(15-(j))*"*")
for i in range(1,8):
    print(28*" "+5*"*")"""
