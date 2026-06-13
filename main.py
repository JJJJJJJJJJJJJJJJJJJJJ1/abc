import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 포켓몬 매칭소",
    page_icon="🔮",
    layout="centered"
)

# 2. 타이틀 및 배너 디자인
st.markdown("<h1 style='text-align: center; color: #FFCB05;'>⚡ MBTI 포켓몬 매칭소 🔮</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>나의 MBTI를 입력하고, 나와 영혼까지 닮은 포켓몬 파트너를 만나보세요!</p>", unsafe_allow_html=True)
st.markdown("---")

# 3. MBTI - 포켓몬 데이터베이스 (공식 이미지 URL 추가!)
pokemon_data = {
    "INFP": {
        "name": "뮤 (Mew)", 
        "type": "🔮 에스퍼", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "desc": "호기심이 많고 순수한 영혼을 가진 포켓몬. 혼자만의 세계에서 자유롭게 날아다니는 모습이 당신과 꼭 닮았어요!"
    },
    "INFJ": {
        "name": "가디안 (Gardevoir)", 
        "type": "🔮 에스퍼 / 🧚 페어리", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "desc": "트레이너를 향한 깊은 헌신과 통찰력을 지닌 포켓몬. 조용하지만 내면의 신념과 따뜻함이 가득해요."
    },
    "INTJ": {
        "name": "뮤츠 (Mewtwo)", 
        "type": "🔮 에스퍼", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "desc": "독립적이고 완벽한 전략을 추구하는 지성파 포켓몬. 냉철한 분석력 뒤에 숨겨진 깊은 고뇌가 느껴집니다."
    },
    "INTP": {
        "name": "폴리곤 (Porygon)", 
        "type": "⚪ 노말", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png",
        "desc": "컴퓨터 데이터로 이루어진 독창적인 포켓몬. 끊임없이 논리적이고 새로운 지식을 탐구하는 당신의 뇌 구조와 일치!"
    },
    "ISFP": {
        "name": "메타몽 (Ditto)", 
        "type": "⚪ 노말", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "desc": "어디든 자연스럽게 녹아드는 유연함과 예술적 감각을 지닌 포켓몬. 평화를 사랑하는 당신의 부드러운 성향과 똑같아요."
    },
    "ISFJ": {
        "name": "해피너스 (Blissey)", 
        "type": "⚪ 노말", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "desc": "주변 사람들을 챙기고 치유해 주는 천사 같은 포켓몬. 당신의 사려 깊은 다정함은 모두에게 위로가 됩니다."
    },
    "ISTJ": {
        "name": "철화구야 (Celesteela)", 
        "type": "⚙️ 강철 / 🕊️ 비행", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/797.png",
        "desc": "규칙적이고 묵묵하게 자신의 자리를 지키는 신뢰의 아이콘. 책임감 강하고 빈틈없는 당신의 완벽한 파트너!"
    },
    "ISTP": {
        "name": "개굴닌자 (Greninja)", 
        "type": "💧 물 / 👁️ 악", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png",
        "desc": "조용하고 신속하게 문제를 해결하는 실천파 포켓몬. 뛰어난 상황 적응력과 쿨한 마이웨이 기질이 완벽히 매치됩니다."
    },
    "ENFP": {
        "name": "이브이 (Eevee)", 
        "type": "⚪ 노말", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "desc": "무한한 가능성과 통통 튀는 매력을 가진 포켓몬! 어떤 환경에서든 밝은 에너지를 뿜어내며 주변을 행복하게 만들어요."
    },
    "ENFJ": {
        "name": "토게키스 (Togekiss)", 
        "type": "🧚 페어리 / 🕊️ 비행", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png",
        "desc": "주변에 기쁨과 평화를 전파하는 행복 전도사 포켓몬. 타인을 이끄는 따뜻한 리더십과 배려심이 당신을 떠올리게 해요."
    },
    "ENTJ": {
        "name": "리자몽 (Charizard)", 
        "type": "🔥 불꽃 / 🕊️ 비행", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "desc": "강력한 열정과 카리스마로 무리를 이끄는 지도자형 포켓몬. 목표를 향해 거침없이 돌진하는 대담함이 멋집니다."
    },
    "ENTP": {
        "name": "팬텀 (Gengar)", 
        "type": "👻 고스트 / ☠️ 독", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "desc": "장난기 가득한 눈빛으로 세상을 흥미진진하게 바라보는 재간꾼. 독창적인 아이디어와 유쾌한 토론을 즐기는 성향입니다."
    },
    "ESFP": {
        "name": "피카츄 (Pikachu)", 
        "type": "⚡ 전기", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "desc": "어디서나 존재감을 뿜어내는 우주의 주인공! 지치지 않는 에너지를 가진 당신은 모두의 사랑을 받는 스타입니다."
    },
    "ESFJ": {
        "name": "푸린 (Jigglypuff)", 
        "type": "⚪ 노말 / 🧚 페어리", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "desc": "사람들과 어울리는 것을 좋아하고 분위기를 화기애애하게 만드는 마당발 포켓몬. 공감 능력이 최고조에 달해 있어요."
    },
    "ESTJ": {
        "name": "윈디 (Arcanine)", 
        "type": "🔥 불꽃", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "desc": "위엄 있고 당당하며, 조직을 효율적으로 이끄는 정의로운 포켓몬. 확실한 규칙과 실행력으로 무리를 안전하게 지킵니다."
    },
    "ESTP": {
        "name": "루카리오 (Lucario)", 
        "type": "🥊 격투 / ⚙️ 강철", 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "desc": "위기 앞에서도 주저하지 않고 몸으로 부딪히는 실천파 액션 히어로! 스릴을 즐기고 에너제틱한 당신과 찰떡궁합입니다."
    }
}

