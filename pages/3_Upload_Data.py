import streamlit as st
from utils import load_multisheet_excel
import pandas as pd
from datetime import datetime

# ============ SIMPLE PURPLE THEME =============
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f8f4ff 0%, #f0ebff 100%);
    }
    
    h1, h2, h3 {
        color: #6A11CB !important;
        font-weight: 600 !important;
    }
    
    .stFileUploader {
        border: 2px dashed #9D4EDD !important;
        border-radius: 15px !important;
        padding: 30px !important;
        background: rgba(157, 78, 221, 0.05) !important;
    }
    
    .stFileUploader:hover {
        background: rgba(157, 78, 221, 0.1) !important;
        border-color: #6A11CB !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #6A11CB 0%, #9D4EDD 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
    }
    
    .stats-card {
        background: white;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #e6d9ff;
        box-shadow: 0 4px 12px rgba(106, 17, 203, 0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ============ HEADER =============
st.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1 style="font-size: 2.2rem; margin-bottom: 10px;">📁 Upload & Preview Data</h1>
    <p style="color: #666; font-size: 1rem;">
        Unggah file Excel untuk analisis forecasting dan visualisasi
    </p>
</div>
""", unsafe_allow_html=True)

# ============ FILE UPLOAD =============
st.markdown("### 📤 Unggah File Excel")
uploaded_file = st.file_uploader(
    "Pilih file Excel (.xlsx)",
    type=["xlsx"],
    help="Format: produk, tanggal, permintaan",
    label_visibility="collapsed"
)

# ============ MAIN CONTENT =============
if uploaded_file:
    try:
        df = load_multisheet_excel(uploaded_file)
        
        # Display success message
        st.success(f"✅ File berhasil diupload! ({uploaded_file.name})")
        
        # Quick stats in columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="stats-card">
                <div style="font-size: 12px; color: #6A11CB; font-weight: 600;">Total Data</div>
                <div style="font-size: 24px; font-weight: 700; color: #2D1B69;">{len(df):,}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stats-card">
                <div style="font-size: 12px; color: #6A11CB; font-weight: 600;">Jumlah Produk</div>
                <div style="font-size: 24px; font-weight: 700; color: #2D1B69;">{df['produk'].nunique()}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            date_range = f"{df['tanggal'].min().strftime('%d/%m')} - {df['tanggal'].max().strftime('%d/%m/%Y')}"
            st.markdown(f"""
            <div class="stats-card">
                <div style="font-size: 12px; color: #6A11CB; font-weight: 600;">Periode Data</div>
                <div style="font-size: 14px; font-weight: 600; color: #2D1B69;">{date_range}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Preview table with limited rows
        st.markdown("### 👁️ Preview Data (10 baris pertama)")
        st.dataframe(
            df.head(10),
            use_container_width=True,
            height=350
        )
        
        # Product list
        st.markdown("### 📦 Daftar Produk")
        produk_list = df['produk'].unique()
        for i, produk in enumerate(produk_list[:5]):  # Show first 5
            data_produk = df[df['produk'] == produk]
            st.write(f"**{i+1}. {produk}** - {len(data_produk)} data poin")
        
        if len(produk_list) > 5:
            st.caption(f"...dan {len(produk_list) - 5} produk lainnya")
        
        # Download button
        st.markdown("### 💾 Download Data")
        col_dl1, col_dl2 = st.columns(2)
        
        with col_dl1:
            csv_data = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download sebagai CSV",
                data=csv_data,
                file_name=f"data_japfa_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col_dl2:
            if st.button("📊 Lanjut ke Analisis", use_container_width=True):
                st.switch_page("pages/1_Forecasting.py")
    
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {str(e)}")
        st.info("Pastikan file Excel sesuai format dengan kolom: produk, tanggal, permintaan")

else:
    # ============ LANDING PAGE =============
    st.markdown("""
    <div style="
        text-align: center; 
        padding: 40px 20px; 
        background: white;
        border-radius: 15px;
        border: 2px dashed #9D4EDD;
        margin: 30px 0;
    ">
        <div style="font-size: 60px; color: #6A11CB; margin-bottom: 15px;">📁</div>
        <h3 style="color: #6A11CB; margin-bottom: 15px;">Upload File Excel Anda</h3>
        <p style="color: #666; max-width: 600px; margin: 0 auto 20px;">
            Seret file ke area di atas atau klik untuk memilih file Excel (.xlsx)
        </p>
        <div style="color: #9D4EDD; font-weight: 600; font-size: 14px;">
            Format yang didukung: Excel dengan kolom produk, tanggal, permintaan
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick guide
    with st.expander("📋 Format Data yang Dibutuhkan"):
        st.markdown("""
        ### Kolom dalam Excel:
        
        | Kolom | Format | Contoh |
        |-------|--------|--------|
        | **produk** | Text | CORN DDGS, SOY MEAL |
        | **tanggal** | Date (YYYY-MM-DD) | 2024-01-01 |
        | **permintaan** | Number (kg) | 150000 |
        
        ### Tips:
        - File harus .xlsx
        - Nama kolom harus tepat
        - Tanggal dalam format standar
        - Nilai nol diperbolehkan
        """)

# ============ FOOTER =============
st.markdown("""
<div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #e6d9ff; color: #666;">
    <div style="font-size: 12px;">
        Sistem Upload Data JAPFA © 2025 | Dikembangkan oleh Kelompok 17 APTEK
    </div>
</div>
""", unsafe_allow_html=True)