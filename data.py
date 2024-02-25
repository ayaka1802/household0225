import streamlit as st
import sqlite3
import pandas as pd
import numpy as np

# データベースに接続する
# conn = sqlite3.connect('test.db')
# c = conn.cursor()

# データを追加する
def add_data(date, kind1, kind2, kind3, name, person, pay_option, money):
    # データベースに接続する
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # データベースにテーブルを作成する
    c.execute('CREATE TABLE IF NOT EXISTS spending (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, kind1 TEXT, kind2 TEXT, kind3 TEXT, name TEXT, person TEXT, pay_option TEXT, money INTEGER)')
    #INSERT
    c.execute('INSERT INTO spending (date,kind1,kind2,kind3,name,person,pay_option,money) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (date, kind1, kind2, kind3, name, person, pay_option,money))
    conn.commit()
    st.balloons()
    st.write('データが追加されました。')
    # データベースをクローズする
    conn.close()


# 全てのデータを表示する
def show_all_data():
    # データベースに接続する
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS spending (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, kind1 TEXT, kind2 TEXT, kind3 TEXT, name TEXT, person TEXT, pay_option TEXT, money INTEGER)')
    c.execute('SELECT date(date),kind1,kind2,kind3,name,person,pay_option,money FROM spending ORDER BY date(date)')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=('日付','大分類','中分類','小分類','詳細名','払った人','支払い方法','金額'))
    # データベースをクローズする
    conn.close()

    return df

def show_sum_data():
    # データベースに接続する
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS spending (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, kind1 TEXT, kind2 TEXT, kind3 TEXT, name TEXT, person TEXT, pay_option TEXT, money INTEGER)')
    c.execute('SELECT substr(date,1,7),kind1,kind2,kind3,sum(money) FROM spending GROUP BY substr(date,1,7),kind1,kind2,kind3')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=('年月','大分類','中分類','小分類','金額'))
    # データベースをクローズする
    conn.close()

    return df



