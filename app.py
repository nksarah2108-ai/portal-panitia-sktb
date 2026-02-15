import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# --- CUSTOM CSS: TEMA ABSTRAK & PINK LEMBUT ---
st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%);
        background-attachment: fixed;
    }
    
    /* Gaya Tulisan Selamat Datang */
    .welcome-title {
        text-align: center;
        color: #ad1457;
        font-family: 'Georgia', serif;
        font-weight: bold;
        font-size: 45px;
        text-shadow: 2px 2px #f8bbd0;
        margin-top: 20px;
    }
    
    .sub-welcome {
        text-align: center;
        color: #5d4037;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 40px;
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

    /* Kad Fail - Tulisan Putih */
    .card { 
        border-radius: 20px; padding: 25px; text-align: center; 
        color: #FFFFFF !important; font-weight: bold !important; 
        height: 180px; display: flex; flex-direction: column; 
        justify-content: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
    }
    
    /* Gaya Gambar Pentadbir */
    .admin-frame {
        border-radius: 50%;
        border: 5px solid #fff;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }
    
    .sublink { display: block; padding: 12px; text-decoration: none !important; color: #000000 !important; font-weight: 600; transition: 0.3s; border-radius: 10px; margin: 8px 0; }
    .sublink:hover { background-color: #fce4ec; color: #ad1457 !important; transform: translateX(10px); }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: black;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
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

# --- 3. LOGIK PAPARAN LAMAN UTAMA ---
if pilihan == "🏠 LAMAN UTAMA":
    # Logo Sekolah
    col_logo1, col_logo2, col_logo3 = st.columns([2, 1, 2])
    with col_logo2:
        # Masukkan URL Logo Sekolah Moon di sini
        st.image("https://via.placeholder.com/150?text=LOGO+SKTB", width=150) 

    st.markdown('<div class="welcome-title">SELAMAT DATANG</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-welcome">PORTAL PENGURUSAN FAIL PANITIA SKTB 2026</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Bahagian Pentadbir
    st.markdown("<h3 style='text-align: center; color: #ad1457;'>👤 BARISAN PENTADBIR SKTB</h3>", unsafe_allow_html=True)
    
    col_admin1, col_admin2, col_admin3 = st.columns(3)
    
    with col_admin1:
        st.image("https://via.placeholder.com/200?text=GPK+KURIKULUM", caption="GPK KURIKULUM")
    with col_admin2:
        st.image("https://via.placeholder.com/250?text=GURU+BESAR", caption="GURU BESAR")
    with col_admin3:
        st.image("https://via.placeholder.com/200?text=GPK+HEM", caption="GPK HEM")

# --- 4. LOGIK PAPARAN PANITIA (RBT DAN LAIN-LAIN) ---
else:
    # (Kod asal panitia Moon kekal di bawah ini)
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
            "Gantt": "https://drive.google.com/file/d/1POSqk4gZVQ3JuFhwSHmiZBezOGK0tiRr/view?usp=sharing",
            "Laporan": "https://drive.google.com/drive/folders/1VidiLz-pZ3WJj29p13BrVXFHly6IShKc?usp=drive_link",
            "PLC": "https://drive.google.com/drive/folders/1NwX9c5l7SDRPNVa3UKzz1LX1s-Ic3Ghc?usp=sharing",
            "PBD": "https://drive.google.com/drive/folders/1sUR2Sq6fWbZk1gGveuRX935pqWkmUIgx?usp=sharing",
            "Analisis": "https://drive.google.com/drive/folders/1aJspYVKRdzMMpNsYtRA1SjEOKSeWoka8?usp=drive_link",
            "Jadual_E": "https://drive.google.com/drive/folders/17doEPe67XPYLNcSqS-d-aGtCXjMddiDj?usp=sharing",
            "JSU": "https://drive.google.com/drive/folders/17swAo8ZjS9HPE1N1xNTyi9Lfw2LRzc15?usp=sharing",
            "Bank": "https://drive.google.com/drive/folders/17-cMG1Orr1Q5oxbUBzKShiDSuMDyv8gH?usp=sharing"
        })

    st.markdown(f'<h1 class="main-title">📂 Portal Fail Digital Pengurusan Panitia <br>{pilihan}</h1>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="card color-a"><div class="ref-no">600-4/1/2/1</div>🔵 FAIL A<br>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        with st.expander("FAIL A 👇"):
            st.markdown(f'<a class="sublink" href="{links["Carta"]}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Biodata"]}" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_M"]}" target="_blank">📝 Jadual Pemantauan</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Enrolmen"]}" target="_blank">📊 Data Enrolmen</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Kewangan"]}" target="_blank">💰 Pengurusan Kewangan</a>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card color-b"><div class="ref-no">600-4/1/2/2</div>🟠 FAIL B<br>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇"):
            st.markdown(f'<a class="sublink" href="{links["Minit"]}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["DSKP"]}" target="_blank">📚 DSKP</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Manual"]}" target="_blank">📂 Manual & Modul</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["BBM"]}" target="_blank">💻 BBM</a>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c"><div class="ref-no">600-4/1/2/3</div>🟣 FAIL C<br>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇"):
            st.markdown(f'<a class="sublink" href="{links["RPT"]}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Akademik"]}" target="_blank">🚀 Program Akademik</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Gantt"]}" target="_blank">📈 Carta Gantt</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Laporan"]}" target="_blank">📝 Laporan Program</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["PLC"]}" target="_blank">👥 Program PLC</a>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d"><div class="ref-no">600-4/1/2/4</div>🟢 FAIL D<br>PEPERIKSAAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇"):
            st.markdown(f'<a class="sublink" href="{links["PBD"]}" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Analisis"]}" target="_blank">📝 Analisis Peperiksaan</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_E"]}" target="_blank">📅 Jadual Peperiksaan</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["JSU"]}" target="_blank">🔍 Analisis Item & JSU</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Bank"]}" target="_blank">🏦 Bank Soalan 🔍</a>', unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SKTB 2026</p>', unsafe_allow_html=True)
