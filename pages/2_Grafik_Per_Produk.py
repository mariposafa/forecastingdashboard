import streamlit as st
import matplotlib.pyplot as plt
from utils import load_multisheet_excel
import numpy as np
import pandas as pd
from datetime import datetime

# ============ CUSTOM THEME - PURPLE ELEGANCE =============
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f8f4ff 0%, #f0ebff 50%, #e8e0ff 100%) !important;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    /* Title styling dengan gradien */
    h1, h2, h3 {
        font-weight: 600 !important;
    }
    
    h1 {
        background: linear-gradient(90deg, #6A11CB 0%, #2575FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border-bottom: 3px solid #9D4EDD;
        padding-bottom: 15px;
        margin-bottom: 30px !important;
    }
    
    h2 {
        color: #7B2CBF !important;
        border-left: 4px solid #9D4EDD;
        padding-left: 15px;
        margin-top: 25px !important;
    }
    
    /* Elegant file uploader */
    .stFileUploader {
        border: 2px dashed #9D4EDD !important;
        border-radius: 15px !important;
        padding: 30px !important;
        background: rgba(157, 78, 221, 0.05) !important;
        transition: all 0.3s ease !important;
    }
    
    .stFileUploader:hover {
        background: rgba(157, 78, 221, 0.1) !important;
        border-color: #6A11CB !important;
    }
    
    /* Elegant selectbox */
    .stSelectbox [data-baseweb="select"] {
        border-radius: 12px !important;
        border: 1px solid #e6d9ff !important;
        background: white !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox [data-baseweb="select"]:hover {
        border-color: #9D4EDD !important;
        box-shadow: 0 2px 10px rgba(106, 17, 203, 0.1);
    }
    
    /* Elegant stats cards */
    .stat-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #e6d9ff;
        box-shadow: 0 6px 20px rgba(106, 17, 203, 0.1);
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(106, 17, 203, 0.15);
        border-color: #9D4EDD;
    }
    
    .stat-value {
        color: #2D1B69 !important;
        font-size: 28px !important;
        font-weight: 700 !important;
        margin-bottom: 8px !important;
    }
    
    .stat-label {
        color: #6A11CB !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    
    /* Elegant buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6A11CB 0%, #2575FC 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 28px !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 6px 20px rgba(106, 17, 203, 0.2) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(106, 17, 203, 0.3) !important;
        background: linear-gradient(135deg, #5a0db8 0%, #1c68f0 100%) !important;
    }
    
    /* Color picker styling */
    [data-testid="stColorPicker"] {
        border-radius: 10px !important;
        border: 1px solid #e6d9ff !important;
        padding: 10px !important;
    }
    
    /* Slider styling */
    .stSlider [data-baseweb="slider"] [data-baseweb="track"] {
        background-color: #e6d9ff !important;
        height: 8px !important;
        border-radius: 4px !important;
    }
    
    .stSlider [data-baseweb="slider"] [data-baseweb="thumb"] {
        background-color: #6A11CB !important;
        border: 4px solid white !important;
        box-shadow: 0 2px 10px rgba(106, 17, 203, 0.3) !important;
    }
    
    /* Checkbox styling */
    .stCheckbox > label {
        font-weight: 500 !important;
        color: #5A189A !important;
    }
    
    /* Elegant alert boxes */
    .stAlert {
        border-radius: 12px !important;
        border: 1px solid !important;
        background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%) !important;
    }
    
    .stAlert [data-baseweb="notification"] {
        border: none !important;
        background: transparent !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f4ff 0%, #f0ebff 100%) !important;
        border-radius: 12px !important;
        border: 1px solid #e6d9ff !important;
        color: #6A11CB !important;
        font-weight: 600 !important;
    }
    
    /* Elegant divider */
    .elegant-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #9D4EDD, transparent);
        margin: 30px 0;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f0ebff;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #6A11CB 0%, #2575FC 100%);
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ============ HEADER SECTION =============
st.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1 style="font-size: 2.8rem; margin-bottom: 10px;">📊 Grafik Tren Permintaan</h1>
    <p style="font-size: 1.2rem; color: #666; max-width: 800px; margin: 0 auto 30px; line-height: 1.6;">
        Visualisasi interaktif untuk analisis pola permintaan produk dengan <span style="color: #6A11CB; font-weight: 600;">kustomisasi lengkap</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ============ FILE UPLOAD SECTION =============
st.markdown("### 📤 Unggah Data Excel")
uploaded_file = st.file_uploader(
    "Pilih file Excel",
    type=["xlsx"],
    help="Unggah file Excel multi-sheet dengan kolom: produk, tanggal, permintaan",
    label_visibility="collapsed"
)

# ============ MAIN CONTENT =============
if uploaded_file:
    try:
        # Load data
        df = load_multisheet_excel(uploaded_file)
        
        # Product selection in elegant layout
        col_header1, col_header2, col_header3 = st.columns([1, 2, 1])
        
        with col_header2:
            produk_list = df["produk"].unique()
            if len(produk_list) > 0:
                produk = st.selectbox(
                    "Pilih Produk untuk Analisis",
                    produk_list,
                    help="Pilih produk yang ingin dianalisis tren permintaannya"
                )
            else:
                st.warning("⚠️ Tidak ada data produk ditemukan dalam file")
                st.stop()
        
        # Data preparation
        data = df[df["produk"] == produk].sort_values("tanggal")
        data = data.reset_index(drop=True)
        
        # ============ STATISTICS CARDS =============
        st.markdown("### 📈 Statistik Permintaan")
        
        total_permintaan = data["permintaan"].sum()
        rata_rata = data["permintaan"].mean()
        max_permintaan = data["permintaan"].max()
        min_permintaan = data["permintaan"].min()
        n_zeros = (data["permintaan"] == 0).sum()
        zero_percentage = (n_zeros / len(data)) * 100
        
        col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
        
        with col_stat1:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{len(data):,}</div>
                <div class="stat-label">Total Data</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_stat2:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{total_permintaan:,.0f}</div>
                <div class="stat-label">Total Permintaan</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_stat3:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{rata_rata:,.0f}</div>
                <div class="stat-label">Rata-rata Harian</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_stat4:
            trend_color = "#00C853" if rata_rata > 0 else "#FF9800"
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{max_permintaan:,.0f}</div>
                <div class="stat-label">Puncak Permintaan</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional mini stats
        col_mini1, col_mini2 = st.columns(2)
        
        with col_mini1:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Permintaan Minimum</div>
                <div class="stat-value">{min_permintaan:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_mini2:
            zero_color = "#FF9800" if zero_percentage > 20 else "#4CAF50"
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Hari Tanpa Permintaan</div>
                <div class="stat-value">{n_zeros}</div>
                <div style="color: {zero_color}; font-size: 12px; font-weight: 600; margin-top: 5px;">
                    ({zero_percentage:.1f}% dari total)
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # ============ GRAPH CUSTOMIZATION =============
        st.markdown("### ⚙️ Kustomisasi Grafik")
        
        with st.expander("Pengaturan Visualisasi", expanded=True):
            col_set1, col_set2, col_set3 = st.columns(3)
            
            with col_set1:
                line_color = st.color_picker(
                    "🎨 Warna Garis Utama",
                    value="#6A11CB",
                    help="Pilih warna untuk garis tren utama"
                )
                
                marker_style = st.selectbox(
                    "🔘 Style Marker",
                    ["○ Bulat", "□ Kotak", "△ Segitiga", "◇ Belah Ketupat", "Tidak ada"],
                    index=0,
                    help="Pilih bentuk marker pada setiap data point"
                )
                
                # Map selection to matplotlib markers
                marker_map = {
                    "○ Bulat": "o",
                    "□ Kotak": "s",
                    "△ Segitiga": "^",
                    "◇ Belah Ketupat": "D",
                    "Tidak ada": None
                }
                marker = marker_map[marker_style]
            
            with col_set2:
                line_width = st.slider(
                    "📏 Ketebalan Garis",
                    min_value=1,
                    max_value=5,
                    value=3,
                    help="Atur ketebalan garis grafik"
                )
                
                grid_intensity = st.slider(
                    "🔲 Intensitas Grid",
                    min_value=0.0,
                    max_value=1.0,
                    value=0.3,
                    step=0.1,
                    help="Atur transparansi grid background"
                )
            
            with col_set3:
                show_grid = st.checkbox("Tampilkan Grid", value=True)
                show_zero_points = st.checkbox("Sorot Hari Kosong", value=True)
                smooth_line = st.checkbox("Garis Halus", value=False)
        
        # ============ CREATE ELEGANT GRAPH =============
        st.markdown("### 📊 Visualisasi Tren")
        
        # Create figure with elegant styling
        plt.style.use('seaborn-v0_8-whitegrid')
        fig, ax = plt.subplots(figsize=(14, 7))
        
        # Set background colors
        fig.patch.set_facecolor('#f8f4ff')
        ax.set_facecolor('#ffffff')
        
        # Prepare data
        dates = data["tanggal"]
        values = data["permintaan"]
        
        if smooth_line and len(data) > 1:
            # Add smoothed line (simple moving average for visualization)
            window = min(5, len(values) // 4)
            if window > 1:
                smoothed = values.rolling(window=window, center=True).mean()
                ax.plot(dates, smoothed, color=line_color, linewidth=line_width+1, 
                       alpha=0.7, linestyle='--', label='Trend Halus')
        
        # Plot the main line
        ax.plot(
            dates, 
            values, 
            marker=marker,
            color=line_color,
            linewidth=line_width,
            markersize=8 if marker else 0,
            markerfacecolor='white',
            markeredgecolor=line_color,
            markeredgewidth=2,
            label=f"Permintaan {produk}",
            zorder=3
        )
        
        # Highlight zero values if requested
        if show_zero_points and n_zeros > 0:
            zero_data = data[data["permintaan"] == 0]
            ax.scatter(
                zero_data["tanggal"],
                zero_data["permintaan"],
                color='#FF5722',
                s=120,
                marker='X',
                linewidths=3,
                zorder=4,
                alpha=0.8,
                label=f'Hari Tanpa Permintaan ({n_zeros})',
                edgecolors='white'
            )
        
        # Highlight peak demand
        max_idx = data["permintaan"].idxmax()
        if not pd.isna(max_idx):
            ax.scatter(
                data.loc[max_idx, "tanggal"],
                data.loc[max_idx, "permintaan"],
                color='#FFD700',
                s=200,
                marker='*',
                zorder=5,
                label=f'Puncak: {data.loc[max_idx, "permintaan"]:,.0f} kg',
                edgecolors='#B8860B',
                linewidths=2
            )
        
        # Customize the plot with elegant styling
        ax.set_xlabel("Tanggal", fontsize=13, fontweight='bold', color='#333', labelpad=15)
        ax.set_ylabel("Permintaan (kg)", fontsize=13, fontweight='bold', color='#333', labelpad=15)
        
        ax.set_title(
            f"Analisis Tren Permintaan - {produk}",
            fontsize=18,
            fontweight='bold',
            color='#6A11CB',
            pad=25,
            loc='left'
        )
        
        # Format y-axis
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))
        
        # Rotate and style x-axis
        plt.xticks(rotation=45, fontsize=11)
        plt.yticks(fontsize=11)
        
        # Add grid if requested
        if show_grid:
            ax.grid(True, alpha=grid_intensity, linestyle='--', color='#9D4EDD', linewidth=0.5)
        
        # Add legend with elegant styling
        legend = ax.legend(
            loc='upper left',
            fontsize=11,
            framealpha=0.95,
            shadow=True,
            fancybox=True,
            facecolor='white',
            edgecolor='#e6d9ff',
            borderpad=1
        )
        legend.get_frame().set_linewidth(1.5)
        
        # Add subtle border to plot
        for spine in ax.spines.values():
            spine.set_edgecolor('#e6d9ff')
            spine.set_linewidth(2)
        
        # Add watermark
        ax.text(
            0.98, 0.02, 
            f'JAPFA Analytics • {datetime.now().strftime("%d %b %Y")}',
            transform=ax.transAxes,
            fontsize=9,
            color='#9D4EDD',
            alpha=0.5,
            ha='right',
            va='bottom'
        )
        
        plt.tight_layout()
        
        # Display the plot
        st.pyplot(fig)
        
        # ============ INSIGHTS SECTION =============
        st.markdown('<div class="elegant-divider"></div>', unsafe_allow_html=True)
        st.markdown("### 💡 Insights Analisis")
        
        # Calculate trends
        if len(data) > 1:
            # Simple trend calculation
            first_half = data["permintaan"].iloc[:len(data)//2].mean()
            second_half = data["permintaan"].iloc[len(data)//2:].mean()
            trend_direction = "Meningkat" if second_half > first_half else "Menurun"
            trend_percentage = abs((second_half - first_half) / first_half * 100) if first_half > 0 else 0
            
            # Find date ranges
            date_range = f"{data['tanggal'].min().strftime('%d %b %Y')} - {data['tanggal'].max().strftime('%d %b %Y')}"
            
            col_ins1, col_ins2 = st.columns(2)
            
            with col_ins1:
                st.success(f"""
                **📅 Periode Analisis:** {date_range}
                
                **📈 Tren Utama:** Permintaan **{trend_direction.lower()}** sebesar **{trend_percentage:.1f}%**
                
                **⚡ Karakteristik Data:**
                - Rentang data: **{max_permintaan:,.0f} kg** (tertinggi) hingga **{min_permintaan:,.0f} kg** (terendah)
                - Variasi harian: **±{(data['permintaan'].std() / rata_rata * 100):.1f}%** dari rata-rata
                """)
            
            with col_ins2:
                if n_zeros > 0:
                    st.warning(f"""
                    **⚠️ Perhatian Khusus:**
                    
                    Terdapat **{n_zeros} hari** tanpa permintaan ({zero_percentage:.1f}% dari total)
                    
                    **Rekomendasi:**
                    1. Periksa data hari tanpa permintaan
                    2. Validasi apakah terjadi gangguan operasional
                    3. Pertimbangkan dalam perencanaan inventori
                    """)
                else:
                    st.info(f"""
                    **✅ Konsistensi Data:**
                    
                    Tidak ada hari tanpa permintaan selama periode analisis
                    
                    **📊 Stabilitas Permintaan:**
                    - Standar deviasi: **{data['permintaan'].std():,.0f} kg**
                    - Koefisien variasi: **{(data['permintaan'].std() / rata_rata * 100):.1f}%**
                    """)
        
        # ============ DOWNLOAD GRAPH OPTION =============
        st.markdown("### 💾 Ekspor Hasil")
        
        col_dl1, col_dl2, col_dl3 = st.columns([2, 1, 1])
        
        with col_dl1:
            st.info("Grafik dapat disimpan sebagai gambar PNG untuk laporan atau presentasi.")
        
        with col_dl2:
            # Save figure to buffer for download
            import io
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
            buf.seek(0)
            
            st.download_button(
                label="📥 Download Grafik (PNG)",
                data=buf,
                file_name=f"grafik_tren_{produk.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.png",
                mime="image/png",
            )
        
        with col_dl3:
            if st.button("🔄 Buat Grafik Baru", use_container_width=True):
                st.rerun()
    
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat memproses data: {str(e)}")
        st.info("Pastikan format file Excel sesuai dengan template yang ditentukan.")

else:
    # ============ LANDING PAGE =============
    st.markdown("""
    <div style="
        text-align: center; 
        padding: 50px 30px; 
        background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%);
        border-radius: 20px;
        border: 2px solid #e6d9ff;
        box-shadow: 0 10px 40px rgba(106, 17, 203, 0.1);
        margin: 30px 0;
    ">
        <div style="font-size: 80px; color: #6A11CB; margin-bottom: 20px;">📈</div>
        <h2 style="color: #6A11CB; margin-bottom: 15px; font-size: 32px;">
            Analisis Visual Tren Permintaan
        </h2>
        <p style="color: #666; max-width: 700px; margin: 0 auto 30px; line-height: 1.7; font-size: 16px;">
            Platform analisis visual untuk memahami pola dan tren permintaan produk. 
            Upload data Excel Anda dan dapatkan insight visual yang powerful untuk pengambilan keputusan.
        </p>
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 15px;
            background: linear-gradient(135deg, #6A11CB 0%, #2575FC 100%);
            color: white;
            padding: 15px 35px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 18px;
            margin-top: 10px;
        ">
            📁 Unggah File Excel untuk Memulai
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features showcase
    st.markdown("## ✨ Fitur Analisis Grafik")
    
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    
    with col_feat1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%); 
                    padding: 25px; border-radius: 16px; border: 1px solid #e6d9ff; 
                    text-align: center; height: 100%;">
            <div style="font-size: 2.5rem; color: #6A11CB; margin-bottom: 15px;">🎨</div>
            <div style="font-size: 1.2rem; font-weight: 600; color: #6A11CB; margin-bottom: 10px;">
                Kustomisasi Lengkap
            </div>
            <div style="color: #666; line-height: 1.5;">
                Pilih warna, marker, dan gaya grafik sesuai kebutuhan presentasi
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_feat2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%); 
                    padding: 25px; border-radius: 16px; border: 1px solid #e6d9ff; 
                    text-align: center; height: 100%;">
            <div style="font-size: 2.5rem; color: #2575FC; margin-bottom: 15px;">📊</div>
            <div style="font-size: 1.2rem; font-weight: 600; color: #2575FC; margin-bottom: 10px;">
                Statistik Real-time
            </div>
            <div style="color: #666; line-height: 1.5;">
                Analisis statistik lengkap dengan visualisasi card yang informatif
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_feat3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 100%); 
                    padding: 25px; border-radius: 16px; border: 1px solid #e6d9ff; 
                    text-align: center; height: 100%;">
            <div style="font-size: 2.5rem; color: #9D4EDD; margin-bottom: 15px;">💡</div>
            <div style="font-size: 1.2rem; font-weight: 600; color: #9D4EDD; margin-bottom: 10px;">
                Insights Otomatis
            </div>
            <div style="color: #666; line-height: 1.5;">
                Deteksi pola dan berikan rekomendasi berdasarkan analisis data
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============ FOOTER =============
st.markdown("""
<div style="
    position: fixed; 
    bottom: 0; 
    left: 0; 
    right: 0; 
    background: linear-gradient(135deg, #6A11CB 0%, #2575FC 100%); 
    color: white; 
    padding: 15px; 
    text-align: center; 
    font-size: 0.9rem;
    z-index: 999;
">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>Sistem Analisis Grafik JAPFA © 2025</div>
            <div>Status: <span style="font-weight: 600;">● Aktif</span></div>
            <div>Mode: Visualisasi Tren</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)