# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Import our custom modules
import resume_data
import sources_data
import conclusions_data  # <-- NEW IMPORT
import visualize_pipeline
import visualize_regulatory
import visualize_safety
import visualize_kol
import visualize_financials
import visualize_geo
import visualize_pricing
import visualize_trials
import visualize_wac
import visualize_nadac
import visualize_openfda

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Vladimir Korobov | Commercial Analytics", layout="wide")

st.markdown("""
    <style>
        .main-slogan {
            font-size: 60px;
            font-weight: 700;
            color: #2C3E50;
            text-align: center;
            margin-top: 40px;
            margin-bottom: 60px;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .source-box {
            background-color: #F8F9FA;
            padding: 20px;
            border-left: 5px solid #2980B9;
            margin-bottom: 15px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)


# --- DATA LOADING ---
@st.cache_data
def load_data():
    try:
        df_pipeline = pd.read_csv("adalimumab_pipeline_intelligence.csv")
        df_regulatory = pd.read_excel("adalimumab_regulatory_timeline.xlsx")
        df_safety = pd.read_csv("adalimumab_safety_profile.csv")
        df_kol = pd.read_csv("adalimumab_kol_mapping.csv")
        df_financial = pd.read_csv("adalimumab_real_financial_intelligence.csv")
        df_geo = pd.read_csv("adalimumab_global_footprint.csv")
        df_pricing = pd.read_csv("adalimumab_real_medicare_pricing.csv")
        df_trials = pd.read_excel("Adalimumab_Chart_Data.xlsx")
        df_wac = pd.read_excel("wac-increase-5-year-history-mar-2026.xlsx")
        df_nadac = pd.read_csv("Adalimumab_NADAC_Cleaned.csv")
        df_openfda = pd.read_excel("Adalimumab_Complete_FDA_Data.xlsx")

        return df_pipeline, df_regulatory, df_safety, df_kol, df_financial, df_geo, df_pricing, df_trials, df_wac, df_nadac, df_openfda
    except FileNotFoundError:
        st.error("Data files not found. Please ensure all datasets are in the directory.")
        return [None] * 11


p1, p2, p3, p4, p5, p_geo, p_pricing, df_trials, df_wac, df_nadac, df_openfda = load_data()

# Load text content from data modules
resume = resume_data.get_resume_content()
sources = sources_data.get_sources_content()
conclusions = conclusions_data.get_conclusions()  # <-- LOAD CONCLUSIONS DICT

# --- TOP NAVIGATION TABS ---
tab_about, tab_adalimumab, tab_sources = st.tabs(["About Me", "Adalimumab", "Sources"])

# --- TAB 1: ABOUT ME ---
with tab_about:
    st.markdown(f'<div class="main-slogan" style="font-size: 60px;">{resume["slogan"]}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.header(resume["header"])
        st.write("---")
        st.write(resume["intro"])

        st.subheader("Professional Experience")
        # st.write(resume["experience"]["title"])
        for bullet in resume["experience"]["bullets"]:
            st.write(f"* {bullet}")

        st.subheader("Education")
        for bullet in resume["education"]["bullets"]:
            st.write(f"* {bullet}")

# --- TAB 2: ADALIMUMAB CASE STUDY ---
with tab_adalimumab:
    st.header("Adalimumab: Data Analytics Training Project")
    st.write("A non-professional case study focused on practicing data extraction, processing, and visualization.")
    st.write("This project is an educational exercise designed to demonstrate technical workflows using open-source pharmaceutical data. This research is inherently incomplete and is intended purely for training purposes. It does not provide professional pharmaceutical analysis or conclusions.")
    st.write("---")

    # 0. GLOBAL WHITE SPACE MAP
    if p_geo is not None:
        st.subheader("Global Clinical Trial Footprint (White Space Analysis)")
        st.write("Mapping trial density to identify regional saturation.")
        fig_map = visualize_geo.create_geo_map(p_geo)
        st.plotly_chart(fig_map, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["geo_map"])
        st.write("---")

    # 1. PIPELINE
    if p1 is not None:
        st.subheader("Biosimilar Pipeline Intelligence")
        fig1 = visualize_pipeline.create_pipeline_chart(p1)
        st.plotly_chart(fig1, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["pipeline"])
        st.write("---")

    # 1.5 CLINICAL TRIAL EFFICIENCY
    if df_trials is not None:
        st.subheader("Late-Stage Pipeline Execution & Efficiency")
        st.write("Evaluating Phase 3/4 trial execution timelines and patient enrollment velocity.")
        col_trial1, col_trial2 = st.columns(2)
        with col_trial1:
            fig_gantt = visualize_trials.create_gantt_chart(df_trials)
            st.plotly_chart(fig_gantt, width="stretch")
        with col_trial2:
            fig_scatter = visualize_trials.create_efficiency_scatter(df_trials)
            st.plotly_chart(fig_scatter, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["clinical_trials"])
        st.write("---")

    # 2. REGULATORY
    if p2 is not None:
        st.subheader("FDA Regulatory Timeline & Interchangeability")
        fig2 = visualize_regulatory.create_regulatory_chart(p2)
        st.plotly_chart(fig2, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["regulatory"])
        st.write("---")

    # 3. SAFETY
    if p3 is not None:
        st.subheader("Real-World Safety Profile (FAERS)")
        fig3 = visualize_safety.create_safety_chart(p3)
        st.plotly_chart(fig3, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["safety"])
        st.write("---")

    # 4. KOL INFLUENCE
    if p4 is not None:
        st.subheader("Share of Scientific Voice")
        fig4 = visualize_kol.create_kol_chart(p4)
        st.plotly_chart(fig4, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["kol"])
        st.write("---")

    # 5. FINANCIALS
    if p5 is not None:
        st.subheader("Manufacturer Financial Strategy")
        colA, colB = st.columns(2)
        with colA:
            fig5a = visualize_financials.create_spend_pie_chart(p5)
            st.plotly_chart(fig5a, width="stretch")
        with colB:
            fig5b = visualize_financials.create_physician_bar_chart(p5)
            st.plotly_chart(fig5b, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["financials"])
        st.write("---")

    # 6. MEDICARE PRICING
    if p_pricing is not None:
        st.subheader("Medicare Spending & Lifecycle Management (2019-2023)")
        st.write("Verified open-source data extracted from the CMS Medicare Part D Spending ledger.")
        col_price1, col_price2 = st.columns(2)
        with col_price1:
            fig_rev = visualize_pricing.create_spending_bar_chart(p_pricing)
            st.plotly_chart(fig_rev, width="stretch")
        with col_price2:
            fig_cost = visualize_pricing.create_cost_line_chart(p_pricing)
            st.plotly_chart(fig_cost, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["medicare"])
        st.write("---")

    # 7. WAC HISTORY
    if df_wac is not None:
        st.subheader("Adalimumab WAC (Wholesale Acquisition Cost) History")
        st.write("Tracking historical list price increases prior to biosimilar market entry.")
        fig_wac = visualize_wac.create_wac_chart(df_wac)
        st.plotly_chart(fig_wac, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["wac"])
        st.write("---")

    # 8. NADAC PRICING
    if df_nadac is not None:
        st.subheader("Real Pharmacy Acquisition Costs (NADAC) for Adalimumab Products")
        st.write("Tracking the actual acquisition costs paid by retail pharmacies for Adalimumab products.")
        fig_nadac = visualize_nadac.create_nadac_scatter(df_nadac)
        st.plotly_chart(fig_nadac, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["nadac"])
        st.write("---")

    # 9. OPENFDA ECOSYSTEM
    if df_openfda is not None:
        st.subheader("The Adalimumab Biosimilar Market Ecosystem in the US (Based on open source: openFDA)")
        st.write(
            "Mapping the hierarchical market structure from labeler to product NDC using live-extracted FDA metadata.")
        fig_openfda = visualize_openfda.create_openfda_sunburst(df_openfda)
        st.plotly_chart(fig_openfda, width="stretch")

        # Inject dynamic conclusion
        st.info(conclusions["openfda"])
        st.write("---")

# --- TAB 3: SOURCES ---
with tab_sources:
    st.header("Data Sources & Methodology")
    # st.write(sources["intro"])

    for source in sources["sources"]:
        st.markdown(f"### [{source['name']}]({source['link']})")
        st.write(source['description'])
        st.divider()
