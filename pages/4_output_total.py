#요구 문서 출력 페이지
import streamlit as st
import base64

def load_text(filename):
    with open(f"txt/{filename}", "r", encoding="utf-8") as file:
        return file.read()

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

# 기술문서 조건용 Y/N 값 가져오기
q1 = st.session_state.get("q1", "선택 안됨")
q2 = st.session_state.get("q2", "선택 안됨")
q3 = st.session_state.get("q3", "선택 안됨")
q4 = st.session_state.get("q4", "선택 안됨")
q5 = st.session_state.get("q5", "선택 안됨")

if grade:
    st.subheader(f"📍 선택된 등급: {grade}")
    
    if grade == 1:
        st.success("❗제출 서류: 신고서")
        show_pdf_download("신고서 pdf", "pdf/[별지 제3호서식] 의료기기 제조(수입) 허가신청서(의료기기법 시행규칙).pdf")
    else:
        st.success("제출 서류:")
        st.markdown("- 인증신청서")
        st.markdown("- GMP 적합인정서")
        st.markdown("- 기술문서")

        st.divider()

        st.subheader("❗인증신청서:")
        st.markdown("[의료기기법 시행규칙]")
        show_pdf_download("인증신청서 pdf", "pdf/[별지 제3호서식] 의료기기 제조(수입) 허가신청서(의료기기법 시행규칙).pdf")
        
        st.subheader("❗GMP 적합인정서:")
        st.markdown("[의료기기 제조 및 품질관리 기준] 제7조 기반 자료")
        content_GMP = load_text("GMP.txt").replace("\t", "    ")
        st.code(content_GMP, language="text")
        show_pdf_download("GMP 적합인정서 pdf", "pdf/의료기기 적합성인정등 심사 신청서(GMP).pdf")

        st.subheader("❗기술문서:")
        st.markdown("[의료기기 허가ㆍ신고ㆍ심사 등에 관한 규정] 제26조, 제 29조 기반 자료")
        content_td = load_text("기술문서.txt").replace("\t", "    ")
        st.code(content_td, language="text")
        if q1 == "Yes":
            st.text("❕ 전기ㆍ기계적 안전에 관한 자료")
            content_s1 = load_text("전기ㆍ기계적 안전에 관한 자료.txt").replace("\t", "    ")
            st.code(content_s1, language="text")
        if q2 == "Yes":
            st.text("❕ 생물학적 안전에 관한 자료")
            content_s2 = load_text("생물학적 안전에 관한 자료.txt").replace("\t", "    ")
            st.code(content_s2, language="text")
        if q3 == "Yes":
            st.text("❕ 방사선에 관한 안전성 자료")
            content_3 = load_text("방사선에 관한 안전성 자료.txt").replace("\t", "    ")
            st.code(content_3, language="text")
        if q4 == "Yes":
            st.text("❕ 전자파 안전에 관한 자료")
            content_4 = load_text("전자파안전에 관한 자료.txt").replace("\t", "    ")
            st.code(content_4, language="text")
        st.text("❕ 성능에 관한 자료")
        content_s5 = load_text("성능에 관한 자료.txt").replace("\t", "    ")
        st.code(content_s5, language="text")
        if q5 == "Yes":
            st.text("❕ 물리ㆍ화학적 특성에 관한 자료")
            content_s6 = load_text("물리ㆍ화학적 특성에 관한 자료.txt").replace("\t", "    ")
            st.code(content_s6, language="text")
        st.text("❕ 안전성에 관한 자료")
        content_s6 = load_text("안정성에 관한 자료.txt").replace("\t", "    ")
        st.code(content_s6, language="text")
        content_td2 = load_text("기술문서_2.txt").replace("\t", "    ")
        st.code(content_td2, language="text")
        
        st.markdown("❕별지 및 별표")
        show_pdf_download("[별지 제3호 서식] pdf", "pdf/[별지 3] 본질적 동등품목비교표.pdf")
        if q2 == "Yes":
            show_pdf_download("[별표 2] pdf", "pdf/[별표 2] 멸균의료기기의 멸균방법(제11조제1항제1호 관련).pdf")
        show_pdf_download("[별표 13] pdf", "pdf/[별표 13] 의료기기 소프트웨어 적합성 확인보고서 작성방법(제29조제8호 관련).pdf")
        show_pdf_download("[별지 제 13호 서식] pdf", "pdf/[별지 13] 의료기기 소프트웨어 적합성 확인보고서.pdf")
        show_pdf_download("[별표 3] pdf", "pdf/[별표 3] 경미한 변경사항(제19조 관련).pdf")
        show_pdf_download("[별표 12] pdf", "pdf/[별표 12] 생물학적 안전에 관한 자료 제출범위(제26조제2항 관련).pdf")
        show_pdf_download("[별표 16] pdf", "pdf/[별표 16] 첨부자료 제출 요약표(제29조제2항 관련).pdf")

else:
    st.warning("등급 정보가 없어 안내를 진행할 수 없습니다.")