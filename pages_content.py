"""
pages_content.py
-----------------
All static case-study content (text, tables, structured data) for the
GlowWise PM Case Study dashboard. Keeping this separate from app.py
means you can update copy without touching layout/rendering logic.
"""

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
HERO = {
    "tag": "⬡ Beauty-Tech · Sustainability · Consumer App",
    "title": "GlowWise — AI-Powered Sustainable Beauty Platform",
    "subtitle": (
        "A full product lifecycle case study — from user research to GTM — "
        "built to demonstrate real PM skills for FAANG-level interviews."
    ),
    "meta": [
        ("Product Type", "B2C Mobile App"),
        ("Market", "India + Global"),
        ("Timeline", "7-Week Project"),
        ("Role", "Product Manager (Solo)"),
        ("Target User", "Gen Z & Millennial Women"),
    ],
}

# ---------------------------------------------------------------------------
# PHASE 1 — PROBLEM DISCOVERY
# ---------------------------------------------------------------------------
DISCOVERY_STATS = [
    ("Interviews Conducted", "12", "Ages 18–32, urban India, beauty-conscious users"),
    ("Survey Respondents", "200", "Online survey via Google Forms — 3 cities"),
    ("Key Pain Point Rate", "78%", "Can't verify sustainability claims on product labels"),
]

QUOTES = [
    (
        "I want to buy clean beauty but I genuinely don't know what 'paraben-free' "
        "or 'cruelty-free' actually means on the label. There's too much greenwashing.",
        "Priya, 24, Software Engineer, Pune",
    ),
    (
        "I'd switch to sustainable brands if I knew what worked for my skin tone and "
        "type — but recommendations on Instagram are always for fair skin.",
        "Ananya, 27, MBA Student, Bengaluru",
    ),
    (
        "I've wasted ₹4,000+ on products that didn't work. I wish there was a way to "
        "scan a product and instantly know if it's safe and sustainable for me.",
        "Meera, 21, College Student, Mumbai",
    ),
]

# (label, percentage) — used by pain_points.py to render the survey chart
PAIN_POINTS = [
    ("Cannot verify sustainability claims", 78),
    ("Recommendations don't match skin tone/type", 71),
    ("Overwhelmed by too many product choices", 65),
    ("Wasted money on products that didn't work", 62),
    ("Distrust influencer/brand recommendations", 54),
]

PROBLEM_STATEMENT = (
    "Beauty-conscious Indian consumers (18–32F) struggle to identify genuinely "
    "sustainable, effective products suited to their unique skin profile — leading "
    "to wasted spend, decision paralysis, and distrust of brands. There is no "
    "trusted, personalized, AI-powered tool to help them shop sustainably with "
    "confidence."
)

# ---------------------------------------------------------------------------
# PHASE 2 — MARKET & COMPETITOR RESEARCH
# ---------------------------------------------------------------------------
MARKET_SIZING = [
    ("TAM — Global Clean Beauty", "$54B", "Global clean beauty market by 2027 (Statista 2023)"),
    ("SAM — India Beauty-Tech App", "$2.8B", "India beauty e-commerce + tech addressable (2024)"),
    ("SOM — Year 3 Target", "$48M", "~1.7% capture via 800K MAUs × ₹5K avg. annual spend"),
]

# columns: Product, AI Scan, Sustainability Score, India Skin-Type Match, Community, Gap
COMPETITORS = [
    ["Think Dirty", "✓ Yes", "✓ Yes", "✗ No", "✗ No", "US-centric, no personalization"],
    ["INCI Decoder", "Partial", "✗ No", "✗ No", "✗ No", "Technical, not consumer-friendly"],
    ["SkinKraft", "✗ No", "✗ No", "✓ Yes", "✗ No", "D2C only, no open marketplace"],
    ["Nykaa", "✗ No", "✗ No", "Basic", "Partial", "Commerce-first, not trust-first"],
    ["YUKA", "✓ Yes", "✓ Yes", "✗ No", "✗ No", "Food-first, limited beauty data"],
    ["GlowWise ★", "✓ Yes", "✓ Yes", "✓ Yes", "✓ Yes", "Full-stack differentiation"],
]
COMPETITOR_COLUMNS = [
    "Product", "AI Scan", "Sustainability Score",
    "India Skin-Type Match", "Community", "Gap",
]

MARKET_TAILWINDS = [
    "India's clean beauty market growing at **21% CAGR** (Grand View Research 2023)",
    "72% of Indian Gen Z willing to pay premium for sustainable products (Nielsen 2023)",
    "Beauty-tech app installs in India up **3.4× since 2021** (App Annie)",
]

