# Tests 
from dht import *
import numpy as np
import matplotlib.pyplot as plt
import random
import pickle

N_e = 14
N_s = 3
num_exp = 100
numJumps_join = {} 
numJumps_pf = {} 

for i in range(N_s, N_e+1):
    numJumps_join[i] = {}
    numJumps_pf[i] = {} 
    for exp in range(num_exp):
        numJumps_join[i][exp] = []
        numJumps_pf[i][exp] = []



for exp in range(num_exp):
    
    print("--{} exp / {}".format(exp, num_exp-1))
    for i in range(N_s, N_e+1):
        print("{}/{}".format(i,N_e))
        d = DHT(i)
        
        # Add nodes
        all_nodes = set(range(2**i))
        for j in range((2**i)):
            r = random.choice(tuple(all_nodes))
            all_nodes.remove(r)
            numJumps_join[i][exp].append(d.join(Node(r)))
           
        
        #msg forwarding
        all_nodes = set(range(2**i))
        for j in range(2**i):
            n1 = random.choice(tuple(all_nodes))
            n2 = random.choice(tuple(all_nodes))
            a = d.packet_forward(n1, n2)
            if a == 0:
                continue
            #numJumps_pf[i-3][exp] += a
            numJumps_pf[i][exp].append(a)
    


with open('numJumps_join.pickle', 'wb') as handle:
    pickle.dump(numJumps_join, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    
with open('numJumps_pf.pickle', 'wb') as handle:
    pickle.dump(numJumps_pf, handle, protocol=pickle.HIGHEST_PROTOCOL)


