## streamlit 라이브러리를 반드시 호출해야 streamlit에서 제공하는 기능들을 활용할 수 있음!
## 앞으로 streamlit 라이브러리의 기능을 사용하기 위해선 항상 streamlit.{기능명} 이런식으로 호출해야 하나, 너무 길기에 st로 줄일 것임을 미리 명시해두기.
import streamlit as st
from utilities.llm import get_basic_response, get_revised_response

# st.title('제목') <- 웹 상단에 나타날 이름.
st.title("ChatBot")

# streamlit은 session_state 를 상태 저장 용 딕셔너리로 사용함. 웹이 안정적으로 구동하기 위해선 session_state에 상호작용 내역을 저장해 둘 필요가 있음.
# st.session_state.{딕셔너리이름} = []  <- 웹에서 나타난 상호작용을 저장하는 용도
if "messages" not in st.session_state:
    st.session_state.messages = []

# session_state.messages에 message (이전 기록)이 있는 경우, 이를 마크다운 형태로 나타냄.
# 현재 message는 {'role': "user/assistant", "content": "내용"} 형태로 저장되고 있음.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])  # <- 웹에 나타내기

# userchat이라는 변수에 st.chat_input 함수를 통해 유저가 입력한 내용을 저장할 것임.
# st.chat_input("placeholder") <- placeholder는 입력창에 아무 것도 입력되지 않은 경우에만 보여지는 지시문임.
userchat = st.chat_input("What is up?")
if userchat:
    st.chat_message("user").markdown(userchat)  # <- 웹에 유저가 입력한 내용 나타내기
    st.session_state.messages.append({"role": "user", "content": userchat})  # <- session_state에 대화 내용 저장하기

    # response라는 변수에 assistant의 대답을 저장함. 아직 API가 연결되지 않았기에, 유저의 입력을 반복하는 따라쟁이 챗봇을 구현함.
    response = f"Echo: {userchat}"
    with st.chat_message("assistant"):
        st.markdown(response) # <- 웹에 assistant가 입력한 내용 나타내기

    st.session_state.messages.append({"role": "assistant", "content": response})  # <- session_state에 대화 내용 저장하기
