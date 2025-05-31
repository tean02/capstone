import streamlit as st
import pandas as pd

st.title("📌 의료기기 등급 탐색기")

@st.cache_data
def load_data():
    df = pd.read_excel("data/의료기기 품목 및 품목별 등급에 관한 규정.xlsx")
    df.columns = df.columns.str.strip()

    # 중분류 코드 생성
    df['중분류코드'] = df['넘버'].astype(str).apply(
        lambda x: x[:4] if x.startswith("A155") else x[:3]
    )
    return df

@st.cache_data
def load_middle_names():
    middle_df = pd.read_excel("data/중분류 이름.xlsx")
    middle_df['중분류코드'] = middle_df['코드'].astype(str).apply(
        lambda x: x[:4] if x.startswith("A155") else x[:3]
    )
    return dict(zip(middle_df['중분류코드'], middle_df['이름']))

@st.cache_data
def get_category_names():
    return {
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

def format_middle_display(code, name):
    if code.startswith("A155"):
        return f"{code}00 - {name}"
    return f"{code}000 - {name}"

# 1. 데이터 불러오기
df = load_data()
middle_name_map = load_middle_names()
category_name_map = get_category_names()

# 2. 대분류 선택
available_categories = sorted(df['분류'].dropna().unique())
category_display_list = [
    f"{code} - {category_name_map.get(code, '')}" for code in available_categories
]
selected_category_display = st.selectbox("대분류 선택", category_display_list)
selected_category = selected_category_display.split(" - ")[0]

# 3. 중분류 선택
available_middle_codes = sorted(
    df[df['분류'] == selected_category]['중분류코드'].dropna().unique()
)

middle_display_list = [
    format_middle_display(code, middle_name_map.get(code, "이름 없음"))
    for code in available_middle_codes
]
selected_middle_display = st.selectbox("중분류 선택", middle_display_list)

selected_middle_code = (
    selected_middle_display.split(" - ")[0][:4]
    if "A155" in selected_middle_display
    else selected_middle_display.split(" - ")[0][:3]
)

# 4. 품목 필터링
filtered_df = df[
    (df['분류'] == selected_category) &
    (df['중분류코드'] == selected_middle_code)
]

# 5. 검색 필터
search_query = st.text_input("검색어로 항목 필터링")
if search_query:
    filtered_df = filtered_df[
        filtered_df['이름'].str.contains(search_query, case=False, na=False)
    ]

# 6. 선택 항목 보여주기
if not filtered_df.empty:
    filtered_df['표시'] = filtered_df.apply(
        lambda row: f"{row['넘버']} | {row['이름']} | {row['영문명']} | {row['설명']}",
        axis=1
    )
    selected_item = st.selectbox("항목 선택", filtered_df['표시'])
    selected_row = filtered_df[filtered_df['표시'] == selected_item].iloc[0]

    st.success(f"등급: {selected_row['등급']}")
    st.session_state['등급'] = selected_row['등급']
    st.session_state['grade'] = selected_row['등급']
    st.session_state['분류'] = selected_category
else:
    st.warning("해당 중분류에 해당하는 항목이 없습니다.")

# 7. 페이지 이동
if st.button("다음 단계로 이동"):
    st.switch_page("pages/2_select_technical document.py")