OUR_MOAT = [
    "**AI ingredient scanner** — real-time barcode + label scan",
    "**India skin-tone model** — trained on South & Southeast Asian skin data",
    "**Eco-score algorithm** — proprietary 0–100 sustainability rating",
    "**Community reviews** — trust-verified peer recommendations",
]

# ---------------------------------------------------------------------------
# PHASE 3 — PRD & FEATURE PRIORITIZATION
# ---------------------------------------------------------------------------
PRODUCT_VISION = (
    "Empower every consumer to make beauty choices that are good for their skin "
    "and good for the planet — through AI, transparency, and community trust."
)

TARGET_USERS = [
    "Primary: Women 18–32, urban India, eco-conscious",
    "Secondary: Beauty enthusiasts globally seeking transparency",
    "Tertiary: Sustainable brands seeking discovery",
]

ASSUMPTIONS = [
    "Users will scan products at point of purchase",
    "60%+ will allow camera permission on first prompt",
    "Community content drives retention over AI alone",
]

USER_STORIES = [
    "As a user, I can scan a product barcode to see its Eco-Score instantly",
    "As a user, I can input my skin type/tone and get personalized recommendations",
    "As a user, I can see ingredient-level toxicity ratings in plain English",
    "As a user, I can browse a community-reviewed sustainable brand directory",
    "As a user, I can build a personalized \"clean shelfie\" and share it",
]

NON_GOALS = [
    "In-app e-commerce / checkout",
    "Male grooming vertical",
    "Hair care ingredient analysis",
]

# columns: Feature, Reach, Impact, Confidence, Effort (wks), RICE Score, Priority
RICE_SCORES = [
    ["AI Ingredient Scanner (Barcode)", 9, 3, "85%", "4 wks", 574, "P0 — Ship it"],
    ["Skin Profile Quiz + AI Match", 8, 3, "80%", "3 wks", 512, "P0 — Ship it"],
    ["Eco-Score Algorithm + Badge", 9, 2, "90%", "3 wks", 540, "P0 — Ship it"],
    ["Community Reviews + Trust Score", 7, 2, "75%", "5 wks", 210, "P1 — Next sprint"],
    ["\"Clean Shelfie\" Social Sharing", 6, 1, "70%", "2 wks", 210, "P1 — Next sprint"],
    ["Brand Sustainability Directory", 5, 2, "65%", "6 wks", 108, "P2 — Backlog"],
    ["AR Virtual Try-On", 4, 2, "50%", "12 wks", 33, "P3 — Future"],
]
RICE_COLUMNS = ["Feature", "Reach", "Impact", "Confidence", "Effort", "RICE Score", "Priority"]

ROADMAP = [
    ("Q1 — Months 1–3", "MVP Launch",
     "AI scanner, skin quiz, eco-score badge. iOS + Android beta (500 users)."),
    ("Q2 — Months 4–6", "Community + Virality",
     "Community reviews, clean shelfie sharing, referral program. Target 10K MAU."),
    ("Q3 — Months 7–9", "Brand Marketplace",
     "Sustainable brand directory, affiliate revenue, B2B brand dashboard."),
    ("Q4 — Months 10–12", "Scale & Monetize",
     "Premium subscription tier, global expansion (SEA), 100K MAU goal."),
]

# ---------------------------------------------------------------------------
# PHASE 4 — DESIGN & PROTOTYPE
# ---------------------------------------------------------------------------
DESIGN_PRINCIPLES = [
    ("Trust over beauty", "Every UI element must build transparency, not hide it."),
    ("Scan-first UX", "Camera should be one tap from any screen."),
    ("Plain English first", "No scientific jargon; translate for a 16-year-old."),
    ("Inclusive by default", "All 6 Fitzpatrick skin tones represented in AI model."),
]

CORE_FLOWS = [
    ("Onboarding", "Skin quiz (5 Q) → Profile built → First recommendation shown"),
    ("Scan Flow", "Tap camera → Scan barcode → Eco-Score + Ingredient breakdown → Save or Share"),
    ("Discovery Flow", "Browse category → Filter by eco-score → Community rating → Add to shelfie"),
]

USABILITY_ROUNDS = [
    ("Round 1", 62, "Task completion on scan flow (n=8). Key issue: camera permission prompt confusing."),
    ("Round 2", 81, "After redesigning permission prompt with value explanation. +19pp improvement."),
    ("Round 3", 94, "After simplifying ingredient labels to plain English. Ready for beta."),
]

