from cgitb import text
import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import Font

# ==========================================================
# Repository Health Comparison
# ==========================================================
PLOT_LAYOUT = dict(

    template="plotly_dark",

    paper_bgcolor="#172033",
    plot_bgcolor="#172033",

    font=dict(
        family="Inter",
        size=11,
        color="white"
    ),

    margin=dict(
        l=15,
        r=15,
        t=45,
        b=15
    ),

    height=300,

    legend=dict(
        orientation="h",
        y=-0.20,
        x=0,
        font=dict(color="white")
    ),

    xaxis=dict(
        gridcolor="#2B3652",
        zerolinecolor="#2B3652",
        color="white"
    ),

    yaxis=dict(
        gridcolor="#2B3652",
        zerolinecolor="#2B3652",
        color="white"
    )
)

def health_chart(df):

    fig = px.bar(
        df,
        x="repository_health_score",
        y="repo_full_name",
        orientation="h",
        text="repository_health_score",
        color="repository_health_score",
        color_continuous_scale=["#3B82F6","#60A5FA","#93C5FD"])
    fig.update_layout(title="Repository Health Score",**PLOT_LAYOUT)
    fig.update_traces(texttemplate="%{text:.1f}")
    fig.update_layout(
    paper_bgcolor="#172033",
    plot_bgcolor="#172033"
)

    fig.update_xaxes(
        showline=False,
        zeroline=False
    )

    fig.update_yaxes(
        showline=False,
        zeroline=False
    )
    return fig


# ==========================================================
# Pull Request Analytics
# ==========================================================

def pull_request_chart(df):
    metrics = ["merge_rate","approval_rate","change_request_rate"]
    fig = go.Figure()
    for _, row in df.iterrows():
        fig.add_trace(go.Bar(name=row["repo_full_name"],x=metrics,y=[row["merge_rate"],row["approval_rate"],row["change_request_rate"]]))
    fig.update_layout(barmode="group",title="Pull Request Analytics",**PLOT_LAYOUT)
    fig.update_traces(marker_color=["#3B82F6", "#60A5FA"],marker_line_width=0)
    fig.update_layout(
    paper_bgcolor="#172033",
    plot_bgcolor="#172033"
    )

    fig.update_xaxes(
        showline=False,
        zeroline=False
    )

    fig.update_yaxes(
        showline=False,
        zeroline=False
    )
    return fig

# ==========================================================
# Issue Analytics
# ==========================================================

def issue_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Issues",x=df["repo_full_name"],y=df["issue_closure_rate"]))
    fig.update_layout(title="Issue Closure Rate",yaxis_title="Percentage",**PLOT_LAYOUT)
    fig.update_traces(marker_color="#F59E0B",marker_line_width=0)
    fig.update_layout(
    paper_bgcolor="#172033",
    plot_bgcolor="#172033"
    )

    fig.update_xaxes(
        showline=False,
        zeroline=False
    )

    fig.update_yaxes(
        showline=False,
        zeroline=False
    )
    return fig


# ==========================================================
# Contributor Analytics
# ==========================================================

def contributor_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Average Contributions",x=df["repo_full_name"],y=df["avg_contributions"]))
    fig.update_layout(title="Contributor Activity",**PLOT_LAYOUT)
    fig.update_traces(marker_color="#10B981",marker_line_width=0)
    fig.update_layout(
    paper_bgcolor="#172033",
    plot_bgcolor="#172033"
    )

    fig.update_xaxes(
        showline=False,
        zeroline=False
    )

    fig.update_yaxes(
        showline=False,
        zeroline=False
    )
    return fig


# ==========================================================
# Workflow Analytics
# ==========================================================

def workflow_chart(df):

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Workflow Success",x=df["repo_full_name"],y=df["workflow_success_rate"]))
    fig.update_layout(title="Workflow Success Rate",yaxis_title="Percentage",**PLOT_LAYOUT)
    fig.update_traces(marker_color="#8B5CF6",marker_line_width=0)
    fig.update_layout(
        paper_bgcolor="#172033",
        plot_bgcolor="#172033"
    )

    fig.update_xaxes(
        showline=False,
        zeroline=False
        
    )

    fig.update_yaxes(
        showline=False,
        zeroline=False
    )
    return fig


# ==========================================================
# Radar Chart
# ==========================================================

def radar_chart(df):
    categories = ["repository_health_score","merge_rate","issue_closure_rate","workflow_success_rate","approval_rate"]
    fig = go.Figure()
    for _, row in df.iterrows():
        fig.add_trace(
            go.Scatterpolar(
                r=[row["repository_health_score"],row["merge_rate"],row["issue_closure_rate"],row["workflow_success_rate"],row["approval_rate"]],
                theta=["Health","Merge","Issues","Workflow","Reviews"],fill="toself",name=row["repo_full_name"])
        )
    fig.update_layout(
        polar=dict(bgcolor="#172033",
    radialaxis=dict(visible=True,range=[0,100],gridcolor="#2B3652",linecolor="#2B3652",tickfont=dict(color="white")),
    angularaxis=dict(tickfont=dict(color="white"),gridcolor="#2B3652")))
    fig.update_layout(
    paper_bgcolor="#172033",
    plot_bgcolor="#172033"
)

    fig.update_xaxes(
        showline=False,
        zeroline=False
    )

    fig.update_yaxes(
        showline=False,
        zeroline=False
    )
    return fig