import streamlit as st
import const
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
##selected = option_menu(**const.OPTION_MENU_CONFIG)

st.title('家計簿アプリ')

