#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SIFIRDAN YAPAY SİNİR AĞI YAZMA

import numpy as np

def sigmoid(x):
   return 1 / (1 + np.exp(-x))

n = 0.5 #n:öğrenme oranı
i = np.array([[0.05,0.10]], dtype=np.float64)  #aynı boyutlu matrislerde işlem yapılır
w1 = np.array([[0.15,0.25],[0.20,0.30]], dtype=np.float64)
b1 = 0.35

h = (np.dot(i,w1)+ b1)   #h1:0.3775 , h2:0.3925 , h:gizli katman çıktısı
h1sigmoid = sigmoid(h)
print("sigmoid sonucu [h1,h2] : {} ".format(h1sigmoid))

w2 = np.array([[0.40,0.50], [0.45,0.55]], dtype=np.float64)
b2 = 0.60
neto1 = np.array([[0.59326999, 0.59688438]], dtype = np.float64)

o = (np.dot(neto1,w2)+ b2)    #o1:1.10590597 , o2:1.2249214
o1sigmoid = sigmoid(o)
print("sigmoid sonucu [o1,o2] : {} ".format(o1sigmoid))

#hata değeri bulma

hedef = np.array([[0.01, 0.99]], dtype = np.float64)
gercek = np.array([[0.75136507, 0.77292847]], dtype = np.float64)

cıktı = (gercek - hedef) 
toplamhata = 1/2 * np.sum(cıktı**2)
print("toplamhata : {} ".format([toplamhata]))

#geriye doğru yayılım

degisim = np.dot(h1sigmoid.T, -(hedef-gercek) * o1sigmoid* (1-o1sigmoid)) 
print("degisim : {} ".format(degisim))

yenidegerler = w2 - n*degisim
print("yenidegerler : {} ".format(yenidegerler))

#0.08216704: 0.74136507x0.1868156x0.59326999yapar:w5, (0.4-n*0.08216704):0.3589..
#0.02274024: 0.21707153x0.17551005x0.59688438yapar:w8, (0.55-n*0.02274024):0.5613...
#0.08266763: 0.74136507x0.1868156x0.59688438yapar:w6, (0.45-n*0.08266763):0.4086...
#0.02260238: 0.21707153x0.17551005x0.59326999yapar:w7  ,(0.50-n*-0.02260238):0.51130127



# In[ ]:




