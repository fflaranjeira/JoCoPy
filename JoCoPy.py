# JoCoPy
# A script to perform Join Count Analysis in lattices
# by Francisco Laranjeira


###############################################
# Import needed modules

import csv
import math
import string
import across
import within
import queen
import rook
import basicJC
import os.path
import graphJC
import time

##################################################################
def getInputs():
    # RETURNS  the name of the file to process for the entire analysis
   
    filename = ''
    
    while os.path.exists(filename) == False:
        filename = raw_input("What file do you want to process? ")
        
    return  filename
##################################################################
def getID(filename):
    # RETURNS  the ID for the entire analysis based on the name of the file, except
    # the termination ".txt". e.g 'A06foci.txt' => 'A06foci'
    
    id = string.upper (filename[ : -4])
    
    return  id
        
#################################################################

def Read_File( a ):

    # Imports a file, reads the lines and puts them in a list of lists
    # Remember that such a list contains strings
    
    infile = open(a, 'rb')
    data = csv.reader(infile, delimiter = ';')
    linhas = [ ]
    
    # Reads the list in the file, line by line

    for row in data:              # For each line in the file, append a list in linhas. 
        linhas.append(row)  # So, linhas is a list of lists

    return linhas
    infile.close( )
    data.close( )

##############################################################################

def GravaHeads (ID, incidence):

    # This function just put a Header in the output file
    heads =  [['Join Count Statistics'], ['File ' + ID ], ['Program JoCoPy'],[time.ctime()], ['Incidence: ', incidence], [ ]] 
    Write_File (ID, heads)    

##############################################################################

def Write_File(ID, lista ):

# Open the file created by Result_File ( ) function, appending it with final results
    
    outfile = open (ID +'_out.txt', 'ab')
    data = csv.writer(outfile, delimiter = '\t')

    for row in lista:
        data.writerow ( row )

    outfile.close( )
        
#################################################################
def trimList(lista):
    
    for item in lista:
        del item[0]
        
    return lista
#################################################################
def main():

    file_name = getInputs ( )
    
    ID = getID (file_name)
    
    linhas = Read_File ( file_name )
    
    (ntotal, nb, nw, incidence) = basicJC.Ns_Calc (linhas)

    GravaHeads (ID, incidence)
    
    sec_heads = [['Order', 'Case', 'BW', 'Z_BW', 'BB', 'Z_BB']]
    Write_File (ID, sec_heads)
   
    nth_order = basicJC.Order (linhas)
    
    queenBB, rookBB, acrossBB, withinBB = ['Queen' ], ['Rook' ], ['Within' ], ['Across' ]
    
    for order in range (1, nth_order):

        # Queen's case
        final_results = [  ]
        case = 'Queen'
        
        (BB, BW) = queen.BB_et_BW_Calc (linhas, order)
         
        (S0, S1, S2) = queen.Ss_Calc (order, linhas)
        
        (Exp_BB, Exp_BW) = basicJC.Exp_Calc (S0, nb, ntotal, nw)
        (StDev_BB, StDev_BW) = basicJC.StDev_Calc (S1, nb, ntotal, S2, S0, Exp_BB, nw, Exp_BW)        
        Z_BB = basicJC.Z_Calc (BB, Exp_BB,  StDev_BB)    
        Z_BW = basicJC.Z_Calc (BW, Exp_BW,  StDev_BW)
    
        final_results.append([order, case, BW, Z_BW, BB, Z_BB])    
        Write_File (ID, final_results)
        queenBB.append(Z_BB)
        
        # Rook's case
        final_results = [  ]
        case = 'Rook'
        (BB, BW) = rook.BB_et_BW_Calc (linhas, order)
         
        (S0, S1, S2) = rook.Ss_Calc (order, linhas)
        
        (Exp_BB, Exp_BW) = basicJC.Exp_Calc (S0, nb, ntotal, nw)
        (StDev_BB, StDev_BW) = basicJC.StDev_Calc (S1, nb, ntotal, S2, S0, Exp_BB, nw, Exp_BW)        
        Z_BB = basicJC.Z_Calc (BB, Exp_BB,  StDev_BB)    
        Z_BW = basicJC.Z_Calc (BW, Exp_BW,  StDev_BW)
    
        final_results.append([order, case, BW, Z_BW, BB, Z_BB])    
        Write_File (ID, final_results)
        rookBB.append(Z_BB)
        
        # Within rows' case
        final_results = [  ]
        case = 'Within'
        (BB, BW) = within.BB_et_BW_Calc (linhas, order)
         
        (S0, S1, S2) = within.Ss_Calc (order, linhas)
        
        (Exp_BB, Exp_BW) = basicJC.Exp_Calc (S0, nb, ntotal, nw)
        (StDev_BB, StDev_BW) = basicJC.StDev_Calc (S1, nb, ntotal, S2, S0, Exp_BB, nw, Exp_BW)        
        Z_BB = basicJC.Z_Calc (BB, Exp_BB,  StDev_BB)    
        Z_BW = basicJC.Z_Calc (BW, Exp_BW,  StDev_BW)
    
        final_results.append([order, case, BW, Z_BW, BB, Z_BB])    
        Write_File (ID, final_results)
        withinBB.append(Z_BB)
        
         # Across rows' case
        final_results = [  ]
        case = 'Across'
        
        (BB, BW) = across.BB_et_BW_Calc (linhas, order)
         
        (S0, S1, S2) = across.Ss_Calc (order, linhas)
        
        (Exp_BB, Exp_BW) = basicJC.Exp_Calc (S0, nb, ntotal, nw)
        (StDev_BB, StDev_BW) = basicJC.StDev_Calc (S1, nb, ntotal, S2, S0, Exp_BB, nw, Exp_BW)        
        Z_BB = basicJC.Z_Calc (BB, Exp_BB,  StDev_BB)    
        Z_BW = basicJC.Z_Calc (BW, Exp_BW,  StDev_BW)
    
        final_results.append([order, case, BW, Z_BW, BB, Z_BB]) 
        Write_File (ID, final_results)
        acrossBB.append(Z_BB)       
        
        
    third_heads = [[ ],['Case', 'Z_BB for orders: 1 to max order']]
    Write_File (ID, third_heads)   
    
  
    BBlist = [queenBB, rookBB, withinBB, acrossBB]
    Write_File (ID, BBlist)   

    BBlist = trimList (BBlist)


    # Plotting Results
    cases = ['Rook', 'Within', 'Across', 'Queen']
    
    for case in cases:
        graphJC.Plotting (case, BBlist, nth_order, ID)
    
        
main()