SCAN_RESULT_MOCKUP = {
    "brand": "Lotus Herbals",
    "product": "Whiteglow SPF 25",
    "category": "Face Cream · 60g",
    "eco_score": 72,
    "ingredients": [
        ("Aloe Vera ✓", "good"),
        ("Niacinamide ✓", "good"),
        ("Titanium ⚠", "warn"),
        ("Parabens ✗", "bad"),
    ],
    "skin_match": (
        "⚠ Caution — Contains parabens, not ideal for your sensitive + oily "
        "profile. Try Minimalist SPF 50 instead."
    ),
}

# ---------------------------------------------------------------------------
# PHASE 5 — METRICS & SUCCESS CRITERIA
# ---------------------------------------------------------------------------
NORTH_STAR = {
    "name": "Weekly Scans per Active User",
    "description": (
        "This metric captures both product engagement (users returning to scan) "
        "and value delivery (users making informed decisions). A user who scans "
        "weekly is a user who trusts GlowWise for real decisions — not just a "
        "one-time download."
    ),
    "target": "≥3.5 scans/active user/week by Month 6",
}

OKRS = [
    {
        "objective": "Objective 1 — Build a product users love and trust",
        "krs": [
            "Achieve 4.5+ App Store rating within 90 days of launch (benchmark: category avg 3.8)",
            "Day-30 retention ≥ 40% (industry avg for beauty apps: 22%)",
            "NPS score ≥ 55 within 6 months of launch",
        ],
    },
    {
        "objective": "Objective 2 — Grow to 100K Monthly Active Users in 12 months",
        "krs": [
            "500 beta users in Month 1 → 10K MAU by Month 4 → 100K MAU by Month 12",
            "Referral rate ≥ 25% of new installs driven by in-app sharing",
            "CAC ≤ ₹80 per user via organic + community channels",
        ],
    },
    {
        "objective": "Objective 3 — Establish a sustainable revenue model",
        "krs": [
            "Launch GlowWise Pro (₹149/mo) with 5% MAU conversion by Month 9",
            "Sign 10 brand partnership agreements for premium eco-verified badge placement",
            "MRR of ₹25L+ by end of Year 1",
        ],
    },
]

# columns: Test Name, Hypothesis, Control, Variant, Primary Metric, Duration
AB_TESTS = [
    ["Onboarding Gate", "Showing eco-score before sign-up increases conversions",
     "Sign up first", "Scan 1 product, then sign up", "Sign-up rate", "2 weeks"],
    ["Score Framing", "Letter grade (A/B/C) increases scan engagement vs numeric",
     "Numeric 0–100", "Letter Grade A–F", "Scans/user/week", "3 weeks"],
    ["Shelfie CTA", "Social proof headline increases sharing rate",
     "\"Share your shelfie\"", "\"Join 8,400 users with clean shelfies\"", "Share click rate", "2 weeks"],
    ["Pro Upsell Timing", "Upsell after 5th scan converts better than on Day 3",
     "Day 3 prompt", "After 5th scan", "Pro conversion %", "4 weeks"],
]
AB_TEST_COLUMNS = ["Test Name", "Hypothesis", "Control", "Variant", "Primary Metric", "Duration"]

TARGET_METRICS = [
    ("Target D1 Retention", "55%", "vs 35% industry avg"),
    ("Target D30 Retention", "40%", "vs 22% beauty app avg"),
    ("Avg Scans / Week", "3.5", "North Star target M6"),
    ("Target NPS", "55+", "Promoter-class benchmark"),
]

# ---------------------------------------------------------------------------
# PHASE 6 — LAUNCH & GTM
# ---------------------------------------------------------------------------
GTM_PHASES = [
    ("🌱", "Pre-Launch (Weeks 1–4) — Seed the Community",
     "Partner with 30 micro-influencers (10K–80K followers) in sustainable beauty "
     "niche. Give early access to 500 waitlist users. Generate 50+ UGC posts "
     "pre-launch. Target: 5,000 waitlist signups before Day 1."),
    ("🚀", "Launch Week — Product Hunt + Press",
     "Launch on Product Hunt (target Top 5 of Day). Pitch to TechCrunch India, "
     "YourStory, Femina. Press angle: \"The app fighting greenwashing in India's "
     "₹1.3T beauty industry.\" Goal: 2,000 installs in Week 1."),
    ("🔁", "Month 2–3 — Referral Loop Activation",
     "Launch \"Invite 3 friends, unlock GlowWise Pro for 1 month free.\" Every "
     "shelfie share includes app deep-link. Target: 25% of new installs from "
     "referral within 60 days of launch."),
    ("🤝", "Month 4–6 — Brand Partnerships",
     "Onboard 10 certified sustainable brands (Forest Essentials, Mamaearth, "
     "Plum) as \"GlowWise Verified\" partners. Revenue: ₹50K–₹2L/month per brand "
     "for eco-verification badge + featured placement."),
]

