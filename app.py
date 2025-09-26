import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RANTAI BUSI",
    page_icon="💰",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **RANTAI BUSI** adalah modul Business Intelligence (BI) yang menyediakan dashboard interaktif dan laporan real-time untuk membantu pengguna bisnis memantau kinerja, tren, dan indikator kunci secara mudah dan cepat. Dengan integrasi data yang solid dan visualisasi yang intuitif, BI memungkinkan pengambilan keputusan yang lebih efisien dan berbasis data.
    
    ---
    #### 🔮 Vision Statement
    
    Menjadi solusi BI terdepan yang memberikan wawasan bisnis realtime, praktis, dan dapat diakses oleh semua level organisasi, mendorong keputusan cerdas yang memacu pertumbuhan berkelanjutan.

    ---
    ### 🌐 RANTAI Pipeline
    
    Keempat modul—EDA, BI, Predictive Modeling, dan ETHIKA—bekerja bersama sebagai bagian dari siklus analitik data yang saling terintegrasi, memastikan alur data dan insight yang mulus dari awal hingga akhir dengan keseimbangan etika dan fairness sebagai pijakan utama.
    
    - Exploratory Data Analysis (EDA) merupakan langkah awal yang mempersiapkan dan memvalidasi data mentah. Dengan analisis statistik dan visualisasi eksploratif, EDA mengidentifikasi pola, anomali, dan kualitas data yang akan menjadi dasar untuk tahap selanjutnya.
    
    - Business Intelligence (BI) menerima data yang sudah bersih dan terstruktur dari EDA untuk membangun dashboard interaktif dan laporan. BI fokus menyediakan visualisasi realtime yang mudah dipahami dan mendukung pengambilan keputusan bisnis secara cepat dan terukur.
    
    - Predictive Modeling (PM) menggunakan data yang sudah tervalidasi dan insight dari BI untuk membuat model prediktif. Output model ini dapat dikembalikan ke dashboard BI untuk memberikan prediksi dan rekomendasi, melengkapi insight historis dengan analisis masa depan.

    - Etika, Bias, Hukum, dan Agama hadir sebagai modul check & balance dalam pipeline ini, mendeteksi ketidakseimbangan dataset dan mengevaluasi fairness model. ETHIKA tidak hanya memberi peringatan bias, tetapi juga mendorong refleksi etis dan tanggung jawab sosial dalam setiap tahapan pengembangan model, memastikan hasil analitik layak secara moral dan sosial untuk digunakan.
    
    > 💡 Pipeline ini membentuk siklus data yang berkelanjutan: dari pemahaman awal (EDA), ke reporting yang actionable (BI), hingga keputusan proaktif berbasis prediksi (PM), serta keseimbangan etika dan fairness (ETHIKA), mendukung keputusan bisnis yang lebih cerdas, responsif, dan bertanggung jawab.
    
    ---
    ### 🧩 STC Ecosystem
    
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [STC CarbonPrint](https://stc-carbonprint.streamlit.app/)
    9. [STC ImpactViz](https://stc-impactviz.streamlit.app/)
    10. [DataHub](https://stc-data.streamlit.app/)

    ---
    ### ⛓ RANTAI Communities

    > 💡 RANTAI Communities adalah ekosistem apps eksperimental berbasis Web3 & AI untuk riset, kolaborasi, dan inovasi. Dibangun di atas 3 core: Dev → Build, Net → Connect, Lab → Grow.
    
    🔧 Dev → “Build the chain”
    1. [Numerical Methods Lab](https://metnumlab.streamlit.app/)
    2. [Computational Analytics Studio](https://komnumlab.streamlit.app/)
    3. [BlockPedia](https://blockpedia.streamlit.app/)
    4. [Learn3](https://learn3.streamlit.app/)
    5. [LearnPy](https://rantai-learnpy.streamlit.app/)
    6. [Cruise](https://rantai-cruise.streamlit.app/)
    7. [IndustriX](https://rantai-industrix.streamlit.app/)

    🌐 Net → “Connect the chain”
    1. [SmartFaith](https://smartfaith.streamlit.app/)
    2. [Nexus](https://rantai-nexus.streamlit.app/)
    3. [Decentralized Supply Chain](https://rantai-trace.streamlit.app/)
    4. [ESG Compliance Manager](https://rantai-sentinel.streamlit.app/)
    5. [Decentralized Storage Optimizer](https://rantai-greenstorage.streamlit.app/)
    6. [Cloud Carbon Footprint Tracker](https://rantai-greencloud.streamlit.app/)
    7. [Cloud.Climate.Chain](https://rantai-3c.streamlit.app/)
    8. [Property Management System](https://rantai-pms.streamlit.app/)
    
    🌱 Lab → “Grow the chain”
    1. [BlockBook](https://blockbook.streamlit.app/)
    2. [Data Insights & Visualization Assistant](https://rantai-diva.streamlit.app/)
    3. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    4. [Business Intelligence](https://rantai-busi.streamlit.app/)
    5. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    6. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    7. [Smart Atlas For Environment](https://rantai-safe.streamlit.app/)
    8. [Blockchain Healthcare Revolution](https://healthchain.streamlit.app/)
    9. [Academic Flow Diagram Generator](https://mermaind.streamlit.app/)
    10. [Decentralized Agriculture](https://agroviz.streamlit.app/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/rantai-busi)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

# URL Ohara
iframe_url = "https://ohara.ai/mini-apps/miniapp_cmfpb44hq01pe8hnx6onpfy4i"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, hide_bottom_px = 25, height=800)
