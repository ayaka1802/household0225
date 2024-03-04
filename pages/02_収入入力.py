import streamlit as st
import data
import const
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)

st.write('### 収入入力')
ym_date = ("{}/{:02}".format(y,m) for y in range(2024,2050) for m in range(1,13))
income_date = st.selectbox('振り込まれた年月：',ym_date)
col2_1,col2_2=st.columns(2)
income_person = col2_1.radio('稼いだ人：',('あやたん','だいすけ'),horizontal=True)
type = col2_2.selectbox('分類:',('給料','贈与'))
memo = st.text_area('メモ：')
in_money = st.number_input('金額',0)
if st.button('収入追加',type="primary"):
    data.add_income(income_date,income_person,type,memo,in_money)