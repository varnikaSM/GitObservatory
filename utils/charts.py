import plotly.graph_objects as go
import plotly.express as px

# ==========================================================
# Repository Health Comparison
# ==========================================================
TEMPLATE = "plotly_white"
PLOT_LAYOUT = dict(
    template=TEMPLATE,
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(family="Inter",size=13),
    margin=dict(l=15,r=15,t=40,b=15))
    
def health_chart(df):

    fig = px.bar(
        df,
        x="repository_health_score",
        y="repo_full_name",
        orientation="h",
        text="repository_health_score",
        color="repository_health_score",
        color_continuous_scale="Blues")
    fig.update_layout(title="Repository Health Score",**PLOT_LAYOUT)
    fig.update_traces(texttemplate="%{text:.1f}")
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
    return fig

# ==========================================================
# Issue Analytics
# ==========================================================

def issue_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Issues",x=df["repo_full_name"],y=df["issue_closure_rate"]))
    fig.update_layout(title="Issue Closure Rate",yaxis_title="Percentage",**PLOT_LAYOUT)
    return fig


# ==========================================================
# Contributor Analytics
# ==========================================================

def contributor_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Average Contributions",x=df["repo_full_name"],y=df["avg_contributions"]))
    fig.update_layout(title="Contributor Activity",**PLOT_LAYOUT)
    return fig


# ==========================================================
# Workflow Analytics
# ==========================================================

def workflow_chart(df):

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Workflow Success",x=df["repo_full_name"],y=df["workflow_success_rate"]))
    fig.update_layout(title="Workflow Success Rate",yaxis_title="Percentage",**PLOT_LAYOUT)
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
        polar=dict(radialaxis=dict(visible=True)),title="Overall Repository Comparison",**PLOT_LAYOUT)
    return fig