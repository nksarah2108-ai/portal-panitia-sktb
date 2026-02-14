import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# --- CUSTOM CSS (TEMA COMEL MOON) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); }
    .main-title { text-align: center; color: #000000 !important; font-family: 'Arial Black', sans-serif; padding: 20px; }
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    .card { border-radius: 20px; padding: 25px; text-align: center; color: white !important; font-weight: bold; height: 180px; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); transition: transform 0.3s; }
    .card:hover { transform: scale(1.05); }
    .stExpander { background-color: #AED6F1 !important; border-radius: 12px !important; border: 1px solid #85C1E9 !important; }
    .stExpander details summary p { color: #008080 !important; font-weight: 900; font-size: 22px; font-style: italic; text-align: center; margin: auto; width: 100%; transition: all 0.4s; }
    .stExpander details summary:hover p { color: #004d4d !important; transform: scale(1.1); letter-spacing: 2px; }
    .sublink { display: block; padding: 12px; text-decoration: none !important; color: #000000 !important; font-weight: 600; transition: 0.3s; border-radius: 10px; margin: 8px 0; }
    .sublink:hover { background-color: #fce4ec; color: #ad1457 !important; transform: translateX(10px); }
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }
    .ref-no { font-size: 13px; opacity: 0.9; }
    .fail-title { font-size: 20px; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio(
        "Pilih Panitia:",
        ["REKA BENTUK & TEKNOLOGI (RBT)", "BAHASA MELAYU (BM)", "BAHASA INGGERIS (BI)", 
         "MATEMATIK", "SAINS", "PENDIDIKAN ISLAM", "SEJARAH", 
         "P. JASMANI & KESIHATAN", "PSV", "PENDIDIKAN MUZIK", "BAHASA ARAB"]
    )

# 3. PENGURUSAN PAUTAN (Moon kemaskini kat sini je nampak!)
# Kita set pautan RBT sebagai pautan asal.
links = {
    "Carta": "#", "Biodata": "#", "Jadual": "#", "Enrolmen": "#", "Kewangan": "#",
    "Minit": "#", "DSKP": "#", "Manual": "#", "BBM": "#",
    "RPT": "#", "Akademik": "#", "Gantt": "#", "Laporan": "#", "PLC": "#",
    "PBD": "#", "Analisis": "#", "Jadual_Peperiksaan": "#", "JSU": "#", "Bank": "#"
}

if pilihan == "REKA BENTUK & TEKNOLOGI (RBT)":
    links["Carta"] = "https://docs.google.com/presentation/d/1b76mhH6fqiZSt48ARdrNyJulunexr_u7PZj4AFoq_Gc/edit?usp=sharing"
    links["Biodata"] = "https://docs.google.com/presentation/d/18h4II0zdKX5IEZXhMRlxr89j-4CZdhRLuKdqrcR1118/edit?usp=drive_link"
    links["Jadual"] = "https://docs.google.com/presentation/d/1vx4yASQI69Dw3WgLbHdLLIi6y6Uvwqx_cPR7jDpnEf4/edit?usp=sharing"
    links["Enrolmen"] = "https://docs.google.com/spreadsheets/d/1lQLHlLLklHhZpKaVTs0D5C7PGaJOvo9g/edit?usp=drive_link"
    links["Kewangan"] = "https://docs.google.com/spreadsheets/d/1DdzyEc8c0OnEY6KN9LPWsYkpdNJcBDr7oZzLLo1_9mc/edit?usp=sharing"
    links["Minit"] = "https://drive.google.com/drive/folders/1KfhRHblLKPyn9VFLq0bwBEgeVPq_9PLP?usp=sharing"
    links["DSKP"] = "https://drive.google.com/drive/folders/15v24g0l9KulIq14F6pwwn-I1naMaO-0S?usp=sharing"
    links["Manual"] = "https://drive.google.com/drive/folders/1__aMuk0rjNRJIPgUAHhBgCYmNRpOuInJ?usp=sharing"
    links["BBM"] = "https://drive.google.com/drive/folders/1AsgXDpVbDMTBOEknbRn-70czAZVUXHVJ?usp=sharing"
    links["RPT"] = "https://drive.google.com/drive/folders/13ONhdCcHDgjo-pMYoMtyQUKqQc3XFGGh?usp=drive_link"
    links["Akademik"] = "https://docs.google.com/presentation/d/1W_pVK4kuv4XHzJrm8Vi6IPjnqhfo7xXSVUo7n54Vflc/edit?usp=sharing"
    links["Gantt"] = "https://drive.google.com/file/d/1POSqk4gZVQ3JuFhwSHmiZBezOGK0tiRr/view?usp=sharing"
    links["Laporan"] = "https://drive.google.com/drive/folders/1VidiLz-pZ3WJj29p13BrVXFHly6IShKc?usp=drive_link"
    links["PLC"] = "https://drive.google.com/drive/folders/1NwX9c5l7SDRPNVa3UKzz1LX1s-Ic3Ghc?usp=sharing"
    links["PBD"] = "https://drive.google.com/drive/folders/1sUR2Sq6fWbZk1gGveuRX935pqWkmUIgx?usp=sharing"
    links["Analisis"] = "https://drive.google.com/drive/folders/1aJspYVKRdzMMpNsYtRA1SjEOKSeWoka8?usp=drive_link"
    links["Jadual_Peperiksaan"] = "https://drive.google.com/drive/folders/17doEPe67XPYLNcSqS-d-aGtCXjMddiDj?usp=sharing"
    links["JSU"] = "https://drive.google.com/drive/folders/17swAo8ZjS9HPE1N1xNTyi9Lfw2LRzc15?usp=sharing"
    links["Bank"] = "https://drive.google.com/drive/folders/17-cMG1Orr1Q5oxbUBzKShiDSuMDyv8gH?usp=sharing"

elif pilihan == "BAHASA MELAYU (BM)":
    # Moon cuma perlu copy-paste baris links[...] kat atas dan tukar URL saja nanti.
    pass 

# 4. PAPARAN UTAMA (Sama untuk semua Panitia)
st.markdown(f'<h1 class="main-title">📂 Portal Fail Digital Pengurusan Panitia <br>{pilihan}</h1>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card color-a"><div class="ref-no">600-4/1/2/1</div><div class="fail-title">🔵 FAIL A</div><br>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
    with st.expander("FAIL A 👇"):
        st.markdown(f'<a class="sublink" href="{links["Carta"]}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Biodata"]}" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Jadual"]}" target="_blank">📝 Jadual Pemantauan</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Enrolmen"]}" target="_blank">📊 Data Enrolmen</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Kewangan"]}" target="_blank">💰 Pengurusan Kewangan</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card color-b"><div class="ref-no">600-4/1/2/2</div><div class="fail-title">🟠 FAIL B</div><br>KURIKULUM</div>', unsafe_allow_html=True)
    with st.expander("FAIL B 👇"):
        st.markdown(f'<a class="sublink" href="{links["Minit"]}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["DSKP"]}" target="_blank">📚 DSKP</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Manual"]}" target="_blank">📂 Manual & Modul</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["BBM"]}" target="_blank">💻 BBM</a>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card color-c"><div class="ref-no">600-4/1/2/3</div><div class="fail-title">🟣 FAIL C</div><br>PERANCANGAN</div>', unsafe_allow_html=True)
    with st.expander("FAIL C 👇"):
        st.markdown(f'<a class="sublink" href="{links["RPT"]}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Akademik"]}" target="_blank">🚀 Program Akademik</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Gantt"]}" target="_blank">📈 Carta Gantt</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Laporan"]}" target="_blank">📝 Laporan Program</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["PLC"]}" target="_blank">👥 Program PLC</a>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card color-d"><div class="ref-no">600-4/1/2/4</div><div class="fail-title">🟢 FAIL D</div><br>PEPERIKSAAN</div>', unsafe_allow_html=True)
    with st.expander("FAIL D 👇"):
        st.markdown(f'<a class="sublink" href="{links["PBD"]}" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Analisis"]}" target="_blank">📝 Analisis Peperiksaan</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Jadual_Peperiksaan"]}" target="_blank">📅 Jadual Peperiksaan</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["JSU"]}" target="_blank">🔍 Analisis Item & JSU</a>', unsafe_allow_html=True)
        st.markdown(f'<a class="sublink" href="{links["Bank"]}" target="_blank">🏦 Bank Soalan 🔍</a>', unsafe_allow_html=True)

st.divider()
st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SKTB 2026</p>', unsafe_allow_html=True)