# 4. 사용자 입력 UI
mbti_list = sorted(list(pokemon_data.keys()))
user_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요:", ["선택하세요"] + mbti_list)

st.markdown("<br>", unsafe_allow_html=True)

# 5. 매칭 결과 출력
if user_mbti != "선택하세요":
    st.balloons() # 풍선 팡팡!
    
    result = pokemon_data[user_mbti]
    st.success(f"✨ {user_mbti} 타입인 당신을 위한 완벽한 파트너를 찾았습니다!")
    
    # 좌측에 이미지, 우측에 설명을 배치하는 2단 레이아웃
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        # 공식 고화질 이미지 출력
        st.image(result["img"], use_container_width=True)
        
    with col2:
        # 포켓몬 정보 카드 디자인
        st.markdown(
            f"""
            <div style="
                background-color: #f9f9f9; 
                padding: 20px; 
                border-radius: 15px; 
                border-left: 5px solid #FFCB05;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
                height: 100%;
            ">
                <h2 style="margin-top:0; color:#1E1E1E;">🤖 {result['name']}</h2>
                <p style="font-size: 1.1em; color: #444;"><b>속성:</b> {result['type']}</p>
                <hr style="border-top: 1px dashed #ccc;">
                <p style="font-size: 1.05em; line-height: 1.6; color: #333;"><b>💡 성향 분석:</b><br>{result['desc']}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    st.markdown("---")
    
    # 🔗 센스 있는 링크 공유 기능
    st.markdown("<p style='text-align: center; font-weight: bold;'>🎈 이 재미있는 테스트를 친구들에게도 공유해 보세요! 🎈</p>", unsafe_allow_html=True)
    
    # 링크 복사 버튼 (스트림릿 내장 기능 활용)
    # 클라우드 배포 후, 사용자가 이 버튼을 누르면 이 앱의 주소가 클립보드에 복사되고 안내 문구가 뜹니다.
    st.link_button("🔗 웹앱 주소 복사 및 이동하기", "https://share.streamlit.io/")
    st.info("💡 팁: 스트림릿 클라우드 배포 후, 브라우저 상단의 주소창 URL을 복사해서 친구들에게 보내주셔도 됩니다!")

else:
    st.info("우측 화살표를 눌러 MBTI를 선택하면 파트너 포켓몬이 나타납니다! 👇")
