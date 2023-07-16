import pandas as py
import random 
import math
import numpy as np

def generate_player():
    
    player = {
        'current': [
            ('Research & Development',[
                ('Performance' , 4),#random.randint(4, 15)),
                ('Size' , random.randint(1, 15)),
                ('Reliability' , random.randint(10000, 20000)),
            ],185),
            ('Marketing',[
                ('Price' , random.randint(15, 35)),
                ('Promo_budget' , random.randint(0, 3000)),
                ('Sales_budget' , random.randint(0, 3000)),
                ('Unit_sales_forecast' , random.randint(0, 3000)),
            ],225),
            ('Production',[
                ('Production_order' ,  100),
                ('Capacity_changer' ,  random.randint(0, 100)),
            ],140),
            ('Finance',[
                ('Current_debt' ,  0),
                ('Bond_issue' ,  0),
                ('Bond_retire' ,  0),
                ('Stock_outs', False),
                ('Cash', 0),
                ('Bond_list' , ['10_10000_3','10_10000_4','10_10000_5']),
                ('E_loan', 0),
            ],350),
            ('Calculation',[
                ('Awareness' , 0),
                ('Accessibility' , 0),
                ('Favourability' , 35 ),
                ('Units_sold' , 0),
                ('Revenue' , 0),
            ],265),
            ('Rest',[
                ('Plant_capacity', 100),
                ('Capacity_change',0),
                ('Inventory',30),
            ],180),
        ]
    }

    return player