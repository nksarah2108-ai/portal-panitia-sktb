import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# Link Logo Moon yang dah ditukar jadi Direct Link
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"

# --- CUSTOM CSS: TEMA ABSTRAK & PINK LEMBUT (IKUT SELERA MOON) ---
st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%);
        background-attachment: fixed;
    }
    
    /* Gaya Tulisan Selamat Datang */
    .welcome-title {
        text-align: center; color: #ad1457; font-family: 'Georgia', serif;
        font-weight: bold; font-size: 45px; text-shadow: 2px 2px #f8bbd0; margin-top: 10px;
    }
    
    .sub-welcome {
        text-align: center; color: #5d4037; font-size: 22px; font-weight: 800; margin-bottom: 30px;
    }

    /* Sidebar - Tulisan Hitam Pekat */
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    [data-testid="stWidgetLabel"] p, .stRadio label p, div[role="radiogroup"] span {
        color: #000000 !important; font-weight: 800 !important; font-size: 18px !important;
    }
    
    /* Hover Pink Sidebar */
    div[role="radiogroup"] label:hover {
        background-color: #f8bbd0 !important;
        border-radius: 10px;
        transition: 0.3s;
    }
    div[role="radiogroup"] label:hover p { color: #ad1457 !important; }

    /* KAD FAIL - TULISAN PUTIH (KEKAL 4 KOLUM) */
    .card { 
        border-radius: 20px; padding: 25px; text-align: center; 
        color: #FFFFFF !important; font-weight: bold !important; 
        height: 180px; display: flex; flex-direction: column; 
        justify-content: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        transition: transform 0.3s;
    }
    .card:hover { transform: scale(1.05); border: 2px solid #FFFFFF; }
    
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }
    
    .ref-no { font-size: 13px; opacity: 1.0; color: #FFFFFF !important; margin-bottom: 5px; }
    .fail-title { font-size: 20px; color: #FFFFFF !important; font-weight: 900; }

    .sublink { display: block; padding: 12px; text-decoration: none !important; color: #000000 !important; font-weight: 600; transition: 0.3s; border-radius: 10px; margin: 8px 0; }
    .sublink:hover { background-color: #fce4ec; color: #ad1457 !important; transform: translateX(10px); }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SIDEBAR
with st.sidebar:
    st.image(LOGO_URL, width=100)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: 0;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio(
        "Navigasi:",
        [
            "🏠 LAMAN UTAMA",
            "REKA BENTUK DAN TEKNOLOGI", 
            "BAHASA MELAYU", 
            "BAHASA INGGERIS", 
            "MATEMATIK", 
            "SAINS", 
            "PENDIDIKAN ISLAM", 
            "SEJARAH", 
            "PENDIDIKAN JASMANI DAN KESIHATAN", 
            "PENDIDIKAN SENI VISUAL", 
            "PENDIDIKAN MUZIK", 
            "BAHASA ARAB"
        ]
    )

# --- 3. LAMAN UTAMA ---
if pilihan == "🏠 LAMAN UTAMA":
    st.markdown("<br>", unsafe_allow_html=True)
    col_logo1, col_logo2, col_logo3 = st.columns([1.5, 1, 1.5])
    with col_logo2:
        st.image(LOGO_URL, use_container_width=True) 

    st.markdown('<div class="welcome-title">SELAMAT DATANG</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-welcome">PORTAL PENGURUSAN FAIL PANITIA SKTB 2026</div>', unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<h3 style='text-align: center; color: #ad1457;'>👤 BARISAN PENTADBIR SKTB</h3>", unsafe_allow_html=True)
    
    col_admin1, col_admin2, col_admin3 = st.columns(3)
    with col_admin1:
        st.image("https://via.placeholder.com/200?text=GPK+KURIKULUM", caption="GPK KURIKULUM")
    with col_admin2:
        st.image("https://via.placeholder.com/250?text=GURU+BESAR", caption="GURU BESAR")
    with col_admin3:
        st.image("https://via.placeholder.com/200?text=GPK+HEM", caption="GPK HEM")

# --- 4. LAMAN PANITIA (KEKALKAN LAYOUT 4 KOLUM ASAL MOON) ---
else:
    links = {k: "#" for k in ["Carta", "Biodata", "Jadual_M", "Enrolmen", "Kewangan", "Minit", "DSKP", "Manual", "BBM", "RPT", "Akademik", "Gantt", "Laporan", "PLC", "PBD", "Analisis", "Jadual_E", "JSU", "Bank"]}

    if pilihan == "REKA BENTUK DAN TEKNOLOGI":
        links.update({
            "Carta": "https://docs.google.com/presentation/d/1b76mhH6fqiZSt48ARdrNyJulunexr_u7PZj4AFoq_Gc/edit?usp=sharing",
            "Biodata": "https://docs.google.com/presentation/d/18h4II0zdKX5IEZXhMRlxr89j-4CZdhRLuKdqrcR1118/edit?usp=drive_link",
            "Jadual_M": "https://docs.google.com/presentation/d/1vx4yASQI69Dw3WgLbHdLLIi6y6Uvwqx_cPR7jDpnEf4/edit?usp=sharing",
            "Enrolmen": "https://docs.google.com/spreadsheets/d/1lQLHlLLklHhZpKaVTs0D5C7PGaJOvo9g/edit?usp=drive_link",
            "Kewangan": "https://docs.google.com/spreadsheets/d/1DdzyEc8c0OnEY6KN9LPWsYkpdNJcBDr7oZzLLo1_9mc/edit?usp=sharing",
            "Minit": "https://drive.google.com/drive/folders/1KfhRHblLKPyn9VFLq0bwBEgeVPq_9PLP?usp=sharing",
            "DSKP": "https://drive.google.com/drive/folders/15v24g0l9KulIq14F6pwwn-I1naMaO-0S?usp=sharing",
            "Manual": "https://drive.google.com/drive/folders/1__aMuk0rjNRJIPgUAHhBgCYmNRpOuInJ?usp=sharing",
            "BBM": "https://drive.google.com/drive/folders/1AsgXDpVbDMTBOEknbRn-70czAZVUXHVJ?usp=sharing",
            "RPT": "https://drive.google.com/drive/folders/13ONhdCcHDgjo-pMYoMtyQUKqQc3XFGGh?usp=drive_link",
            "Akademik": "https://docs.google.com/presentation/d/1W_pVK4kuv4XHzJrm8Vi6IPjnqhfo7xXSVUo7n54Vflc/edit?usp=sharing",
            "Gantt": "
