import streamlit as st
import time

# 1. 페이지 기본 설정 (상단 탭 이름 및 파비콘)
st.set_page_config(
    page_title="MBTI 포켓몬 매칭소",
    page_icon="🔮",
    layout="centered"
)

# 2. 다크 테마 커스텀 CSS (눈이 편안한 블랙/다크그레이 배경과 고급스러운 네온 포인트)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap');
    
    /* 1) 전체 배경을 세련된 다크 그레이/블랙 테마로 변경 */
    .stApp {
        background-color: #0E1117 !important;
        color: #F0F2F6 !important;
        font-family: 'Nanum Gothic', sans-serif;
    }
    
    /* 2) 대화형 드롭다운 컴포넌트 다크 테마로 커스텀 */
    .stSelectbox {
        background-color: #1F232A;
        border-radius: 16px;
        padding: 5px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* 3) 다크 포켓몬 카드 디자인 (반투명 블랙 레이아웃 및 부드러운 네온 쉐도우) */
    .pokemon-card {
        background: #1A1D24;
        border-radius: 28px;
        padding: 35px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        border: 2px solid #30363D;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-top: 20px;
    }
    
    .pokemon-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(255, 107, 107, 0.15);
        border-color: #FF6B6B;
    }
    
    /* 4) 포켓몬 타입별 네온 스타일 배지 */
    .type-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 50px;
        font-family: 'Jua', sans-serif;
        font-size: 0.95rem;
        margin-right: 6px;
        margin-bottom: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    
    /* 5) 다크모드에 걸맞는 강렬한 네온 레드 버튼 스타일 */
    div.stButton > button {
        background-color: #FF5E7E !important;
        color: white !important;
        border-radius: 16px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-family: 'Jua', sans-serif !important;
        font-size: 1.15rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 15px rgba(255, 94, 126, 0.3) !important;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #FF3B60 !important;
        transform: scale(1.03) !important;
        box-shadow: 0 8px 20px rgba(255, 94, 126, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 타이틀 및 인트로 디자인 (블랙 배경에 어울리는 화려한 네온 효과)
st.markdown("""
<div style='text-align: center; margin-bottom: 25px;'>
    <h1 style="
        font-family: 'Jua', sans-serif; 
        color: #FFCB05; 
        font-size: 3.2rem; 
        margin-bottom: 10px;
        text-shadow: 0 0 10px rgba(255, 203, 5, 0.5);
    ">⚡ MBTI 포켓몬 매칭소 🔮</h1>
    <p style="color: #A3B3C2; font-size: 1.2rem; font-weight: bold; margin-top: 5px;">
        나의 MBTI를 입력하고, 영혼의 단짝 포켓몬을 만나러 모험을 떠나볼까요? 🎈
    </p>
</div>
""", unsafe_allow_html=True)

# 4. MBTI - 포켓몬 데이터베이스 (도감 설명과 MBTI 성향 매칭 분리 탑재)
pokemon_data = {
    "INFP": {
        "name": "뮤 (Mew)", 
        "types": ["에스퍼"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "poke_desc": "모든 포켓몬의 유전자를 가졌다고 전해지는 환상의 포켓몬입니다. 자유자재로 모습을 바꿀 수 있으며, 마음이 깨끗하고 순수한 사람 앞에만 모습을 나타냅니다.",
        "match_desc": "순수하고 깊은 내면세계를 지녔으며, 호기심이 많고 따뜻한 감성을 품고 살아가는 당신은 뮤의 맑은 영혼과 신비롭고 낭만적인 성향에 완벽히 어울립니다."
    },
    "INFJ": {
        "name": "가디안 (Gardevoir)", 
        "types": ["에스퍼", "페어리"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "poke_desc": "트레이너를 지키기 위해서라면 자신의 온 힘과 모든 사이코 에너지를 쥐어짜 내어 작은 블랙홀까지 만들어내는 깊은 충성심과 수호 본능을 가진 포켓몬입니다.",
        "match_desc": "조용해 보이지만 내면에는 확고한 신념과 선한 가치를 품고 있으며, 소중한 이들을 진심으로 배려하고 돕고자 하는 당신의 헌신적인 면모는 가디안의 성격과 정확히 일치합니다."
    },
    "INTJ": {
        "name": "뮤츠 (Mewtwo)", 
        "types": ["에스퍼"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "poke_desc": "뮤의 유전자를 연구하여 재구성함으로써 전투 능력을 극도로 높여 인위적으로 창조된 포켓몬입니다. 극도의 차가운 판단력과 압도적인 인지 능력을 지녔습니다.",
        "match_desc": "독립적이고 완벽한 전략을 추구하는 뛰어난 지성파인 당신! 감정에 휘둘리지 않고 상황의 본질을 꿰뚫어 보는 냉철하고 정교한 분석력은 뮤츠의 깊고 쿨한 매력과 똑 닮아 있습니다."
    },
    "INTP": {
        "name": "폴리곤 (Porygon)", 
        "types": ["노말"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png",
        "poke_desc": "최첨단 과학 기술을 동원해 인공적으로 탄생한 전자공학 포켓몬입니다. 전뇌 공간을 자유롭게 이동하고 탐구하며, 감정이 없으나 매우 지적이고 논리적인 구조를 취합니다.",
        "match_desc": "끝없는 호기심으로 주변 사물과 논리를 해킹하듯 해체하여 독창적으로 생각하는 당신! 끊임없이 새로운 아이디어와 흥미로운 지식을 탐색하는 모습이 폴리곤의 디지털 뇌 구조와 닮았어요."
    },
    "ISFP": {
        "name": "메타몽 (Ditto)", 
        "types": ["노말"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "poke_desc": "몸의 모든 세포 조직을 스스로 마음대로 재배열하여 눈앞에 있는 상대 포켓몬의 모습, 능력, 심지어 사용하는 기술까지 완벽하게 그대로 복사하여 변신할 수 있습니다.",
        "match_desc": "물 흐르듯 자연스럽게 어디든 녹아드는 놀라운 유연함과 따뜻하고 예술적인 감각을 지닌 당신은 메타몽처럼 부드럽고 친화력 높은 최상의 평화주의자 파트너입니다."
    },
    "ISFJ": {
        "name": "해피너스 (Blissey)", 
        "types": ["노말"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "poke_desc": "믿을 수 없을 만큼 다정다감하고 친절한 성격입니다. 이 포켓몬이 품고 다니는 알을 단 한 입만 먹어도 누구든지 금세 기분이 좋아지고 미소를 짓는 행복과 치유의 포켓몬입니다.",
        "match_desc": "주변 사람들을 소리 없이 챙기고 위로해 주는 따뜻한 배려심의 수호자! 타인의 상처를 들어주고 진심 어린 치유를 해주는 성향이 해피너스의 자비로운 천사 같은 모습과 완전히 겹칩니다."
    },
    "ISTJ": {
        "name": "철화구야 (Celesteela)", 
        "types": ["강철", "비행"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/797.png",
        "poke_desc": "엄청난 철갑 같은 몸을 지녔으며 가스를 내뿜어 높은 하늘을 안전하고 묵직하게 가르는 신비한 울트라비스트 포켓몬입니다. 흔들림 없는 강직함과 압도적인 무게감을 자랑합니다.",
        "match_desc": "매사에 계획적이고 규칙을 잘 지키며, 약속을 칼같이 완수하여 주위 사람들에게 무한한 신뢰를 받는 당신의 정직하고 철저한 책임감은 철화구야의 단단하고 변치 않는 매력과 같습니다."
    },
    "ISTP": {
        "name": "개굴닌자 (Greninja)", 
        "types": ["물", "악"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png",
        "poke_desc": "바람처럼 민첩하고 날렵하게 움직이는 닌자 형태의 포켓몬입니다. 물을 높은 압력으로 압축해 수리검을 만들어 발사하는 기민하고 정교한 파이팅 능력을 자랑합니다.",
        "match_desc": "조용이지만 실용적인 감각이 발달해 뛰어난 도구 활용과 위기대처 능력을 보여주는 당신! 혼자 행동할 때 최고의 효율을 발휘하는 쿨한 기질이 개굴닌자의 프로페셔널한 액션과 똑 닮았습니다."
    },
    "ENFP": {
        "name": "이브이 (Eevee)", 
        "types": ["노말"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "poke_desc": "살아가는 환경과 자극에 따라 다양한 포켓몬으로 무궁무진하게 돌연변이적 성장을 거듭하는 이례적인 유전자를 가지고 있습니다. 애교가 많고 항상 호기심과 활기로 가득 차 있습니다.",
        "match_desc": "어떤 상황이든 즐길 수 있는 긍정적인 힘과 어디로 튈지 모르는 멋진 상상력을 소유한 에너지스타! 사람들의 마음에 무해하고 맑은 기쁨을 피워내는 당신은 무한 가능성의 아이콘 이브이입니다."
    },
    "ENFJ": {
        "name": "토게키스 (Togekiss)", 
        "types": ["페어리", "비행"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png",
        "poke_desc": "서로의 다름을 존중하고 다툼이 없는 세상에만 모습을 나타내는 축복의 날개를 지녔습니다. 세상을 돌아다니며 기쁨과 행운의 은혜를 아낌없이 베푸는 자비로운 포켓몬입니다.",
        "match_desc": "사람들과 조화롭고 건강하게 어울려 가치 있는 성장을 이루어낼 수 있도록 다정하고 힘찬 리더십으로 끌어주는 당신의 성향은 토게키스가 뿌리는 감동적인 은혜의 빛과 꼭 어울립니다."
    },
    "ENTJ": {
        "name": "리자몽 (Charizard)", 
        "types": ["불꽃", "비행"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "poke_desc": "커다란 날개로 넓은 창공을 지배하며 입에서 바위조차 녹여버리는 가공할 수준의 푸른 뜨거운 화염을 뿜어냅니다. 강한 강자와 싸울 때 불꽃이 더 거세게 활활 타오르는 전사입니다.",
        "match_desc": "자신감이 넘치고 명확한 목표 지향성을 지녀 어떤 곤경과 위기에도 굴하지 않고 거침없이 팀을 완벽한 성취로 리드하는 당신의 대담하고도 불타오르는 열정은 카리스마 넘치는 리자몽의 화염입니다."
    },
    "ENTP": {
        "name": "팬텀 (Gengar)", 
        "types": ["고스트", "독"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "poke_desc": "그림자 속에 유연하게 파고들어 기회를 엿보며 주변의 온도를 급격히 낮춰 사람들을 오싹하게 장난치는 개구쟁이 고스트입니다. 늘 기묘하고 똑똑한 장난을 궁리합니다.",
        "match_desc": "기발한 번뜩임과 신선하고 유니크한 통찰력을 사랑하며, 낡은 틀에 묶이지 않고 유쾌하고 재치 있는 아이디어를 이리저리 부딪치고 토론하는 것을 좋아하는 모습은 장난기 넘치는 꾀돌이 팬텀과 일품 매칭입니다."
    },
    "ESFP": {
        "name": "피카츄 (Pikachu)", 
        "types": ["전기"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "poke_desc": "뺨의 붉은 전깃주머니에 짜릿한 전기를 품고 다니며 기분이 좋을 때는 번쩍이며 에너지를 방출합니다. 호기심 많고 애정이 넘쳐 동료들과 신나게 춤추고 교감하기를 즐깁니다.",
        "match_desc": "지루함을 한순간에 날려 보내고 삶을 매 순간 유쾌하고 반짝반짝하게 축제처럼 가꾸는 최고의 분위기 메이커! 타인과 친밀하게 어우러져 기분 좋은 자극을 주는 매력은 피카츄의 전하와 같습니다."
    },
    "ESFJ": {
        "name": "푸린 (Jigglypuff)", 
        "types": ["노말", "페어리"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "poke_desc": "동그란 풍선 같은 몸을 잔뜩 부풀려 커다란 보석 같은 눈동자로 사람들의 이목을 집중시킨 뒤, 심신을 완전히 정화하고 치유해 주는 포근한 자장가 멜로디를 열심히 노래합니다.",
        "match_desc": "주변 동료들과 매끄러운 수다와 진솔한 소통을 이어가길 가장 좋아하고, 모두가 행복하고 상처받지 않게 따뜻한 연결망을 구축하려 애쓰는 마당발인 당신은 사랑스러운 무대의 주인공 푸린입니다."
    },
    "ESTJ": {
        "name": "윈디 (Arcanine)", 
        "types": ["불꽃"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "poke_desc": "전설 속 유서 깊은 두루마리 그림에도 등장할 만큼 늠름한 자태를 가진 기품 있는 수호견 포켓몬입니다. 사나운 위엄과 신속한 질주 능력으로 자신의 무리를 체계적으로 정돈해 다스립니다.",
        "match_desc": "사회의 질서와 조직의 정교한 관리 규칙을 존중하고 솔선수범하여 사람들을 지휘하고 보호하는 듬직한 행동 대장형 리더인 당신의 확실한 통솔 능력은 기품 있는 전설의 윈디와 한 쌍을 이룹니다."
    },
    "ESTP": {
        "name": "루카리오 (Lucario)", 
        "types": ["격투", "강철"], 
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "poke_desc": "생명체라면 누구든 발산하는 고유의 생체 에너지인 '파동(아우라)'을 시각적으로 읽어내는 신비한 무도가 포켓몬입니다. 상대의 보이지 않는 생각마저 파악해 기민하게 먼저 반응합니다.",
        "match_desc": "머리 아픈 계획이나 복잡한 계산보단 지금 당장 뛰어들어 경험하고 스릴 넘치게 문제를 해결해 버리는 타고난 승부사 기질의 소유자! 실질적이고 파워풀한 행동력은 용맹한 아우라 전사 루카리오입니다."
    }
}

# 포켓몬 속성별 다크테마용 네온 컬러 매핑
type_colors = {
    "에스퍼": "#FF4081", "페어리": "#FF80AB", "노말": "#B0BEC5", 
    "강철": "#90A4AE", "비행": "#7986CB", "물": "#4FC3F7", 
    "악": "#90A4AE", "불꽃": "#FF7043", "고스트": "#9575CD", 
    "독": "#BA68C8", "전기": "#FFD54F", "격투": "#E57373"
}

# 5. 사용자 입력 UI
mbti_list = sorted(list(pokemon_data.keys()))

st.markdown("<p style='font-family: \"Jua\", sans-serif; font-size: 1.3rem; margin-bottom: 5px; color:#A3B3C2;'>👇 나의 MBTI 성향을 선택하세요</p>", unsafe_allow_html=True)
user_mbti = st.selectbox("", ["-- 선택해주세요 --"] + mbti_list, label_visibility="collapsed")

# 세션 상태 제어
if "last_mbti" not in st.session_state:
    st.session_state.last_mbti = None

# 6. 매칭 결과 연출 및 카드 생성
if user_mbti != "-- 선택해주세요 --":
    # 새로운 MBTI를 선택한 경우에만 로딩 및 벌룬 연출 실행
    if st.session_state.last_mbti != user_mbti:
        with st.spinner("🔮 당신의 깊은 성향과 일치하는 포켓몬의 주파수를 수신 중입니다..."):
            loading_progress = st.progress(0)
            for percent in range(100):
                time.sleep(0.012)
                loading_progress.progress(percent + 1)
            st.balloons()
        st.session_state.last_mbti = user_mbti
    
    result = pokemon_data[user_mbti]
    
    # 속성 배지 HTML 생성
    badges_html = ""
    for t in result["types"]:
        bg_color = type_colors.get(t, "#777777")
        text_color = "#333" if t == "전기" else "#FFF"
        badges_html += f'<span class="type-badge" style="background-color: {bg_color}; color: {text_color};">#{t}</span>'

    # 웹앱 상에 이미지와 콘텐츠 카드를 한데 묶은 다크 테마 카드 출력
    st.markdown(f"""
    <div class="pokemon-card">
        <div style="display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 30px;">
            <div style="flex: 1; min-width: 220px; text-align: center;">
                <img src="{result['img']}" style="width: 100%; max-width: 250px; filter: drop-shadow(0px 0px 20px rgba(255,255,255,0.15));" alt="{result['name']}">
            </div>
            <div style="flex: 1.5; min-width: 280px; text-align: left;">
                <span style="font-size: 0.95rem; font-weight: bold; color: #FF6B6B; letter-spacing: 1px;">{user_mbti} 파트너</span>
                <h2 style="font-family: 'Jua', sans-serif; font-size: 2.2rem; color: #FFFFFF; margin: 4px 0 12px 0;">{result['name']}</h2>
                <div style="margin-bottom: 18px;">
                    {badges_html}
                </div>
                
                <!-- 📖 포켓몬 고유의 공식 도감 설명 (다크모드용 테마 적용) -->
                <div style="
                    font-size: 1.0rem; 
                    line-height: 1.6; 
                    color: #CFD8DC; 
                    background: #252A34; 
                    padding: 16px; 
                    border-radius: 20px; 
                    border-left: 5px solid #90A4AE;
                    margin-bottom: 15px;
                ">
                    <span style="font-family: 'Jua', sans-serif; color: #90A4AE; font-size: 1.1rem;">📖 도감 설명</span><br>
                    <div style="margin-top: 5px;">{result['poke_desc']}</div>
                </div>
                
                <!-- 💡 MBTI 영혼의 단짝 분석 설명 (다크모드용 테마 적용) -->
                <div style="
                    font-size: 1.0rem; 
                    line-height: 1.6; 
                    color: #FFCDD2; 
                    background: #2D1F24; 
                    padding: 16px; 
                    border-radius: 20px; 
                    border-left: 5px solid #FF5E7E;
                ">
                    <span style="font-family: 'Jua', sans-serif; color: #FF5E7E; font-size: 1.1rem;">💡 당신과 닮은 점은?</span><br>
                    <div style="margin-top: 5px;">{result['match_desc']}</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 7. 🔗 실시간 테스트 링크 공유 파트
    st.markdown("<br><hr style='border: 1px dashed #30363D;'><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-family: \"Jua\", sans-serif; font-size: 1.4rem; color: #FF5E7E;'>🎉 당신의 결과를 친구에게 자랑해보세요! 🎉</p>", unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.link_button("🌐 스트림릿 홈 놀러가기", "https://share.streamlit.io/")
        
    with col_btn2:
        # 아이프레임(iframe) 환경에서도 문제없이 작동하는 호환용 클립보드 복사 기법 적용
        copy_and_share_html = """
        <!-- 커스텀 예쁜 토스트 디자인 -->
        <div id="custom-toast" style="
            display: none;
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background-color: #FF5E7E;
            color: white;
            padding: 14px 28px;
            border-radius: 50px;
            font-size: 1.05rem;
            font-weight: bold;
            z-index: 99999;
            box-shadow: 0 10px 25px rgba(255, 94, 126, 0.45);
            font-family: 'Jua', sans-serif;
            text-align: center;
            animation: slideUp 0.3s ease-out;
        ">
            🎈 링크가 클립보드에 복사되었습니다! 친구들에게 공유해 주세요! 🎈
        </div>

        <button class="share-button" onclick="
            const dummy = document.createElement('textarea');
            dummy.value = window.location.href;
            document.body.appendChild(dummy);
            dummy.select();
            try {
                document.execCommand('copy');
                
                const toast = document.getElementById('custom-toast');
                toast.style.display = 'block';
                setTimeout(() => {
                    toast.style.display = 'none';
                }, 3000);
            } catch (err) {
                console.error('복사 중 에러 발생: ', err);
            }
            document.body.removeChild(dummy);
        ">
            🔗 친구에게 링크 복사하기
        </button>

        <style>
            @keyframes slideUp {
                from { bottom: 0px; opacity: 0; }
                to { bottom: 30px; opacity: 1; }
            }
            .share-button {
                width: 100%;
                background-color: #30363D !important;
                color: #F0F2F6 !important;
                border: 1px solid #FF5E7E !important;
                border-radius: 16px !important;
                padding: 12px 24px !important;
                font-family: 'Jua', sans-serif !important;
                font-size: 1.15rem !important;
                cursor: pointer;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3) !important;
                transition: all 0.3s ease !important;
            }
            .share-button:hover {
                background-color: #FF5E7E !important;
                color: white !important;
                transform: scale(1.03) !important;
                box-shadow: 0 8px 20px rgba(255, 94, 126, 0.4) !important;
            }
        </style>
        """
        st.markdown(copy_and_share_html, unsafe_allow_html=True)

else:
    # 최초 진입 시 보여주는 다크 테마 안내 상자
    st.markdown("""
    <div style="
        background-color: #1A1D24; 
        padding: 25px; 
        border-radius: 20px; 
        text-align: center; 
        border: 2px dashed #30363D;
        margin-top: 10px;
    ">
        <p style="font-size: 1.15rem; color: #A3B3C2; margin: 0; font-weight: bold;">
            위의 드롭다운 메뉴를 눌러 성향을 선택해 주세요! 🔮<br>
            웅장한 사운드와 함께 다크 네온빛 파트너 포켓몬이 등장합니다.
        </p>
    </div>
    """, unsafe_allow_html=True)
