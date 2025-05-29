import streamlit as st

st.title("📌 최종 등급 및 입력 내용")

# 등급 표시
grade = st.session_state.get("grade", "정보 없음")

st.subheader("📍 등급")
st.write(f"등급: **{grade}**")

# 질문 목록
questions = {
    "q1": "1. 전기를 사용하나요?",
    "q2": "2. 인체에 접촉 또는 주입되나요?",
    "q3": "3. 방사선을 이용하거나 노출되나요?",
    "q4": "4. 전자파 안전성이 요구되나요?",
    "q5": "5. 혈액, 체액 또는 약물과 접촉하나요?",
}

# 응답 출력
st.subheader("📍 추가 질문 응답")
for key, question in questions.items():
    answer = st.session_state.get(key, "선택 안됨")
    st.markdown(f"{question} → **{answer}**")

# 페이지 이동
if st.button("다음 단계로 이동"):
    st.success("다음 페이지로 이동합니다.")
    st.switch_page("pages/4_output_total.py")