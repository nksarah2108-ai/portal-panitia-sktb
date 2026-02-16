import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR (FORMAT STABIL UNTUK STREAMLIT)
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
PENTADBIR_URL = "https://lh3.googleusercontent.com/d/1m87eH4bQ-p51DCMVjvM2ID8QgtwNF9ul"

# --- CUSTOM CSS: FIX GAMBAR & KEKALKAN LAYOUT ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); background-attachment: fixed; }
    
    /* PAKSA SEMUA KE TENGAH */
    .super-center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        margin: 0 auto;
    }

    /* TULISAN BERANGKAI BLINK */
    .cursive-blink {
        font-family: 'Dancing Script', cursive;
        font-size: 95px;
        color: #ad1457;
        animation: blink 1.5s linear infinite;
        margin-bottom: 0px;
    }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

    .portal-text { color: #000000 !important; font-size: 38px; font-weight: 800; margin-top: 10px; }
    .year-text { color: #ad1457; font-size: 45px; font-weight: 900; letter-spacing: 4px; margin-bottom: 30px; }

    /* GAMBAR PENTADBIR HD (FLEXIBLE SIZE) */
    .admin-img-box {
        width: 100%;
        max-width: 1000px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-top: 20px;
        border: 5px solid #ffffff;
    }

    /* SIDEBAR & HOVER */
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    [data-testid="stSidebar"] li::marker { content: "—  " !important; color: #ad1457 !important; }
    [data-testid="stWidgetLabel"] p, .stRadio label p, div[role="radiogroup"] span {
        color: #000000 !important; font-weight: 800 !important; font-size: 18px !important;
    }
    div[role="radiogroup"] label:hover { background-color: #f8bbd0 !important; border-radius: 10px; transition: 0.3s; }
    div[role="radiogroup"] label:hover p { color: #ad1457 !important; }

    /* KAD FAIL (TULISAN PUTIH KEKAL) */
    .card { 
        border-radius: 20px; padding: 25px; text-align: center; 
        color: #FFFFFF !important; font-weight: bold !important; 
        height: 180px; display: flex; flex-direction: column; 
        justify-content: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
    }
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }
    .ref-no { font-size: 13px; color: #FFFFFF !important; margin-bottom: 5px; font-weight: 800; }
    .fail-title { font-size: 22px; color: #FFFFFF !important; font-weight: 900; }

    /* EXPANDER & SUBLINK HOVER */
    .stExpander { background-color: #AED6F1 !important; border-radius: 12px !important; }
    .stExpander details summary p { color: #008080 !important; font-weight: 900; font-size: 22px; font-style: italic; }
    .sublink { display: block; padding: 12px; text-decoration: none !important; color: #000000 !important; font-weight: 600; border-radius: 10px; margin: 8px 0; transition: 0.3s; }
    .sublink:hover { background-color: #fce4ec !important; color: #ad1457 !important; transform: translateX(10px); }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SIDEBAR
with st.sidebar:
    st.image(LOGO_URL, width=100)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: 0;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio(
        "Navigasi:",
        ["🏠 LAMAN UTAMA", "REKA BENTUK DAN TEKNOLOGI", "BAHASA MELAYU", "BAHASA INGGERIS", "MATEMATIK", "SAINS", "PENDIDIKAN ISLAM", "SEJARAH", "PENDIDIKAN JASMANI DAN KESIHATAN", "PENDIDIKAN SENI VISUAL", "PENDIDIKAN MUZIK", "BAHASA ARAB"]
    )

# --- 3. LAMAN UTAMA ---
if pilihan == "🏠 LAMAN UTAMA":
    st.markdown(f"""
        <div class="super-center">
            <img src="{LOGO_URL}" width="220">
            <div class="cursive-blink">Selamat Datang</div>
            <div class="portal-text">PORTAL FAIL DIGITAL PENGURUSAN PANITIA</div>
            <div class="year-text">SKTB 2026</div>
            <img src="{PENTADBIR_URL}" class="admin-img-box">
        </div>
    """, unsafe_allow_html=True)

# --- 4. LAMAN PANITIA ---
else:
    links = {k: "#" for k in ["Carta", "Biodata", "Jadual_M", "Enrolmen", "Kewangan", "Minit", "DSKP", "Manual", "BBM", "RPT", "Akademik", "Gantt", "Laporan", "PLC", "PBD", "Analisis", "Jadual_E", "JSU", "Bank"]}
    
    st.markdown(f'<div style="text-align:center; color:black; font-family:Pacifico; font-size:35px;">📂 Portal Fail Digital Pengurusan Panitia</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center; color:#ad1457; font-size:55px; font-weight:900; margin-top:-15px;">{pilihan}</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="card color-a"><div class="ref-no">600-4/1/2/1</div><div class="fail-title">🔵 FAIL A</div>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        with st.expander("FAIL A 👇"):
            st.markdown(f'<a class="sublink" href="{links["Carta"]}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Biodata"]}" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card color-b"><div class="ref-no">600-4/1/2/2</div><div class="fail-title">🟠 FAIL B</div>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇"):
            st.markdown(f'<a class="sublink" href="{links["Minit"]}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card color-c"><div class="ref-no">600-4/1/2/3</div><div class="fail-title">🟣 FAIL C</div>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇"):
            st.markdown(f'<a class="sublink" href="{links["RPT"]}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card color-d"><div class="ref-no">600-4/1/2/4</div><div class="fail-title">🟢 FAIL D</div>PEPERIKSAAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇"):
            st.markdown(f'<a class="sublink" href="{links["PBD"]}" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SKTB 2026</p>', unsafe_allow_html=True)
