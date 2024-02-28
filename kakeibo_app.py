import streamlit as st
import data
import const
import datetime
import re
import altair as alt
import pandas as pd
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
##selected = option_menu(**const.OPTION_MENU_CONFIG)

st.title('家計簿アプリ')
tab1, tab2, tab3, tab4 = st.tabs(["支出入力", "収入入力", "一覧表", "分析"])
all_type = ['家賃','電気','ガス','水道',
                                 'おそとあそび費','おうちあそび費','外食費',
                                 'カフェ費','日用品費','スーパー費','コンビニ費',
                                 '通信費','ひとりごはん費','交通費',
                                 '服費','美容費','勉強費','必須費','娯楽費','積立NISA']
with tab1:
    st.write('### 支出入力')

    # データの追加
    today = datetime.datetime.now()
    date = st.date_input("日付：", today)
    col1,col2= st.columns(2)

    kind1 = col1.selectbox(
    "費目1：",
    ("ふたり費", "あやたん費", "だいすけ費")
    )
    

    kind2_taple=()
    if kind1=='ふたり費' :
        kind2_taple=('家賃','電気','ガス','水道','おそとあそび費','おうちあそび費','外食費','カフェ費','日用品費','スーパー費','コンビニ費')
    elif kind1 in('あやたん費','だいすけ費') :
        kind2_taple=('通信費','ひとりごはん費','交通費','服費','美容費','勉強費','必須費','娯楽費','積立NISA')
    kind2 = col2.selectbox(
    "費目2：",
    kind2_taple
    )
    
    person =col1.radio('払った人：',('あやたん','だいすけ'),horizontal=True)

    pay_option = col2.selectbox(
        '支払い方法：',
        ('カード','現金','ポイント','PayPay'))
    name = st.text_input('詳細名：')
    money = st.number_input('金額：',0)
    if st.button('支出追加',type="primary"):
        data.add_data(date, kind1, kind2, name, person, pay_option, money)


with tab2:
    st.write('### 収入入力')
    ym_date = ("{}/{:02}".format(y,m) for y in range(2024,2050) for m in range(1,13))
    income_date = st.selectbox('振り込まれた年月：',ym_date)
    col2_1,col2_2=st.columns(2)
    income_person = col2_1.radio('稼いだ人：',('あやたん','だいすけ'),horizontal=True)
    type = col2_2.selectbox('分類:',('給料','贈与'))
    memo = st.text_area('メモ：')
    in_money = st.number_input('金額',0)
    if st.button('収入追加',type="primary"):
        data.add_data(date, kind1, kind2, name, person, pay_option, money)


with tab3:
    st.write('### 一覧表')
    search_all = st.multiselect('分類名',all_type,default=all_type)
    date = ("{}/{:02}".format(y,m) for y in range(2024,2050) for m in range(1,13))
    search_month=st.selectbox('年月：',date)
    search_month = re.sub(r'/', '', search_month)  # "/"を削除
    #year_month = "".join(date.split("-")[:2])
    df = data.show_all_data()
    df = df[(df["費目2"].isin(search_all))]
    df = df.loc[df["日付"].str.replace("-", "").str.startswith(search_month)]
    #df = df["".join(df["日付"].split("-")[:2])==search_month]
    st.dataframe(df,use_container_width=True, hide_index=True)

with tab4:
    st.write('### 分析')
    #年月、費目別の表
    df = data.show_sum_data()
    df = df.pivot_table(index=['費目1', '費目2'], columns='年月', values='金額', aggfunc='first')
    df = df.fillna(0)
    st.write('ふたり費')
    df_two = df.loc[df.index.get_level_values('費目1') == 'ふたり費']
    df_two.reset_index(level='費目1', inplace=True)
    df_two = df_two.drop(columns=['費目1'])
    st.dataframe(df_two,use_container_width=True)
    st.write('支出推移グラフ')
    df_two_2 = df_two.T.reset_index()
    # データフレームを積み上げ形式に変換
    df_melted = df_two_2.melt(id_vars=["年月"], var_name="支出項目", value_name="金額")
    # 積み上げ棒グラフを作成
    chart = alt.Chart(df_melted).mark_bar().encode(
    x='年月',
    y='金額',
    color=alt.Color(
            "支出項目",
            scale=alt.Scale(
                range=["#FF9999","#99FF99","#9999FF","#FFCC66","#FF99CC","#99CCFF","#CC99FF","#66CCCC","#FFFF99","#FF99CC","#99FFCC"]
            )),
    tooltip=['年月', '支出項目', '金額']
    ).properties(
    width=500
    )
    st.altair_chart(chart,use_container_width=True)

    


    st.write('あやたん費')
    df_aya = df.loc[df.index.get_level_values('費目1') == 'あやたん費']
    df_aya.reset_index(level='費目1', inplace=True)
    df_aya = df_aya.drop(columns=['費目1'])
    st.dataframe(df_aya,use_container_width=True)

    st.write('だいすけ費')
    df_dai = df.loc[df.index.get_level_values('費目1') == 'だいすけ費']
    df_dai.reset_index(level='費目1', inplace=True)
    df_dai = df_dai.drop(columns=['費目1'])
    st.dataframe(df_dai,use_container_width=True)
