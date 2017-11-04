
# coding: utf-8

# In[ ]:




# In[2]:

def scatterData(X,y,classmap):
    import matplotlib.pyplot as plt
    for c,label in classmap.iteritems():
        pltdata=X[(y==c)]
        plt.scatter(pltdata[:,0], pltdata[:,1] ,label=label) 

def plotDecisionBoundary(w,bias,fig_boundary):
    import matplotlib.pyplot as plt
    from helpersmd import getLine
    xline,yline=getLine(w,bias,fig_boundary)
    plt.plot(xline,yline, 'k-',label="Decision Boundary")

