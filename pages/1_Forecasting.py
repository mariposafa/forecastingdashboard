    with col_welcome2:
        st.markdown("""
        <div style="text-align: center; padding: 40px 20px; background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%); 
                    border-radius: 20px; border: 1px solid #e6d9ff; box-shadow: 0 10px 30px rgba(106, 17, 203, 0.1);">
            <div style="font-size: 3rem; margin-bottom: 20px;">📊</div>
            <div style="font-size: 2rem; font-weight: 700; color: #6A11CB; margin-bottom: 15px;">
                Selamat Datang di Sistem Forecasting JAPFA
            </div>
            <div style="font-size: 1.1rem; color: #666; line-height: 1.6; margin-bottom: 30px;">
                Platform forecasting profesional dengan algoritma setara Minitab.<br>
                Unggah data Anda untuk memulai forecasting permintaan yang akurat.
            </div>
            <div style="background: linear-gradient(135deg, #6A11CB 0%, #2575FC 100%); 
                        color: white; padding: 12px 30px; border-radius: 10px; 
                        display: inline-block; font-weight: 600; font-size: 1.1rem;">
                📤 Unggah File Excel untuk Memulai
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Features showcase
    st.markdown("## ✨ Fitur Utama")
    
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    
    with col_feat1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%); 
                    padding: 25px; border-radius: 15px; border: 1px solid #e6d9ff; 
                    text-align: center; height: 100%;">
            <div style="font-size: 2rem; color: #6A11CB; margin-bottom: 15px;">🎯</div>
            <div style="font-size: 1.2rem; font-weight: 600; color: #6A11CB; margin-bottom: 10px;">
                Optimasi Parameter Otomatis
            </div>
            <div style="color: #666; line-height: 1.5; font-size: 0.95rem;">
                Otomatis mencari parameter optimal untuk kedua algoritma SES dan MA
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_feat2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%); 
                    padding: 25px; border-radius: 15px; border: 1px solid #e6d9ff; 
                    text-align: center; height: 100%;">
            <div style="font-size: 2rem; color: #2575FC; margin-bottom: 15px;">📈</div>
            <div style="font-size: 1.2rem; font-weight: 600; color: #2575FC; margin-bottom: 10px;">
                Akurasi Setara Minitab
            </div>
            <div style="color: #666; line-height: 1.5; font-size: 0.95rem;">
                Kompatibilitas terjamin dengan standar akurasi statistik Minitab
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_feat3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%); 
                    padding: 25px; border-radius: 15px; border: 1px solid #e6d9ff; 
                    text-align: center; height: 100%;">
            <div style="font-size: 2rem; color: #9D4EDD; margin-bottom: 15px;">💾</div>
            <div style="font-size: 1.2rem; font-weight: 600; color: #9D4EDD; margin-bottom: 10px;">
                Laporan Komprehensif
            </div>
            <div style="color: #666; line-height: 1.5; font-size: 0.95rem;">
                Ekspor forecast detail, grafik, dan laporan analisis
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Data format instructions
    with st.expander("📋 **Persyaratan Format Data**", expanded=True):
        st.markdown("""
        ### Format Excel yang Diperlukan:
        
        **Struktur File:**
        - File Excel multi-sheet (.xlsx)
        - Setiap sheet berisi data untuk produk berbeda
        
        **Kolom yang Diperlukan:**
        ```csv
        produk,tanggal,permintaan
        CORN DDGS,2024-01-01,130000
        CORN DDGS,2024-01-02,0
        CORN DDGS,2024-01-03,145000
        ```
        
        **Deskripsi Kolom:**
        1. **produk** - Nama produk (teks)
        2. **tanggal** - Tanggal (format YYYY-MM-DD)
        3. **permintaan** - Permintaan harian dalam kilogram (numerik)
        
        **Catatan:** Nilai nol diperbolehkan dan akan ditangani dengan tepat dalam analisis.
        """)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #e6d9ff;">
        <div style="color: #666; font-size: 0.9rem;">
            Sistem Forecasting JAPFA v2.0 | Edisi Profesional<br>
            Didukung oleh Algoritma Statistik Tingkat Lanjut
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============ FOOTER =============
st.markdown("""
<div style="position: fixed; bottom: 0; left: 0; right: 0; background: linear-gradient(135deg, #6A11CB 0%, #2575FC 100%); 
            color: white; padding: 15px; text-align: center; font-size: 0.9rem; z-index: 999;">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>Sistem Forecasting JAPFA © 2025</div>
            <div>Status: <span style="font-weight: 600;">● Siap</span></div>
            <div>Akurasi: Setara Minitab</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
