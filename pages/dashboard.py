import streamlit as st
from utils.charts import (
    health_chart,
    pull_request_chart,
    issue_chart,
    contributor_chart,
    workflow_chart,
    radar_chart
)
from utils.insights import generate_insights
from utils.comparison import comparison_table
def render_dashboard(df):

    repo1 = df.iloc[0]
    repo2 = df.iloc[1]

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("## Repository Comparison Dashboard")
    st.caption("Comprehensive analytics generated using Azure Databricks")

    st.divider()

    # =====================================================
    # REPOSITORY SUMMARY
    # =====================================================

    st.subheader("Repository Overview")

    left, right = st.columns(2)

    with left:

        st.markdown(f"### {repo1['repo_full_name']}")

        c1, c2, c3 = st.columns(3)

        c1.metric("Stars", f"{int(repo1['stars']):,}")
        c2.metric("Forks", f"{int(repo1['forks']):,}")
        c3.metric("Watchers", f"{int(repo1['watchers']):,}")

        c4, c5, c6 = st.columns(3)

        c4.metric(
            "Health",
            f"{repo1['repository_health_score']:.2f}"
        )

        c5.metric(
            "Grade",
            repo1["repository_grade"]
        )

        c6.metric(
            "Status",
            repo1["repository_status"]
        )

    with right:

        st.markdown(f"### {repo2['repo_full_name']}")

        c1, c2, c3 = st.columns(3)

        c1.metric("Stars", f"{int(repo2['stars']):,}")
        c2.metric("Forks", f"{int(repo2['forks']):,}")
        c3.metric("Watchers", f"{int(repo2['watchers']):,}")

        c4, c5, c6 = st.columns(3)

        c4.metric(
            "Health",
            f"{repo2['repository_health_score']:.2f}"
        )

        c5.metric(
            "Grade",
            repo2["repository_grade"]
        )

        c6.metric(
            "Status",
            repo2["repository_status"]
        )

    st.divider()

    # =====================================================
    # WINNER
    # =====================================================

    winner = (
        repo1
        if repo1["overall_repository_score"] >= repo2["overall_repository_score"]
        else repo2
    )

    st.success(
        f"**Recommended Repository:** {winner['repo_full_name']} "
        f"({winner['overall_repository_score']:.2f})"
    )

    st.divider()

    # =====================================================
    # KPI SECTION
    # =====================================================

    st.subheader("Key Performance Indicators")

    row1 = st.columns(3)

    row1[0].metric(
        "Repository Health",
        f"{repo1['repository_health_score']:.1f}",
        delta=f"{repo1['repository_health_score']-repo2['repository_health_score']:.1f}"
    )

    row1[1].metric(
        "Merge Rate",
        f"{repo1['merge_rate']:.1f}%",
        delta=f"{repo1['merge_rate']-repo2['merge_rate']:.1f}%"
    )

    row1[2].metric(
        "Issue Closure",
        f"{repo1['issue_closure_rate']:.1f}%",
        delta=f"{repo1['issue_closure_rate']-repo2['issue_closure_rate']:.1f}%"
    )

    row2 = st.columns(3)

    row2[0].metric(
        "Workflow Success",
        f"{repo1['workflow_success_rate']:.1f}%",
        delta=f"{repo1['workflow_success_rate']-repo2['workflow_success_rate']:.1f}%"
    )

    row2[1].metric(
        "Approval Rate",
        f"{repo1['approval_rate']:.1f}%",
        delta=f"{repo1['approval_rate']-repo2['approval_rate']:.1f}%"
    )

    row2[2].metric(
        "Average Contributions",
        f"{repo1['avg_contributions']:.1f}",
        delta=f"{repo1['avg_contributions']-repo2['avg_contributions']:.1f}"
    )

    st.divider()

    # =====================================================
    # CHARTS
    # =====================================================

    st.subheader("Visual Analytics")

    st.plotly_chart(
        health_chart(df),
         width="stretch"
    )

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            pull_request_chart(df),
             width="stretch"
        )

    with right:
        st.plotly_chart(
            issue_chart(df),
             width="stretch"
        )

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            contributor_chart(df),
             width="stretch"
        )

    with right:
        st.plotly_chart(
            workflow_chart(df),
             width="stretch"
        )

    st.plotly_chart(
        radar_chart(df),
         width="stretch"
    )

    st.divider()
# =====================================================
# INSIGHTS
# =====================================================

    for insight in generate_insights(df):

        st.markdown(
            f"""
            <div class="insight-card">

                <div class="insight-title">

                    {insight['title']}

                </div>

                <div class="insight-body">

                    {insight['message']}

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()
# =====================================================
# RAW DATA
# =====================================================

    with st.expander("View Repository Metrics"):

        st.dataframe(
            df,
            width="stretch"
        )