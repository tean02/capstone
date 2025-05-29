import streamlit as st

# 파일 읽기 함수
def load_text(filename):
    with open(f"txt/{filename}", "r", encoding="utf-8") as file:
        return file.read().replace("\t", "    ")

# PDF 다운로드 버튼 함수
def show_pdf_download(label, file_path):
    with open(file_path, "rb") as f:
        st.download_button(
            label=f"{label} 다운로드",
            data=f,
            file_name=file_path.split("/")[-1],
            mime="application/pdf"
        )

st.header("📌 맞춤 요구서류 목록")

grade = st.session_state.get("grade", None)

# 기술문서 조건 질문
questions = {
    "q1": ("전기ㆍ기계적 안전에 관한 자료", "전기ㆍ기계적 안전에 관한 자료.txt"),
    "q2": ("생물학적 안전에 관한 자료", "생물학적 안전에 관한 자료.txt"),
    "q3": ("방사선 안전성 자료", "방사선에 관한 안전성 자료.txt"),
    "q4": ("전자파 안전성 자료", "전자파안전에 관한 자료.txt"),
    "q5": ("물리ㆍ화학적 특성 자료", "물리ㆍ화학적 특성에 관한 자료.txt"),
}

# 등급 확인
if grade:
    st.subheader(f"📍 선택된 등급: {grade}")

    if grade == 1:
        st.success("❗제출 서류: 신고서")
        show_pdf_download("신고서", "pdf/[별지 제3호서식] 의료기기 제조(수입) 허가신청서(의료기기법 시행규칙).pdf")

    else:
        st.success("제출 서류:")
        st.markdown("- 인증신청서\n- GMP 적합인정서\n- 기술문서")
        st.divider()

        # 인증신청서
        st.subheader("❗인증신청서:")
        st.markdown("[의료기기법 시행규칙]")
        show_pdf_download("인증신청서", "pdf/[별지 제3호서식] 의료기기 제조(수입) 허가신청서(의료기기법 시행규칙).pdf")

        # GMP
        st.subheader("❗GMP 적합인정서:")
        st.markdown("[의료기기 제조 및 품질관리 기준] 제7조 기반 자료")
        st.code(load_text("GMP.txt"), language="text")
        show_pdf_download("GMP 적합인정서", "pdf/의료기기 적합성인정등 심사 신청서(GMP).pdf")

        # 기술문서
        st.subheader("❗기술문서:")
        st.markdown("[의료기기 허가ㆍ신고ㆍ심사 등에 관한 규정] 제26조, 제29조 기반 자료")
        st.code(load_text("기술문서.txt"), language="text")

        # 조건부 자료
        for key, (label, filename) in questions.items():
            if st.session_state.get(key) == "Yes":
                st.text(f"❕ {label}")
                st.code(load_text(filename), language="text")

        # 공통 기술자료
        st.text("❕ 성능에 관한 자료")
        st.code(load_text("성능에 관한 자료.txt"), language="text")
        st.text("❕ 안전성에 관한 자료")
        st.code(load_text("안정성에 관한 자료.txt"), language="text")
        st.code(load_text("기술문서_2.txt"), language="text")

        # 별지/별표 다운로드
        st.markdown("❕별지 및 별표")
        pdf_files = [
            ("[별지 3] 본질적 동등품목비교표", "pdf/[별지 3] 본질적 동등품목비교표.pdf"),
            ("[별표 13] 소프트웨어 적합성 확인보고서 작성방법", "pdf/[별표 13] 의료기기 소프트웨어 적합성 확인보고서 작성방법(제29조제8호 관련).pdf"),
            ("[별지 13] 소프트웨어 적합성 확인보고서", "pdf/[별지 13] 의료기기 소프트웨어 적합성 확인보고서.pdf"),
            ("[별표 3] 경미한 변경사항", "pdf/[별표 3] 경미한 변경사항(제19조 관련).pdf"),
            ("[별표 12] 생물학적 안전 제출범위", "pdf/[별표 12] 생물학적 안전에 관한 자료 제출범위(제26조제2항 관련).pdf"),
            ("[별표 16] 첨부자료 제출 요약표", "pdf/[별표 16] 첨부자료 제출 요약표(제29조제2항 관련).pdf"),
        ]
        for label, path in pdf_files:
            show_pdf_download(label, path)

        # q2 조건에 따른 추가 PDF
        if st.session_state.get("q2") == "Yes":
            show_pdf_download("[별표 2] 멸균방법", "pdf/[별표 2] 멸균의료기기의 멸균방법(제11조제1항제1호 관련).pdf")
else:
    st.warning("등급 정보가 없어 안내를 진행할 수 없습니다.")