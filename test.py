# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19_Xw4L8l072r_p5gx2ZbcHRY9PEiX2pf
"""

from smartapi import SmartConnect
import pandas as pd
import streamlit as st

obj = SmartConnect(api_key = 'B94qZLC7')
data = obj.generateSession('P714176', 'P@ssw0rd@123')

def place_order(orderparams):
    try:
        orderID = obj.placeOrder(orderparams)
        placeholder1.success(f"The Order ID for Symbol {orderparams['tradingsymbol']} is: {orderID}")
    except Exception as e:
        placeholder1.error(f"Order placement for Symbol {orderparams['tradingsymbol']} failed: {e}")

def generate_trade_list(uploaded_file):

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        df = pd.read_excel(uploaded_file)
    trade_list = [] #empty list

    #looping over each row in the dataframe and storing
    #the value in each column to generate orderparams dict
    #we use str to convert to strings
    for index, rows in df.iterrows():
        new_dict = {"variety": str(rows['variety']), 
                    "tradingsymbol" : str(rows['tradingsymbol']),
                    "symboltoken" : str(rows['symboltoken']),
                    "transactiontype": str(rows['transactiontype']), 
                    "exchange": str(rows['exchange']),
                    "ordertype": str(rows['ordertype']), 
                    "producttype": str(rows['producttype']),
                    "duration": str(rows['duration']), 
                    "price": str(rows['price']), 
                    "quantity": str(rows['quantity']),
                    "triggerprice": str(rows['triggerprice'])}

        trade_list.append(new_dict)