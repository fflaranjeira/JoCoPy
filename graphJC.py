# graphJC.py
# module to harbour some matplotlib functions and graph results of JoCoPy

import matplotlib.pyplot as plt

##################################################################
def Plotting (plotflag, resultlist, lag, ID):

    """Creates line plots using matplotlib, pop them on the screen, save them as png"""
     
    if plotflag == 'Queen': y = resultlist[0]
            
    elif plotflag == 'Rook': y = resultlist[1]
        
    elif plotflag == 'Within': y = resultlist[2]
        
    elif plotflag == 'Across': y = resultlist[3]
    
    
    x = [i for i in range(1, lag)]


    plt.figure (1)
    plt.plot(x, y, 'ko')

    plt.title (ID + ' case: ' + plotflag)
    plt.xlabel('Spatial lag', size=18)
    plt.ylabel('Z (BB)', size=18)
    plt.axis([min(x) - 1, max(x) +1, min(y) - 1, max(y) + 1])
    plt.axhline(y = 1.96)
    plt.axhline(y = -1.96)

    plt. savefig(ID + '_' + plotflag + '.png', dpi=600, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='png',
        transparent=False)
        
    if plotflag != 'Queen':
        plt.clf( )
    else: plt.show( )
    
##################################################################