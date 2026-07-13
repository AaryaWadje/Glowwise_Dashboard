"""
app.py
------
GlowWise — PM Case Study Dashboard
A Streamlit port of the original static HTML case study, turned into an
interactive, navigable dashboard with charts.

Run locally:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd

import pages_content as c
from pain_points import build_pain_points_chart
from charts import build_market_funnel, build_rice_chart, build_usability_chart

# ---------------------------------------------------------------------------
# PAGE CONFIG + THEME
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="GlowWise — PM Case Study",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

FOREST = "#2D4A3E"
GOLD = "#B8860B"
CREAM = "#FAF7F2"
SAND = "#EDE8DF"

CUSTOM_CSS = f"""
<style>
    .stApp {{ background-color: {CREAM}; }}
    h1, h2, h3 {{ font-family: 'Georgia', serif; color: {FOREST}; }}
    .metric-card {{
        background: white; border: 1px solid {SAND}; border-radius: 12px;
        padding: 18px; border-left: 4px solid {FOREST};
    }}
    .quote-block {{
        background: {SAND}; border-left: 4px solid {GOLD};
        border-radius: 0 8px 8px 0; padding: 16px 20px; margin: 10px 0;
        font-style: italic;
    }}
    .section-badge {{
        display:inline-block; background:{FOREST}; color:white;
        padding:4px 12px; border-radius:20px; font-size:12px;
        font-weight:600; letter-spacing:.05em; margin-bottom:8px;
    }}
    div[data-testid="stMetric"] {{
        background: white; border: 1px solid {SAND}; border-radius: 12px;
        padding: 14px; border-left: 4px solid {FOREST};
    }}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------------------------
PAGES = [
    "🏠 Overview",
    "🔍 Phase 01 — Discovery",
    "📊 Phase 02 — Market Research",
    "📝 Phase 03 — PRD & Prioritization",
    "🎨 Phase 04 — Design & Prototype",
    "📈 Phase 05 — Metrics & OKRs",
    "🚀 Phase 06 — GTM Strategy",
    "💼 Phase 07 — Portfolio & Interview Prep",
]

st.sidebar.markdown(f"## 🌿 Glow<span style='color:{GOLD}'>Wise</span>", unsafe_allow_html=True)
st.sidebar.caption("PM Case Study Dashboard")
page = st.sidebar.radio("Navigate", PAGES, label_visibility="collapsed")
st.sidebar.divider()
st.sidebar.caption(c.FOOTER_NOTE)

# ---------------------------------------------------------------------------
# OVERVIEW / HERO
# ---------------------------------------------------------------------------
if page == "🏠 Overview":
    st.markdown(f"<span class='section-badge'>{c.HERO['tag']}</span>", unsafe_allow_html=True)
    st.title(c.HERO["title"])
    st.write(c.HERO["subtitle"])

    cols = st.columns(len(c.HERO["meta"]))
    for col, (label, value) in zip(cols, c.HERO["meta"]):
        with col:
            st.metric(label, value)

    st.divider()
    st.subheader("What's in this case study")
    st.write(
        "Use the sidebar to move through all seven phases of the product "
        "lifecycle — from user research through go-to-market strategy and "
        "interview prep. Each phase mirrors a real PM workflow."
    )
    phase_names = [p.split("— ", 1)[-1] if "—" in p else p.replace("🏠 ", "")
                   for p in PAGES]
    st.write(" → ".join(phase_names[1:]))

# ---------------------------------------------------------------------------
# PHASE 01 — DISCOVERY
# ---------------------------------------------------------------------------
elif page == "🔍 Phase 01 — Discovery":
    st.markdown("<span class='section-badge'>Phase 01</span>", unsafe_allow_html=True)
    st.title("Problem Discovery")
    st.write(
        "I conducted 12 user interviews (ages 18–32) and a survey of 200 "
        "respondents across India. The core insight: consumers want to make "
        "sustainable beauty choices but lack the tools to do so confidently."
    )

    cols = st.columns(3)
    for col, (label, value, sub) in zip(cols, c.DISCOVERY_STATS):
        with col:
            st.metric(label, value, help=sub)

    st.subheader("User Interview Quotes")
    for quote, attr in c.QUOTES:
        st.markdown(
            f"<div class='quote-block'>\"{quote}\"<br>"
            f"<span style='font-style:normal;font-size:13px;color:#6B6560;'>— {attr}</span></div>",
            unsafe_allow_html=True,
        )

    st.subheader("Survey Results — Top Pain Points")
    st.plotly_chart(build_pain_points_chart(c.PAIN_POINTS), use_container_width=True)

    st.subheader("Problem Statement")
    st.info(c.PROBLEM_STATEMENT)

