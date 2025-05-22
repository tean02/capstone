import streamlit as st
import pandas as pd
import openpyxl

st.title("📌 의료기기 등급 탐색기")

df = pd.read_excel("data/의료기기 품목 및 품목별 등급에 관한 규정.xlsx")
df.columns = df.columns.str.strip()

df['중분류코드'] = df['넘버'].astype(str).str[:3]
df['중분류코드'] = df.apply(
    lambda row: row['넘버'][:4] if row['넘버'].startswith("A155") else row['넘버'][:3],
    axis=1
)

category_name_map = {
    "A": "기구·기계 Medical Instruments",
    "B": "의료용품 Medical Supplies",
    "C": "치과재료 Dental Materials",
    "E": "소프트웨어 Software as a Medical Device",
    "I": "검체 전처리 기기 Devices for Sample Preparation",
    "J": "임상화학 검사기기 Devices for Clinical Chemistry",
    "K": "면역 검사기기 Devices for Clinical Immunology",
    "L": "수혈의학 검사기기 Devices for Blood Transfusion",
    "M": "임상미생물 검사기기 Devices for Clinical Microbiology",
    "N": "분자진단기기 Devices for Molecular Diagnostics",
    "O": "조직병리 검사기기 Devices for Immuno Cyto/Histo Chemistry",
    "P": "체외진단 소프트웨어 IVD Software",
}

available_categories = sorted(df['분류'].dropna().unique())
category_display_list = [
    f"{code} - {category_name_map.get(code, '')}" for code in available_categories
]

selected_category_display = st.selectbox("대분류 선택", category_display_list)

category = selected_category_display.split(" - ")[0]

available_middle_codes = sorted(
    df[df['분류'] == category]['중분류코드'].dropna().unique()
)

# 중분류 이름 매핑 (대표 이름: 첫 항목 기준)
middle_name_map = (
    df.groupby('중분류코드')['이름']
    .first()
    .to_dict()
)

middle_display_list = []
for code in available_middle_codes:
    if code == "A155":
        display_code = f"{code}00"
    else:
        display_code = f"{code}000"
    middle_display_list.append(f"{display_code} - {middle_name_map.get(code, '')}")

# 중분류 코드 선택
selected_middle_display = st.selectbox("중분류 선택", middle_display_list)

# 코드만 분리
if "A155" in selected_middle_display:
    selected_middle_code = "A155"
else:
    selected_middle_code = selected_middle_display.split("00")[0]

# 중분류 필터링 (앞 4자리 기준)
filtered_df = df[
    (df['분류'] == category) &
    (df['넘버'].astype(str).str.startswith(selected_middle_code))
]

search_query = st.text_input("검색어로 항목 필터링")

if search_query:
    filtered_df = filtered_df[filtered_df['이름'].str.contains(search_query, case=False, na=False)]


if not filtered_df.empty:
    # 표시 문자열 생성
    filtered_df['표시'] = filtered_df.apply(
        lambda row: f"{row['넘버']} | {row['이름']} | {row['영문명']} | {row['설명']}", axis=1
    )

    selected_item = st.selectbox("항목 선택", filtered_df['표시'])

    selected_row = filtered_df[filtered_df['표시'] == selected_item].iloc[0]
    st.success(f"등급: {selected_row['등급']}")
    st.session_state['등급'] = selected_row['등급']
else:
    st.warning("해당 중분류에 해당하는 항목이 없습니다.")

st.session_state['grade'] = selected_row['등급']

# 다음 페이지로 이동
if st.button("다음 단계로 이동"):
    st.success("다음 페이지로 이동합니다.")
    st.switch_page("pages/2_select_technical document.py") 