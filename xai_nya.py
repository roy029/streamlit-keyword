import streamlit as st

tweet = [
    "旅行に行ったら、土産にインフルもらってきた。",
    "インフル感染の危機。"
]
n = len(tweet)
tweet_and_drop = {
    "旅行に行ったら、土産にインフルもらってきた。": f'旅行に行ったら<span style="color:blue">{"土産に"}</span><span style="color:red">{"インフル"}</span>もらってきた。',
    "インフル感染の危機。": f'<span style="color:blue">{"インフル"}</span>感染の<span style="color:red">{"危機"}</span>。'
}

with st.form("input_form", clear_on_submit=False):
    series = st.selectbox(label='ツイートを選択してください', options=[tweet[i] for i in range(n)])
    submitted = st.form_submit_button("学習結果を表示") 
     
if submitted:
    text = tweet_and_drop[series]
    st.write(text, unsafe_allow_html=True)
