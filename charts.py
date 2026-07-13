"""
charts.py
---------
Reusable Plotly chart builders for the other case-study phases
(market sizing funnel, RICE prioritization, usability testing progress,
and target-metric gauges). Kept separate from pain_points.py since
that module is specific to the Discovery-phase survey chart.
"""

import plotly.graph_objects as go

FOREST = "#2D4A3E"
GOLD = "#B8860B"
ROSE = "#C4736A"
SAND = "#EDE8DF"
CHARCOAL = "#1A1A1A"


def build_market_funnel(tam: float, sam: float, som: float,
                         labels=("TAM", "SAM", "SOM")) -> go.Figure:
    """Build a TAM → SAM → SOM funnel chart (values in $B)."""
    fig = go.Figure(
        go.Funnel(
            y=list(labels),
            x=[tam, sam, som],
            textinfo="value+percent initial",
            marker=dict(color=[FOREST, GOLD, ROSE]),
        )
    )
    fig.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        height=320,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", size=13, color=CHARCOAL),
    )
    return fig


def build_rice_chart(rows: list, columns: list) -> go.Figure:
    """
    Build a horizontal bar chart of RICE scores.
    rows: list of lists matching `columns` order, expects
          "Feature" and "RICE Score" among the columns.
    """
    feature_idx = columns.index("Feature")
    score_idx = columns.index("RICE Score")
    priority_idx = columns.index("Priority")

    sorted_rows = sorted(rows, key=lambda r: r[score_idx], reverse=True)
    features = [r[feature_idx] for r in sorted_rows]
    scores = [r[score_idx] for r in sorted_rows]
    priorities = [r[priority_idx] for r in sorted_rows]

    def color_for(priority):
        if "P0" in priority:
            return FOREST
        if "P1" in priority:
            return GOLD
        if "P2" in priority:
            return "#4A7FBF"
        return ROSE

    colors = [color_for(p) for p in priorities]

    fig = go.Figure(
        go.Bar(
            x=scores,
            y=features,
            orientation="h",
            marker_color=colors,
            text=scores,
            textposition="outside",
            hovertemplate="%{y}<br>RICE Score: %{x}<extra></extra>",
        )
    )
    fig.update_layout(
        xaxis=dict(title="RICE Score", showgrid=True, gridcolor=SAND),
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=10, b=10),
        height=380,
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", size=13, color=CHARCOAL),
        showlegend=False,
    )
    return fig


def build_usability_chart(rounds: list) -> go.Figure:
    """
    rounds: list of (round_name, completion_pct, note) tuples.
    Rendered as a simple progress line/bar showing improvement across rounds.
    """
    names = [r[0] for r in rounds]
    values = [r[1] for r in rounds]

    fig = go.Figure(
        go.Bar(
            x=names,
            y=values,
            marker_color=[ROSE, GOLD, FOREST][: len(names)],
            text=[f"{v}%" for v in values],
            textposition="outside",
        )
    )
    fig.update_layout(
        yaxis=dict(range=[0, 100], title="Task completion %", showgrid=True, gridcolor=SAND),
        margin=dict(l=10, r=10, t=10, b=10),
        height=300,
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", size=13, color=CHARCOAL),
        showlegend=False,
    )
    return fig
