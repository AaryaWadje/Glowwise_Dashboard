"""
pain_points.py
--------------
Chart builder for the Phase 01 (Problem Discovery) survey results.
Kept separate from the other chart helpers because this is the
highest-traffic visual in the case study and gets iterated on most.
"""

import plotly.graph_objects as go


def build_pain_points_chart(pain_points: list[tuple[str, int]]) -> go.Figure:
    """
    Build a horizontal bar chart of survey pain-point percentages.

    Args:
        pain_points: list of (label, percentage) tuples, e.g.
            [("Cannot verify sustainability claims", 78), ...]

    Returns:
        A Plotly Figure ready to be passed to st.plotly_chart().
    """
    labels = [p[0] for p in pain_points]
    values = [p[1] for p in pain_points]

    # Color gradient: highest pain points get the strongest color
    colors = []
    for v in values:
        if v >= 70:
            colors.append("#2D4A3E")   # forest
        elif v >= 60:
            colors.append("#B8860B")   # gold
        else:
            colors.append("#C4736A")   # rose

    fig = go.Figure(
        go.Bar(
            x=values,
            y=labels,
            orientation="h",
            marker_color=colors,
            text=[f"{v}%" for v in values],
            textposition="outside",
            hovertemplate="%{y}: %{x}%<extra></extra>",
        )
    )

    fig.update_layout(
        xaxis=dict(range=[0, 100], title="% of respondents", showgrid=True, gridcolor="#EDE8DF"),
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=10, b=10),
        height=320,
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", size=13, color="#1A1A1A"),
        showlegend=False,
    )
    return fig
