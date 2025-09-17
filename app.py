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
    ### 🧩 STC Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [DataHub](https://stc-data.streamlit.app/)

    ---
    ### ☂ RANTAI Communities
    1. [Learn3](https://learn3.streamlit.app/)
    2. [BlockPedia](https://blockpedia.streamlit.app/)
    3. [SmartFaith](https://smartfaith.streamlit.app/)
    4. [Nexus](https://rantai-nexus.streamlit.app/)
    5. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    6. [Business Intelligence](https://rantai-busi.streamlit.app/)
    7. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    
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

def embed_iframe(src, hide_top_px=72, height=800):
    components.html(f"""
    <div style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:{height + hide_top_px}px; border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>
    """, height=height)

# URL Ohara
iframe_url = "https://ohara.ai/mini-apps/25307da3-8374-43e8-8615-e05d1e7c900a"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, height=800)
