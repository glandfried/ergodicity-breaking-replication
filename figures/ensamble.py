import os
name = os.path.basename(__file__).split(".py")[0]
##########
import matplotlib.pyplot as plt
import sys
import numpy as np
sys.path.append('../software/')
import erg 
#from importlib import reload  # Python 3.4+ only.
#reload(ergodicity)
    
population = erg.multiplicative_perturbed_history(n=1000,iterations=50,rate=1.05,dt=1/12,sigma=4.5)
population = np.array(np.matrix(population))

# 1
plt.plot(np.log( np.cumprod([1]+[1.05]*49) ))
plt.plot(np.log( np.mean(population[0:1,],axis=0) ))
plt.plot(np.log( np.mean(population[0:10,],axis=0) ))
plt.plot(np.log( np.mean(population[0:100,],axis=0) ))
plt.plot(np.log( np.mean(population,axis=0) ))

plt.xticks(fontsize=12) # rotation=90
plt.yticks(fontsize=12) # rotation=90
plt.ylabel("Wealth (log scale)", fontsize=16 )
plt.xlabel("Time", fontsize=16 )
plt.savefig(name+"_1000.pdf",pad_inches =0,transparent =True)
plt.savefig(name+"_1000.png",pad_inches =0,transparent =True,dpi=90)

alone = erg.multiplicative_perturbed_history(n=1,iterations=10000,rate=1.05,dt=1/12,sigma=4.5)
plt.plot(np.log( np.cumprod([1]+[1.05]*9999) ))
plt.plot(np.log( alone[0] ))

plt.xticks(fontsize=12) # rotation=90
plt.yticks(fontsize=12) # rotation=90
plt.ylabel("Wealth (log scale)", fontsize=16 )
plt.xlabel("Time", fontsize=16 )
plt.savefig(name+"_alone.pdf",pad_inches =0,transparent =True)
plt.savefig(name+"_alone.png",pad_inches =0,transparent =True,dpi=90)


#bash_cmd = "pdfcrop --margins '0 0 0 0' {0}.pdf {0}.pdf".format(name)
#os.system(bash_cmd)
    
