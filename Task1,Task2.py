# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:10:39 2023

@author: Kumar
"""
# importing all the needed libraries
import sqlite3
import pandas as pd

#set path to sqlite file
path=r"C:\Users\Kumar\Desktop\New folder\trades.sqlite"



# function to load data from the path
def  load_data(path):

    conn = sqlite3.connect(path)


    sql_query = pd.read_sql_query ("SELECT * FROM epex_12_20_12_13",conn)
    df = pd.DataFrame(sql_query)
    return df

#Task1

#simple function i did group by and sum 
def compute_total_buy_volume():
    df2=load_data(path)
    df1 = df2.groupby(["side"]).sum()
    

    return (print(df1.iloc[0]['quantity']))



def compute_total_sell_volume():
    df2=load_data(path)
    df1 = df2.groupby(["side"]).sum()
    
    return (print(df1.iloc[1]['quantity']))



#Task 2

# if logic is worng i am sorry but its just a formula thing

def compute_pnl(strategy_id):
    df2=load_data(path)
    trade_strg = df2[df2['strategy'] == strategy_id]
    # variable to store profit or loss
    PnL = 0
    for idx, rw in trade_strg.iterrows():
        if rw['side'] == 'buy':
            PnL -= rw['quantity'] * rw['price']
        else:
            PnL += rw['quantity'] * rw['price']
    
    return PnL


