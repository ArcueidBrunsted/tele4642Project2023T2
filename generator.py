import time
import pandas as pd
import random
import numpy as np

while True:
    src = pd.DataFrame(np.random.choice(['host1','host2'],100,p=[0.5,0.5]), columns=['Source'])
    trafficType = pd.DataFrame(np.random.choice(['tcp','udp'],100,p=[0.5,0.5]), columns=['Type'])
    dst = pd.DataFrame(np.random.choice(['A','B'],100,p=[0.5,0.5]), columns=['Destination'])
    pktSize = pd.DataFrame(np.random.randint(1,1000,size=(100, 1)), columns=['Size'])
    df = pd.concat([src,trafficType,dst,pktSize], axis=1)
    print(df)
    df.to_csv('netstats.csv', encoding='utf-8', index=False)
    time.sleep(5)