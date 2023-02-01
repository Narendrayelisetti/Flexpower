# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 23:27:46 2023

@author: Kumar
"""
import traceback
from flask import Flask, jsonify
import pandas as pd
import sqlite3
import os





# using flask as web app
path=os.getcwd() + "/trades.sqlite"
try:
    app = Flask(__name__)

    
    def  load_data(path):

        conn = sqlite3.connect(path)


        sql_query = pd.read_sql_query ("SELECT * FROM epex_12_20_12_13",conn)
        df = pd.DataFrame(sql_query)
        return df

    def compute_pnl(strategy_id):
        df2=load_data(path)
        trade_strg = df2[df2['strategy'] == strategy_id]
        PnL = 0
        for idx, rw in trade_strg.iterrows():
            if rw['side'] == 'buy':
                PnL -= rw['quantity'] * rw['price']
            else:
                PnL += rw['quantity'] * rw['price']
        
        return PnL

    @app.route("/pnl/strategy_1", methods=["GET"])
    def pnl():
        strategy_id = 'strategy_1'
        pnl = compute_pnl(strategy_id)

        return jsonify({
            "strategy": strategy_id,
            "value": pnl,
            "unit": "euro",
            "capture_time": "2023-01-31T12:00:00Z"
        })
    
    @app.route("/pnl/strategy_2", methods=["GET"])
    def pnl2():
        strategy_id = 'strategy_2'
        pnl = compute_pnl(strategy_id)
        return jsonify({
            "strategy": strategy_id,
            "value": pnl,
            "unit": "euro",
            "capture_time": "2023-01-31T12:00:00Z"
        })
    # your code here
except Exception as e:
    traceback.print_exc(e)
   



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080,debug=True)
