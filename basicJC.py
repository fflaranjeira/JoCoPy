# basicJC.py
# module to perform basic calculations for Joint Count Analysis of infected plants
# in lattices

import math
#############################################################################
def Order (linhas):

    length = len(linhas)
    
    if len(linhas[0]) < length:
        
        length = len(linhas[0])

    nth_order = (length / 3) + 1

    return nth_order

##############################################################################
def Ns_Calc (a):
    """Ns_Calc is a function that calculates the number of infected (nb), number of 
susceptibles (nw), total number of plants in the lattice (ntotal) and the incidence"""
    
    nb = 0
    ntotal = len ( a ) * len ( a [0] )
    for i in range (len ( a) ):
        for j in range ( len ( a [0] )):
            nb += int (a [ i ] [ j ])

    ntotal = float (ntotal)
    nb = float (nb)
    nw = ntotal - nb
    incidence = nb / ntotal


    return ntotal, nb, nw, incidence

#############################################################################
def Exp_Calc (S0, nb, ntotal, nw):
    """Exp_Calc is a function that calculates the expected number of BB and BW joins.
See Cliff and Ord (1981)"""

# Calculates the expected number of BB and BW joins
# See Cliff and Ord (1981)

    Exp_BB = 0.5  * S0 * nb  / ntotal * ( nb - 1 ) / ( ntotal-1 )

    Exp_BW = S0 * nb  / ntotal * nw / ( ntotal - 1 )

    return Exp_BB, Exp_BW
    
##############################################################################   
def StDev_Calc (S1, nb, ntotal, S2, S0, Exp_BB, nw, Exp_BW):

    """StDev_Calc is a function that calculates the variance and Std deviation for BB
    and BW joins.See Cliff and Ord (1981)"""
    
# Calculates the variance and Std deviation for BB and BW joins
# See Cliff and Ord (1981)

#n = ntotal
#Var BB = 0.25*(S1*nb/n * (nb-1)/(n-1) + float(S2-2 * S1)*nb/n * (nb-1)/(n-1) *(nb-2)/(n-2)
# + (pow(S0,2) + S1 - S2) * nb/n * (nb-1)/(n-1) * (nb-2)/(n-2) * (nb-3)/(n-3)) - pow(Exp_BB,2)


    first_term = (S1 * (nb * (nb - 1))) / (ntotal * (ntotal - 1))
    second_term = ( S2 - (2 * S1) ) * (nb * (nb-1) * (nb - 2)) / (ntotal * (ntotal - 1) * (ntotal - 2))
    third_term = (pow(S0,2) + S1 - S2) * nb / ntotal * (nb - 1) / (ntotal - 1) * (nb - 2) / (ntotal - 2) * (nb - 3) / (ntotal - 3)
    fourth_term = pow (Exp_BB, 2)
    
    Var_BB = 0.25 * ( first_term + second_term + third_term ) - fourth_term

# Variance for BW, assuming sampling without replacement, i.e.,
# positions in the lattice are not independent
# Var BW = 0.25 * [first_termBW + second_termBW + third_termBW] - pow(Exp_BW,2)

    first_termBW = (( 2 * S1 * nb *nw ) / (ntotal * ( ntotal - 1 )))

    numerator = ( (S2 - (2*S1) ) * nb * nw * ( nb + nw - 2 ) )
    denominator = ntotal * ( ntotal -  1) * ( ntotal -  2 )
    second_termBW = numerator / denominator

    numerator2 = (( pow( S0, 2 ) + S1 - S2 ) * nb *(nb - 1) * nw * (nw - 1) )
    denominator2 = ntotal  * ( ntotal - 1 ) * ( ntotal - 2 ) * ( ntotal -  3 )
    third_termBW = 4.0 * (numerator2 / denominator2)

    fourth_termBW = pow (Exp_BW, 2)

    Var_BW = 0.25 * (first_termBW + second_termBW + third_termBW) - fourth_termBW

# Calculates the Std Deviations

    StDev_BB = math.sqrt(Var_BB)
    if StDev_BB == 0.0: StDev_BB = 0.000001
    
    StDev_BW = math.sqrt (Var_BW)
    if StDev_BW == 0.0: StDev_BW = 0.000001

    return StDev_BB, StDev_BW

##############################################################################

def Z_Calc (Observed, Expected, StDev):
    
    """Z_Calc calculates the statistic Z, i.e., (Observed Joins - Expected Joins)/StDev"""

    Z = (Observed - Expected) / StDev

    return Z

##############################################################################