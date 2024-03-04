import streamlit as st
import sqlite3
import pandas as pd
import numpy as np

# データベースに接続する
# conn = sqlite3.connect('test.db')
# c = conn.cursor()

# 支出データを追加する
def add_data(date, kind1, kind2, name, person, pay_option, money):
    # データベースに接続する
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # データベースにテーブルを作成する
    c.execute('CREATE TABLE IF NOT EXISTS spending_test (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, kind1 TEXT, kind2 TEXT, name TEXT, person TEXT, pay_option TEXT, money INTEGER)')
    #INSERT
    c.execute('INSERT INTO spending_test (date,kind1,kind2,name,person,pay_option,money) VALUES (?, ?, ?, ?, ?, ?, ?)', (date, kind1, kind2, name, person, pay_option,money))
    conn.commit()
    st.balloons()
    st.write('データが追加されました。')
    # データベースをクローズする
    conn.close()

#収入データを追加する
def add_income(ymdate,person,type,memo,money):
    # データベースに接続する
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # データベースにテーブルを作成する
    c.execute('CREATE TABLE IF NOT EXISTS income_test (id INTEGER PRIMARY KEY AUTOINCREMENT, ymdate TEXT, person TEXT, type TEXT, memo TEXT, money INTEGER)')
    #INSERT
    c.execute('INSERT INTO income_test (ymdate,person,type,memo,money) VALUES (?, ?, ?, ?, ?)', (ymdate,person,type,memo,money))
    conn.commit()
    st.balloons()
    st.write('データが追加されました。')
    # データベースをクローズする
    conn.close()

# 全てのデータを表示する
def show_all_data():
    # データベースに接続する
    # kinds = ",".join(kinds)
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS spending_test (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, kind1 TEXT, kind2 TEXT, name TEXT, person TEXT, pay_option TEXT, money INTEGER)')
    c.execute('SELECT date(date),kind1,kind2,name,person,pay_option,money FROM spending_test ORDER BY date(date)')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=('日付','費目1','費目2','詳細名','払った人','支払い方法','金額'))
    # データベースをクローズする
    conn.close()

    return df

#費目ごとの合計を表示する
def show_sum_data():
    # データベースに接続する
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS spending_test (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, kind1 TEXT, kind2 TEXT, name TEXT, person TEXT, pay_option TEXT, money INTEGER)')
    c.execute('SELECT substr(date,1,7),kind1,kind2,sum(money) FROM spending_test GROUP BY substr(date,1,7),kind1,kind2')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=('年月','費目1','費目2','金額'))
    # データベースをクローズする
    conn.close()

    return df



