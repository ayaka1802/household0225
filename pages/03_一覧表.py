import streamlit as st
import data
import const
import re
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)
all_type = ['家賃','電気','ガス','水道',
                                 'おそとあそび費','おうちあそび費','外食費',
                                 'カフェ費','日用品費','スーパー費','コンビニ費',
                                 '通信費','ひとりごはん費','交通費',
                                 '服費','美容費','勉強費','必須費','娯楽費','積立NISA']
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