import streamlit as st
import const
from llm import llm_response
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
##selected = option_menu(**const.OPTION_MENU_CONFIG)

st.title('家計簿アプリ')
if st.session_state.get("chat_messages") is None:
    st.session_state["chat_messages"] = []

st.write("### おしゃべりのコーナー")

for message in st.session_state["chat_messages"]:
    st.chat_message(message["role"]).write(message["content"])

if message := st.chat_input("ここにかいてね"):
    st.chat_message("user").write(message)
    st.session_state["chat_messages"].append({"role": "user", "content": message})

    ai_response = llm_response(st.session_state["chat_messages"])
    st.chat_message("assistant").write(ai_response)
    st.session_state["chat_messages"].append({"role": "assistant", "content": ai_response})

