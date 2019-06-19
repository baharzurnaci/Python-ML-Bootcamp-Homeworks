#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sayi = int(input('Sayı değeri giriniz: '))
carp = 1
for oku in range(sayi):
    carp = carp*(oku+1)
 
 print('Faktoriyel: ', carp)

