import streamlit as st
import data
import const
import altair as alt
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
st.write('### 支出分析')
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
chart = chart.configure_legend(orient='bottom')
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