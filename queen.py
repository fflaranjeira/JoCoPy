# queen.py
# module to perform basic calculations for JoCoPy  program
# Joint Count Analysis in a Lattice using Python, queen's case


###############################################
# Import needed modules

import math

##############################################################################
    
def BB_et_BW_Calc (a, order):

    BB = 0
    BW = 0
    
    for i in range ( len ( a  )  ):
        for j in range ( len ( a [0] ) ):
            try:
                if a [ i ] [ j ] !=a [ i + order] [ j ]  :
                    BW +=1
                elif a [ i ] [ j ] == '1' and a [ i + order ] [ j ] == '1':
                    BB += 1
            except IndexError: continue
            
    for i in range ( len ( a )  ):
        for j in range ( len ( a [0]) ):           
            try:
                if a [ i ] [ j ] != a [ i + order ] [ j + order] :
                    BW += 1
                elif a [ i ] [ j ] == '1' and a [ i + order ] [ j + order] == '1':
                    BB +=  1
            except IndexError: continue

    for i in range ( len ( a )  ):
        for j in range ( len ( a [0] ) ):           
            try:
                if a [ i ] [ j ] != a [ i ] [ j + order ] :
                    BW += 1
                elif a [ i ] [ j ] == '1' and a [ i ] [ j + order ] == '1':
                    BB += 1
            except IndexError: continue

    for i in range (1, len ( a )  ):
        for j in range ( len ( a  [0]) ):           
            try:             
                if a [ i ] [ j ] == '1' and a [ i - order] [ j + order ] == '1' :
                    BB += 1
                elif a [ i ] [ j ] != a [ i - order ] [ j + order ] :
                    BW += 1
            except IndexError: continue
            

    return BB, BW
##############################################################################

def Ss_Calc (order, a):


    # Calculates S0 (Check Cliff and Ord (1981))
    
    # So = 4 plants on the corners, each one with 3 neighbours (4 *3 ) +
    # Plants in the 2 extreme columns (first and last), each one with 5 neighbours
    # except for the 2 plants in the corners ( 2 * 5 * (columns - 2)) +
    # Plants in the 2 extreme lines (first and last), each one with 5 neighbours
    # except for the 2 plants in the corners ( 2 * 5 * (lines - 2)) +
    # Plants in the middle, each one with 8 neighbours [ (lines - 2) * (columns -2 ) * 8 ]

    S0 = (4.0 * pow (order,2)  * 3) +  ( 2 *order * 5 * ( len ( a [0] ) - (2*order) ) ) +  ( 2 *order * 5 * ( len ( a ) - (2*order) ) ) + ( ( len ( a [0] ) - (2*order) ) * ( len ( a ) - (2*order) ) * 8 )

    # Calculates S1 (Check Cliff and Ord (1981))
    # S1 = 4 * (BB + BW + WW) or
    # S1 = 0.5 * (4 corners * 3 neighbours * ( 1 + 1 )**2 +. The inside brackets are the weight of i position on j position and j on i
    # 4 sides * (plants on each side - corners) * 5 neighbours * ( 1 + 1 )**2 +
    # plants in the middle [(columns - 2) * (lines - 2)] * 8 neighbours *( 1 + 1 )**2)

    S1 = 0.5 * (((4 * pow (order,2) * 3) * ( 2 )**2) + \
             ( 2 *order * ( len ( a [0] ) - (2*order) ) * 5 * ( 2 )**2 ) + \
            ( 2 *order * ( len ( a ) - (2*order) ) * 5 * ( 2 )**2 ) + \
             ( ( len ( a [0] ) - (2*order) ) * ( len ( a ) - (2*order) ) * 8 * ( 2 )**2 ))


    # Calculates S2 (Check Cliff and Ord (1981))
    # S2 = 4  * 4corners *(3 neighbours )**2 + [corners]
    # 4 *  2 columns* [(column - 2) ]*( 5 neighbours )**2 + [ up and down borders)
    # 4 * 2 lines * [(lines - 2) ] * ( 5 neighbours )**2 + [ left and right borders)
    # 4 * [(column - 2) ] * [(lines - 2) ] * (8 neighbours )**2 [middle]


    S2 = 4.0 * (( 4.0 * pow (order,2) * (3)**2) + (2 *order *( len ( a [0] ) - (2*order) ) * (5)**2) + (2 *order *( len ( a ) - (2*order) )  * (5)**2) + ( ( len ( a [0] ) - (2*order) ) * ( len ( a ) - (2*order) )) *(8)**2)
       

    return S0, S1, S2
##############################################################################
