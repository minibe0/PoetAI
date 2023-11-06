from dotenv import load_dotenv
load_dotenv()




# complete 
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은")
# print(result)

# chat_model = ChatOpenAI()
# llm.predict("hi")
# chat_model.predict("hi!")

import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

st.title('GeneratedAI for Poet')

content = st.text_input('시의 주제를 입력하세요')

chat_model = ChatOpenAI()   

if st.button('시 작성 요청'):
   with st.spinner('시 작성 중...'):
    result = chat_model.predict(content + "에 대한 시를 써 줘")
    st.write(result)

# # 2.ChatOpenAI 모델을 초기화합니다.
# chat_model = ChatOpenAI()

# content = "코딩"

# result = chat_model.predict(content + "에 대한 시를 써 줘")
# print(result)