# ---------------------------------------------------------------------------
# PHASE 02 — MARKET RESEARCH
# ---------------------------------------------------------------------------
elif page == "📊 Phase 02 — Market Research":
    st.markdown("<span class='section-badge'>Phase 02</span>", unsafe_allow_html=True)
    st.title("Market & Competitor Research")
    st.write(
        "Market sizing using TAM→SAM→SOM funnel, plus competitive teardown "
        "of 5 existing players to identify our moat."
    )

    cols = st.columns(3)
    for col, (label, value, sub) in zip(cols, c.MARKET_SIZING):
        with col:
            st.metric(label, value, help=sub)

    tam, sam, som = 54, 2.8, 0.048  # $B, extracted from MARKET_SIZING values
    st.plotly_chart(build_market_funnel(tam, sam, som), use_container_width=True)

    st.subheader("Competitive Teardown")
    df = pd.DataFrame(c.COMPETITORS, columns=c.COMPETITOR_COLUMNS)
    st.dataframe(df, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Market Tailwinds 📈**")
        for item in c.MARKET_TAILWINDS:
            st.markdown(f"- {item}")
    with col2:
        st.markdown("**Our Moat 🛡️**")
        for item in c.OUR_MOAT:
            st.markdown(f"- {item}")

# ---------------------------------------------------------------------------
# PHASE 03 — PRD & PRIORITIZATION
# ---------------------------------------------------------------------------
elif page == "📝 Phase 03 — PRD & Prioritization":
    st.markdown("<span class='section-badge'>Phase 03</span>", unsafe_allow_html=True)
    st.title("PRD & Feature Prioritization")
    st.write(
        "A structured Product Requirements Document covering goals, users, "
        "features, constraints, and success metrics — plus RICE-scored "
        "prioritization."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Product Vision**")
        st.write(c.PRODUCT_VISION)
        st.markdown("**Target Users**")
        for item in c.TARGET_USERS:
            st.markdown(f"- {item}")
        st.markdown("**Assumptions**")
        for item in c.ASSUMPTIONS:
            st.markdown(f"- {item}")
    with col2:
        st.markdown("**User Stories (Must-Have)**")
        for item in c.USER_STORIES:
            st.markdown(f"- {item}")
        st.markdown("**Non-Goals (v1.0)**")
        for item in c.NON_GOALS:
            st.markdown(f"- {item}")

    st.subheader("Feature Prioritization — RICE Scoring")
    st.caption("RICE Score = (Reach × Impact × Confidence) ÷ Effort")
    st.plotly_chart(build_rice_chart(c.RICE_SCORES, c.RICE_COLUMNS), use_container_width=True)
    df = pd.DataFrame(c.RICE_SCORES, columns=c.RICE_COLUMNS)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Product Roadmap")
    for quarter, title, desc in c.ROADMAP:
        st.markdown(f"**{quarter} — {title}**  \n{desc}")

# ---------------------------------------------------------------------------
# PHASE 04 — DESIGN & PROTOTYPE
# ---------------------------------------------------------------------------
elif page == "🎨 Phase 04 — Design & Prototype":
    st.markdown("<span class='section-badge'>Phase 04</span>", unsafe_allow_html=True)
    st.title("Design & Prototype")
    st.write(
        "Key user flows, wireframe decisions, and design principles. "
        "Prototyped in Figma with 3 rounds of usability testing (n=8 each)."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Design Principles**")
        for title, desc in c.DESIGN_PRINCIPLES:
            st.markdown(f"- **{title}** — {desc}")
    with col2:
        st.markdown("**Core User Flows**")
        for title, desc in c.CORE_FLOWS:
            st.markdown(f"- **{title}:** {desc}")

    st.subheader("Product Scan Result — Mockup")
    m = c.SCAN_RESULT_MOCKUP
    with st.container(border=True):
        cols = st.columns([1, 2])
        with cols[0]:
            st.metric("Eco Score", f"{m['eco_score']}/100", "GOOD ✓")
        with cols[1]:
            st.markdown(f"**{m['brand']}** — {m['product']}  \n{m['category']}")
        tag_cols = st.columns(len(m["ingredients"]))
        for tc, (label, status) in zip(tag_cols, m["ingredients"]):
            with tc:
                st.markdown(f"`{label}`")
        st.caption(m["skin_match"])

    st.subheader("Usability Testing Progress")
    st.plotly_chart(build_usability_chart(c.USABILITY_ROUNDS), use_container_width=True)
    cols = st.columns(3)
    for col, (round_name, pct, note) in zip(cols, c.USABILITY_ROUNDS):
        with col:
            st.metric(f"Usability Test — {round_name}", f"{pct}%", help=note)

# ---------------------------------------------------------------------------
# PHASE 05 — METRICS & OKRS
# ---------------------------------------------------------------------------
elif page == "📈 Phase 05 — Metrics & OKRs":
    st.markdown("<span class='section-badge'>Phase 05</span>", unsafe_allow_html=True)
    st.title("Metrics & Success Criteria")
    st.write(
        "Defined the North Star metric, full KPI stack, OKRs for Year 1, "
        "and A/B testing plan — structured exactly as expected in FAANG PM "
        "interviews."
    )

    with st.container(border=True):
        st.markdown("**North Star Metric**")
        st.markdown(f"### {c.NORTH_STAR['name']}")
        st.write(c.NORTH_STAR["description"])
        st.success(f"Target: {c.NORTH_STAR['target']}")

    st.subheader("OKRs — Year 1")
    for okr in c.OKRS:
        with st.expander(okr["objective"], expanded=True):
            for kr in okr["krs"]:
                st.markdown(f"- {kr}")

    st.subheader("A/B Testing Plan")
    df = pd.DataFrame(c.AB_TESTS, columns=c.AB_TEST_COLUMNS)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Target Metrics")
    cols = st.columns(4)
    for col, (label, value, sub) in zip(cols, c.TARGET_METRICS):
        with col:
            st.metric(label, value, help=sub)

# ---------------------------------------------------------------------------
# PHASE 06 — GTM STRATEGY
# ---------------------------------------------------------------------------
elif page == "🚀 Phase 06 — GTM Strategy":
    st.markdown("<span class='section-badge'>Phase 06</span>", unsafe_allow_html=True)
    st.title("Launch & Go-To-Market Strategy")
    st.write(
        "A phased GTM strategy combining community seeding, influencer "
        "validation, and earned media — designed for low CAC and organic "
        "virality."
    )

    for icon, title, desc in c.GTM_PHASES:
        with st.container(border=True):
            st.markdown(f"### {icon} {title}")
            st.write(desc)

    st.subheader("Channels & Revenue")
    cols = st.columns(3)
    for col, (label, title, desc) in zip(cols, c.GTM_CHANNELS):
        with col:
            st.markdown(f"**{label}**")
            st.markdown(f"##### {title}")
            st.caption(desc)

    st.subheader("Stakeholder Communication Plan")
    df = pd.DataFrame(c.STAKEHOLDERS, columns=c.STAKEHOLDER_COLUMNS)
    st.dataframe(df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# PHASE 07 — PORTFOLIO & INTERVIEW PREP
# ---------------------------------------------------------------------------
elif page == "💼 Phase 07 — Portfolio & Interview Prep":
    st.markdown("<span class='section-badge'>Phase 07</span>", unsafe_allow_html=True)
    st.title("Case Study & Portfolio")
    st.write(
        "How to present this project in your resume, FAANG applications, "
        "and PM interviews — with exact language and storytelling "
        "frameworks."
    )

    st.subheader("Resume Bullet Points (Copy-Paste Ready)")
    for bullet in c.RESUME_BULLETS:
        st.markdown(f"▸ {bullet}")

    st.subheader("FAANG Interview Answer Preparation")
    for q, a in c.INTERVIEW_QA:
        with st.expander(f"Q: {q}"):
            st.write(a)

    st.subheader("What to Include in Your Portfolio")
    cols = st.columns(2)
    for i, item in enumerate(c.PORTFOLIO_CHECKLIST):
        with cols[i % 2]:
            st.checkbox(item, value=True, disabled=True, key=f"portfolio_{i}")

st.divider()
st.caption("GlowWise · A complete PM case study · Beauty-Tech × Sustainability")
st.caption(c.FOOTER_NOTE)
