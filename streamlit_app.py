import streamlit as st

# 웹 페이지 제목 설정
st.title("📊 등급 산출 프로그램")
st.write("점수를 입력하거나 슬라이더를 조절하여 등급을 확인하세요.")

# 1. 점수 입력 받기 (숫자 입력창과 슬라이더)
# min_value, max_value, value(기본값), step(조절 단위) 설정
n = st.number_input("점수를 입력하세요 (0~100):", min_value=0, max_value=100, value=50, step=1)
# n = st.slider("점수를 선택하세요:", min_value=0, max_value=100, value=50) # 슬라이더가 좋다면 이 줄의 주석을 해제하세요.

# 큰 글씨로 결과를 보여주기 위한 공간 분리
st.divider()

# 2. 기존 등급 분류 로직 적용
if n >= 77:
    grade = '1등급'
    color = '🔴'
elif n >= 66:
    grade = '2등급'
    color = '🟠'
elif n >= 55:
    grade = '3등급'
    color = '🟡'
elif n >= 43:
    grade = '4등급'
    color = '🟢'
elif n >= 32:
    grade = '5등급'
    color = '🔵'
elif n >= 21:
    grade = '6등급'
    color = '🟣'
elif n >= 13:
    grade = '7등급'
    color = '🟤'
elif n >= 8:
    grade = '8등급'
    color = '⚫'
else:
    grade = '9등급'
    color = '⚪'

# 3. 결과 화면 출력
st.subheader(f"입력한 점수: {n}점")
st.success(f"결과: {color} **{grade}** 입니다!")