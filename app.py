import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# --- CUSTOM CSS: SIDEBAR HITAM & HOVER PINK ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); }
    .main-title { text-align: center; color: #000000 !important; font-family: 'Arial Black', sans-serif; padding: 20px; }
    
    /* SIDEBAR STYLE - TULISAN MENU PANITIA */
    [data-testid="stSidebar"] { 
        background-color: #fce4ec !important; 
        border-right: 2px solid #f8bbd0; 
    }

    /* TUKAR NAMA PANITIA KAT TEPI JADI HITAM PEKAT */
    .stRadio > label { 
        color: #000000 !important; 
        font-weight: bold !important; 
        font-size: 20px !important;
    }

    /* KESAN HOVER PADA NAMA PANITIA */
    div[role="radiogroup"] label { 
        color: #000000 !important; 
        font-weight: 700 !important; 
        padding: 5px 10px;
        border-radius: 8px;
        transition: all 0.3s;
    }

    div[role="radiogroup"] label:hover { 
        background-color: #f8bbd0 !important; /* Warna pink bila cursor lalu */
        color: #ad1457 !important; /* Tulisan jadi merah hati sikit */
        cursor: pointer;
    }

    /* Kad Fail Induk - Kekal Putih Macam Asal Moon Nak */
    .card { 
        border-radius: 20px; 
        padding: 25px; 
        text-align: center; 
        color: white !important; 
        font-weight: bold; 
        height: 180px; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        margin-bottom: 15px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        transition: transform 0.3s; 
    }
    .card:hover { transform: scale(1.05); }
    
    /* Butang Dropdown & Tulisan Turquoise (Kekal) */
    .stExpander { background-color: #AED6F1 !important; border-radius: 12px !important; border: 1px solid #85C1E9 !important; }
    .stExpander details summary p { 
        color: #008080 !important; font-weight: 900; font-size: 22px; font-style: italic; text-align: center; margin: auto; width: 100%; transition: all 0.4s; 
    }
    .stExpander details summary:hover p { color: #004d4d !important; transform: scale(1.1); }

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

# 2. MENU SIDEBAR 11 PANITIA
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: black;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio(
        "Pilih Panitia:",
        ["REKA BENTUK & TEKNOLOGI (RBT)", "BAHASA MELAYU (BM)", "BAHASA INGGERIS (BI)", 
         "MATEMATIK", "SAINS", "PENDIDIKAN ISLAM", "SEJARAH", 
         "P. JASMANI & KESIHATAN", "PSV", "PENDIDIKAN MUZIK", "BAHASA ARAB"]
    )

# 3. PAPARAN UTAMA
st.markdown(f'<h1 class="main-title">📂 Portal Fail Digital Pengurusan Panitia <br>{pilihan}</h1>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

if pilihan == "REKA BENTUK & TEKNOLOGI (RBT)":
    with col1:
        st.markdown('<div class="card color-a"><div class="ref-no">600-4/1/2/1</div><div class="fail-title">🔵 FAIL A</div><br>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        with st.expander("FAIL A 👇"):
            st.markdown('<a class="sublink" href="https://docs.google.com/presentation/d/1b76mhH6fqiZSt48ARdrNyJulunexr_u7PZj4AFoq_Gc/edit?usp=sharing" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown('<a class="sublink" href="https://docs.google.com/presentation/d/18h4II0zdKX5IEZXhMRlxr89j-4CZdhRLuKdqrcR1118/edit?usp=drive_link" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card color-b"><div class="ref-no">600-4/1/2/2</div><div class="fail-title">🟠 FAIL B</div><br>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇"):
            st.markdown('<a class="sublink" href="https://drive.google.com/drive/folders/1KfhRHblLKPyn9VFLq0bwBEgeVPq_9PLP?usp=sharing" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card color-c"><div class="ref-no">600-4/1/2/3</div><div class="fail-title">🟣 FAIL C</div><br>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇"):
            st.markdown('<a class="sublink" href="https://drive.google.com/drive/folders/13ONhdCcHDgjo-pMYoMtyQUKqQc3XFGGh?usp=drive_link" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card color-d"><div class="ref-no">600-4/1/2/4</div><div class="fail-title">🟢 FAIL D</div><br>PEPERIKSAAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇"):
            st.markdown('<a class="sublink" href="https://drive.google.com/drive/folders/1sUR2Sq6fWbZk1gGveuRX935pqWkmUIgx?usp=sharing" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)
            st.markdown('<a class="sublink" href="https://drive.google.com/drive/folders/17-cMG1Orr1Q5oxbUBzKShiDSuMDyv8gH?usp=sharing" target="_blank">🏦 Bank Soalan 🔍</a>', unsafe_allow_html=True)
else:
    st.warning(f"Fail untuk Panitia {pilihan} belum dimuat naik.")

st.divider()
st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SKTB 2026</p>', unsafe_allow_html=True)
