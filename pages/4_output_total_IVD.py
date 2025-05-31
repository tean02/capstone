import streamlit as st

# 파일 읽기 함수
def load_text(filename):
    with open(f"txt_IVD/{filename}", "r", encoding="utf-8") as file:
        return file.read().replace("\t", "    ")

# PDF 다운로드 버튼 함수
def show_pdf_download(label, file_path):
    with open(file_path, "rb") as f:
        st.download_button(
            label=f"{label} 다운로드",
            data=f,
            file_name=file_path.split("/")[-1],
            mime="application/pdf_IVD"
        )

st.header("📌 맞춤 요구서류 목록")

grade = st.session_state.get("grade", None)
ivd_type = st.session_state.get('ivd_type')

# 등급 확인
st.subheader(f"📍 선택된 등급: {grade}")

if grade == 1:
    st.success("❗제출 서류: 신고서")
    st.markdown("[체외진단의료기기법 시행규칙]")
    show_pdf_download("신고서", "pdf_IVD/[별지 제5호서식] 체외진단의료기기 제조(수입) 인증신청서(체외진단의료기기법 시행규칙).pdf")

else:
    st.success("제출 서류:")
    st.markdown("- 인증신청서\n- GMP 적합인정서\n- 기술문서")
    st.divider()

    # 인증신청서
    st.subheader("❗인증신청서:")
    st.markdown("[체외진단의료기기법 시행규칙]")
    show_pdf_download("신고서", "pdf_IVD/[별지 제5호서식] 체외진단의료기기 제조(수입) 인증신청서(체외진단의료기기법 시행규칙).pdf")

    # GMP
    st.subheader("❗GMP 적합인정서:")
    st.markdown("[체외진단의료기기 제조 및 품질관리 기준] 제7조 기반 자료")
    st.code(load_text("GMP_IVD.txt"), language="text")
    show_pdf_download("GMP 적합인정서", "pdf_IVD/[별지 1] 체외진단의료기기 적합성인정등 심사 신청서(체외진단의료기기 제조 및 품질관리 기준).pdf")
    show_pdf_download("[별표 1] 용어의 정의", "pdf_IVD/[별표 1] 용어의 정의(체외진단의료기기 제조 및 품질관리 기준).pdf")
    show_pdf_download("[별표 2] 체외진단의료기기 적합성인정등 심사기준준", "pdf_IVD/[별표 2] 체외진단의료기기 적합성인정등 심사 기준(체외진단의료기기 제조 및 품질관리 기준).pdf")

    # 기술문서
    st.subheader("❗기술문서:")
    st.markdown("[체외진단의료기기 허가ㆍ신고ㆍ심사 등에 관한 규정] 제25조, 제27조 기반 자료")
    
    if ivd_type == '체외진단시약':
        st.code(load_text("기술문서(진단시약)_IVD.txt"), language="text")
        show_pdf_download("[별지 2] 체외진단시약의 본질적 동등품목 비교표", "pdf_IVD/[별지 2] 체외진단시약의 본질적 동등품목 비교표(체외진단의료기기 허가·신고·심사 등에 관한 규정).pdf")

    elif ivd_type == '체외진단장비':
        st.code(load_text("기술문서(진단장비)_IVD.txt"), language="text")

        # 체외진단장비 기술문서 조건 질문
        questions_IVD = {
        "q1_IVD": ("전기ㆍ기계적 안전에 관한 자료", "전기ㆍ기계적 안전에 관한 자료_IVD.txt"),
        "q2_IVD": ("방사선에 관한 안전성 자료", "방사선에 관한 안전성 자료_IVD.txt"),
        "q3_IVD": ("전자파안전에 관한 자료", "전자파안전에 관한 자료_IVD.txt"),
        }
        
        # 조건부 자료
        for key, (label, filename) in questions_IVD.items():
            if st.session_state.get(key) == "Yes":
                st.text(f"❕ {label}")
                st.code(load_text(filename), language="text")

        # 공통 기술자료
        st.text("❕ 성능에 관한 자료")
        st.code(load_text("성능에 관한 자료_IVD.txt"), language="text")
        st.code(load_text("기술문서(진단장비)_2_IVD.txt"), language="text")

        # 별지/별표 다운로드
        st.markdown("❕별지 및 별표")

        if st.session_state.get("q2_IVD") == "Yes":
            show_pdf_download("[별표 2] 멸균 체외진단의료기기의 멸균균방법", "pdf_IVD/[별표 2] 멸균 체외진단의료기기의 멸균방법(제10조제1항 관련)(체외진단의료기기 허가·신고·심사 등에 관한 규정).pdf")

        pdf_files = [
            ("[별표 9] 체외진단의료기기(소프트웨어) 적합성 확인보고서 작성방법", "pdf_IVD/[별표 9] 체외진단의료기기(소프트웨어) 적합성 확인보고서 작성방법(제27조 관련)(체외진단의료기기 허가·신고·심사 등에 관한 규정).pdf"),
            ("[별지 11] 체외진단장비(소프트웨어) 적합성 확인보고서", "pdf_IVD/[별지 11] 체외진단장비(소프트웨어) 적합성 확인보고서(체외진단의료기기 허가·신고·심사 등에 관한 규정).pdf"),
            ]
        
        for label, path in pdf_files:
            show_pdf_download(label, path)