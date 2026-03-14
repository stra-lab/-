import streamlit as st
from openai import OpenAI
from app import system_prompt


def translation_process(trans:str,language:str)->str:
    system_prompt='你是一个专业的翻译助手，擅长给出信达雅的翻译'
    client = OpenAI(base_url='https://api.deepseek.com', api_key='sk-12c135c39ba340639866679b20cb5fb1')
    language=f'把这句话翻译成{language}:{trans}'
    stream = client.chat.completions.create(
        model='deepseek-chat',
        temperature=0.2,
        max_tokens=1024,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': language}
        ]
    )
    return stream.choices[0].message.content

st.write('## 多语言翻译助手')
col1,col2=st.columns([4,1])
with st.sidebar:
    st.title("语种设置")
    choose_language = st.radio(label="请选择要翻译的语种", options=["英语", "日语", "俄语", "西班牙语"])

with col1:
    choose_trans=st.text_input(label='请输入要翻译的句子:')
with col2:
    button=st.button('确定',type='primary')
if button:
    if choose_trans.strip() != "":
        with st.spinner("翻译中..."):
            result = translation_process(choose_trans, choose_language)
        st.success("翻译结果：")
        st.write(f"### {result}")
