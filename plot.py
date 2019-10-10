
import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd




with open('numJumps_join.pickle', 'rb') as handle:
    numJumps_join = pickle.load(handle)
    
with open('numJumps_pf.pickle', 'rb') as handle:
    numJumps_pf = pickle.load(handle)

results_join = pd.DataFrame(columns=['exp','1stperc','99thperc','mean'])   
results_pf = pd.DataFrame(columns=['exp','1stperc','99thperc','mean'])   

for key1, val1 in numJumps_join.items():
    list_all_join = []
    list_all_pf = []
    for key2, val2 in val1.items():
        list_all_join = list_all_join + numJumps_join[key1][key2] 
        list_all_pf = list_all_pf + numJumps_pf[key1][key2] 
        
    all_join_np = np.asarray(list_all_join)
    all_pf_np = np.asarray(list_all_pf)
        
    res_join = {'exp': key1,  '1stperc': np.percentile(all_join_np, 1),'99thperc': np.percentile(all_join_np, 99),'mean':np.mean(all_join_np)}
    res_pf = {'exp': key1,  '1stperc': np.percentile(all_pf_np, 1),'99thperc': np.percentile(all_pf_np, 99),'mean':np.mean(all_pf_np)}
    
    results_join = results_join.append(res_join, ignore_index = True)
    results_pf = results_pf.append(res_pf, ignore_index = True)
    
##Overhead of Node Insertion    
fig, ax = plt.subplots()
plt.scatter(results_join['exp'], results_join['1stperc'], marker='_', c = 'b')
plt.scatter(results_join['exp'], results_join['99thperc'], marker='_', c = 'b')
plt.scatter(results_join['exp'], results_join['mean'], c = 'b')
plt.vlines(results_join['exp'], results_join['1stperc'],results_join['99thperc'])
plt.xticks(results_join['exp'])
plt.xlabel('k (Number of Nodes = $2^{k}$)')
plt.ylabel('Number of Messages to Re-establish \n The Chord Routing Invariants')
plt.show()
fig.savefig('Node Insertion.jpg')

##Overhead of Packet Forwarding
fig, ax = plt.subplots()
plt.scatter(results_pf['exp'], results_pf['1stperc'], marker='_', c = 'b')
plt.scatter(results_pf['exp'], results_pf['99thperc'], marker='_', c = 'b')
plt.scatter(results_pf['exp'], results_pf['mean'], c = 'b')
plt.vlines(results_pf['exp'], results_pf['1stperc'],results_pf['99thperc'])
plt.xticks(results_pf['exp'])
plt.xlabel('k (Number of Nodes = $2^{k}$)')
plt.ylabel('Path Length')
plt.show()
fig.savefig('PF.jpg')

        
        
        

