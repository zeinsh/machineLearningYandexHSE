
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import matplotlib


# In[2]:

def scatterData(X,y,classmap):
    for c,label in classmap.iteritems():
        pltdata=X[(y==c)]
        plt.scatter(pltdata[:,0], pltdata[:,1] ,label=label) 
