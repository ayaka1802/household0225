import streamlit as st
import data
import const
import datetime
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)

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
