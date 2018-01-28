# within.py
# module to perform basic calculations for JoCoPy  program
# Joint Count Analysis in a Lattice using Python, within's case


###############################################
# Import needed modules

import math

##############################################################
def BB_et_BW_Calc (a, order):

    BB = 0
    BW = 0
    
          
    for i in range ( len ( a )  ):
        for j in range ( len ( a [0] ) ):           
            try:
                if a [ i ] [ j ] != a [ i + order] [ j ] :
                    BW += 1
                elif a [ i ] [ j ] == '1' and a [ i + order ] [ j ] == '1':
                    BB += 1
            except IndexError: continue
            

    return BB, BW
##############################################################################

def Ss_Calc (order, a):


    # Calculates S0 (Check Cliff and Ord (1981))
    

    S0 =   ( 2 *order * 1 * ( len ( a [0] ) ) ) + ( ( len ( a ) - (2*order) ) * ( len ( a [0]) ) * 2 )

    # Calculates S1 (Check Cliff and Ord (1981))


    S1 = 0.5 * (( 2 *order * ( len ( a [0] ) ) * 1 * ( 2 )**2 ) + \
             ( ( len ( a ) - (2*order) ) * ( len ( a [0] ) ) * 2 * ( 2 )**2 ))


    # Calculates S2 (Check Cliff and Ord (1981))


    S2 = 4.0 * ((2 *order *( len ( a [0]) )  * ( 1 )**2 ) + ( ( len ( a ) - (2*order) ) * ( len ( a [0] ))) *( 2 )**2)
       

    return S0, S1, S2
##############################################################################
