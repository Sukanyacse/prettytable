# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:37:03 2020

@author: ELCOT
"""

from prettytable import PrettyTable
#specify the column names while initializing the table
myTable=PrettyTable(["student name","class","section","percentage"])
#add rows
myTable.add_row(["sukan","x","a","55%"])
myTable.add_row(["saras","x","b","65%"])
print(myTable)