# 🌿 GlowWise — PM Case Study Dashboard

An interactive Streamlit dashboard version of a full product-management case
study for **GlowWise**, a fictional AI-powered sustainable beauty app built to
demonstrate real PM skills (discovery → market research → PRD → design →
metrics → GTM → portfolio prep).

This was originally a single static HTML page and has been converted into a
multi-section Streamlit app with live charts (Plotly) instead of static bars.

## 🖥️ Live Demo

Once deployed, add your Streamlit Cloud URL here:
`https://<your-app-name>.streamlit.app`

## 📁 Project Structure

```
.
├── app.py                  # Main Streamlit entry point — page routing & layout
├── pages_content.py        # All static case-study text/data (quotes, tables, OKRs, etc.)
├── pain_points.py          # Chart builder for the Phase 01 survey pain-points bar chart
├── charts.py               # Chart builders for market funnel, RICE scores, usability tests
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Theme (colors/fonts) for the app
├── .gitignore
└── README.md
```

## 🧭 What's in the dashboard

| Phase | Section |
|---|---|
| 00 | Overview / Hero |
| 01 | Problem Discovery — interviews, survey, pain-point chart |
| 02 | Market & Competitor Research — TAM/SAM/SOM funnel, competitor teardown |
| 03 | PRD & Feature Prioritization — RICE scoring, roadmap |
| 04 | Design & Prototype — design principles, usability test results |
| 05 | Metrics & OKRs — North Star metric, OKRs, A/B test plan |
| 06 | Launch & GTM Strategy — phased rollout, channels, stakeholder plan |
| 07 | Portfolio & Interview Prep — resume bullets, FAANG-style Q&A |

## 🚀 Run locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## ☁️ Deploy on Streamlit Community Cloud

1. Push this folder to a **public GitHub repository**.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"**, then select:
   - **Repository:** `<your-username>/<your-repo-name>`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Deploy**. Streamlit Cloud will install `requirements.txt`
   automatically and give you a public URL like
   `https://your-app-name.streamlit.app`.

No secrets or API keys are required — this app only uses static content and
local chart rendering.

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io) — app framework
- [Plotly](https://plotly.com/python/) — interactive charts
- [Pandas](https://pandas.pydata.org) — table rendering

## ✏️ Editing content

All case-study copy (quotes, RICE scores, OKRs, GTM phases, etc.) lives in
**`pages_content.py`** as plain Python lists/dicts — update the values there
and the dashboard updates automatically. Chart logic lives separately in
**`pain_points.py`** (Discovery survey chart) and **`charts.py`** (market
funnel, RICE chart, usability chart) so layout and data stay decoupled.

## 📊 Data Sources

All market/industry figures referenced in this case study are cited from
Statista, Nielsen, Grand View Research, and App Annie (2023–2024) for
illustrative, educational purposes as part of a PM practice project.

## 📄 License

This project is shared for educational/portfolio purposes. Feel free to fork
and adapt it for your own PM case studies.
