import streamlit as st
import const
from llm import aya_response,dai_response
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
##selected = option_menu(**const.OPTION_MENU_CONFIG)

st.write("### おしゃべりのコーナー")

person = st.radio(
    "誰とおしゃべりする？",
    ["あやたん", "だいすけ"]
)
USER_NAME = "user"
AYA_NAME = "ayatan"
DAI_NAME = "daisuke"
avator_img_dict = {
    AYA_NAME: "👧",
    DAI_NAME: "🐤"
}
if st.session_state.get("chat_messages") is None:
    st.session_state["chat_messages"] = []

for message in st.session_state["chat_messages"]:
    st.chat_message(message["name"]).write(message["content"])

if message := st.chat_input("ここにかいてね"):
    st.chat_message("user").write(message)
    st.session_state["chat_messages"].append({"name": USER_NAME, "content": message})

    if(person=='あやたん'):
        ai_response = aya_response(st.session_state["chat_messages"])
        st.chat_message(AYA_NAME,avatar=avator_img_dict[AYA_NAME]).write(ai_response)
        st.session_state["chat_messages"].append({"name": AYA_NAME, "content": ai_response})
    elif(person=='だいすけ'):
        ai_response = dai_response(st.session_state["chat_messages"])
        st.chat_message(DAI_NAME,avatar=avator_img_dict[DAI_NAME]).write(ai_response)
        st.session_state["chat_messages"].append({"name": DAI_NAME, "content": ai_response})