GTM_CHANNELS = [
    ("Primary Channel", "Micro-Influencer UGC",
     "Sustainable beauty creators. Cost: ₹2K–8K per post. Target CAC: ₹45/user from this channel."),
    ("Secondary Channel", "Community + Referral",
     "In-app referral loop + Reddit/Facebook sustainable beauty groups. CAC target: ₹12/user (near-zero cost)."),
    ("Revenue Model", "Freemium + B2B",
     "Free tier (5 scans/day) → Pro ₹149/mo (unlimited + AI tips). + Brand partnership revenue."),
]

# columns: Stakeholder, Interest, Communication, Frequency
STAKEHOLDERS = [
    ["Engineering Team", "Sprint scope, technical dependencies", "Weekly sprint review + Slack", "Weekly"],
    ["Design Team", "UX decisions, usability results", "Design review session + Figma comments", "Bi-weekly"],
    ["Investors / Founders", "MAU growth, revenue, North Star", "Monthly product metrics dashboard", "Monthly"],
    ["Brand Partners", "User reach, eco-badge placement", "Quarterly impact report", "Quarterly"],
    ["Users (Beta)", "Feature updates, bug fixes", "In-app changelog + email digest", "Weekly"],
]
STAKEHOLDER_COLUMNS = ["Stakeholder", "Interest", "Communication", "Frequency"]

# ---------------------------------------------------------------------------
# PHASE 7 — CASE STUDY & PORTFOLIO
# ---------------------------------------------------------------------------
RESUME_BULLETS = [
    "Led end-to-end product discovery for GlowWise — a beauty-tech sustainability "
    "app — conducting 12 user interviews and a 200-person survey, identifying that "
    "78% of Indian consumers cannot verify sustainability claims on beauty products.",
    "Authored a full Product Requirements Document (PRD) covering vision, user "
    "personas, 7 user stories, and a RICE-scored feature backlog; deprioritized 2 "
    "high-effort features saving ~14 engineering weeks.",
    "Designed and tested 3 rounds of lo-fi prototypes (Figma), improving core task "
    "completion rate from 62% → 94% by applying plain-English ingredient labeling "
    "based on usability feedback (n=8 per round).",
    "Defined North Star metric (Weekly Scans per Active User), set OKRs targeting "
    "100K MAU in 12 months, and built a 4-test A/B experimentation roadmap covering "
    "onboarding, score framing, and upsell timing.",
    "Built a go-to-market strategy targeting ₹48M SOM via micro-influencer seeding "
    "(CAC ₹45), in-app referral loop (CAC ₹12), and brand partnership revenue — "
    "projecting MRR of ₹25L+ by end of Year 1.",
]

INTERVIEW_QA = [
    ("Tell me about a product you built. Walk me through your process.",
     "Use the STAR + PM framework: Situation (78% of users can't verify "
     "sustainability) → Task (build a trusted AI scanner) → Action (PRD, RICE "
     "prioritization, 3 usability test rounds) → Result (94% task completion, "
     "clear path to 100K MAU). Reference specific data at every step."),
    ("How did you prioritize features?",
     "Explain RICE scoring: used Reach × Impact × Confidence ÷ Effort. The AI "
     "Ingredient Scanner scored 574 (P0) vs AR Try-On at 33 (P3) — making it easy "
     "to defend cutting the \"exciting\" feature in favor of the high-trust, "
     "high-reach one."),
    ("What metrics would you use to measure success?",
     "North Star: Weekly Scans per Active User — because it measures both "
     "engagement and real decision-making. Supporting KPIs: D30 retention (40% "
     "target vs 22% avg), NPS (55+), CAC (≤₹80). Then explain the A/B test plan "
     "for the upsell timing experiment."),
    ("How big is this market and why does it matter?",
     "TAM: $54B global clean beauty by 2027. SAM: $2.8B India beauty-tech. SOM: "
     "$48M in Year 3 (~1.7% capture via 800K MAU). Back it up: 21% CAGR in India, "
     "72% of Gen Z willing to pay premium for sustainability (Nielsen 2023)."),
]

PORTFOLIO_CHECKLIST = [
    "This case study document (PDF export)",
    "Figma prototype link (shareable)",
    "PRD as a Google Doc (clean, formatted)",
    "User interview notes / survey data (Notion)",
    "RICE prioritization spreadsheet",
    "3-min Loom walkthrough video",
]

FOOTER_NOTE = "All data sourced from Statista, Nielsen, Grand View Research, App Annie 2023–2024"
