import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

df = pd.read_csv("log-k", encoding="UTF-8")
#plt.figure(figsize=(4, 4))
#plt.rcParams['font.family'] = 'Ricty'
#plt.rcParams['font.family'] = 'Meiryo'
plt.rcParams["font.size"] = 22
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 15
plt.rcParams["legend.fontsize"] = 18
plt.grid()

print(df)


colorlist = ["#2ca9e1","#e95295","#aacf53","#f8b500"]

data = df["r"]
m_size=range(100,3100,100)

plt.axhline(y=0)
plt.ylim(ymax=2.0)
plt.ylim(ymin=0.0)
plt.xlim(xmin=0)
plt.xlim(xmax=3000)


plt.xlabel("Matrix size N x N (N)")
plt.ylabel("Speed up")


plt.plot(m_size,data,"r",color=colorlist.pop(),markersize=2)
plt.legend()

plt.savefig("speedup.png", bbox_inches="tight")
