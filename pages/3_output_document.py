# 선택지에 따른 요구 문서 정보 제공
import streamlit as st

st.title("📌 최종 등급 및 입력 내용")

grade = st.session_state.get("등급", "정보 없음")

q1 = st.session_state.get("q1", "선택 안됨")
q2 = st.session_state.get("q2", "선택 안됨")
q3 = st.session_state.get("q3", "선택 안됨")
q4 = st.session_state.get("q4", "선택 안됨")
q5 = st.session_state.get("q5", "선택 안됨")

st.subheader("📍 등급")
st.write(f"등급: **{grade}**")

st.subheader("📍 추가 질문 응답")
st.markdown(f"""
1. 전기를 사용하나요? → **{q1}**  
2. 인체에 접촉, 삽입되거나 인체에 주입하는 혈액, 체액 또는 약물 등과 접촉하나요? → **{q2}**  
3. 방사선을 이용하거나 방사선에 노축되나요? → **{q3}**  
4. 전자파 안전성이 요구되나요? → **{q4}**  
5. 인체에 접촉, 삽입되거나 인체에 주입하는 혈액, 체액 또는 약물 등과 접촉하나요? → **{q5}**
""")

if st.button("다음 단계로 이동"):
    st.success("다음 페이지로 이동합니다.")
    st.switch_page("pages/4_output_total.py")