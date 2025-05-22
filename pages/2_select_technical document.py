import streamlit as st

st.title("📌 기술적 특성 선택지")

q1 = st.radio("1. 전기를 사용하나요?", ("Yes", "No"))
q2 = st.radio("2. 인체에 접촉 또는 주입되나요?", ("Yes", "No"))
q3 = st.radio("3. 방사선을 이용하거나 노출되나요?", ("Yes", "No"))
q4 = st.radio("4. 전자파 안전성이 요구되나요?", ("Yes", "No"))
q5 = st.radio("5. 혈액, 체액 또는 약물과 접촉하나요?", ("Yes", "No"))

if st.button("다음 단계로 이동"):
    st.session_state['q1'] = q1
    st.session_state['q2'] = q2
    st.session_state['q3'] = q3
    st.session_state['q4'] = q4
    st.session_state['q5'] = q5

    st.switch_page("pages/3_output_document.py")
