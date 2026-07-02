import streamlit as st
from utils.repository_service import get_repository_comparison
from utils.workflow import trigger_pipeline, wait_for_completion
from pages.dashboard import render_dashboard
# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(page_title="GitObservatory",page_icon="🔭",layout="wide",initial_sidebar_state="collapsed")

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
load_css()

# ============================================================
# Header
# ============================================================
st.markdown("""
# 🔭 GitObservatory

### GitHub Repository Analytics & Comparison Platform

Compare GitHub repositories using an end-to-end Data Engineering pipeline powered by **Azure Databricks**, **Delta Lake**, **GitHub REST API**, and **Streamlit**.
""")
st.divider()

# ============================================================
# Repository Input Section
# ============================================================

st.markdown("## Repository Selection")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Repository 1")
    repo1 = st.text_input(label="",placeholder="https://github.com/owner/repository")

with col2:
    st.markdown("### Repository 2")
    repo2 = st.text_input(label="",placeholder="https://github.com/owner/repository",key="repo2")

st.divider()

# ============================================================
# Analysis Window
# ============================================================

st.markdown("## Analysis Window")

analysis_options = {
    "Last 15 days":"15d",
    "Last 1 Month": "1m",
    "Last 2 Months": "2m",
    "Last Quarter (3 Months)": "3m",
    "Last 6 Months": "6m",
    "Last 1 Year": "1y",
    "Last 2 Years": "2y"
}
selected_analysis = st.radio("Analysis Window",options=list(analysis_options.keys()),horizontal=True,index=4)
analysis_window = analysis_options[selected_analysis]
st.divider()

# ============================================================
# Compare Button
# ============================================================
compare = st.button("Compare Repositories",use_container_width=True)
# ============================================================
# Validation
# ============================================================
if compare:
    if not repo1 or not repo2:
        st.error("Please enter both GitHub repository URLs.")
    else:
        progress = st.progress(0)
        status = st.empty()
        # -----------------------------------------
        # Validate
        # -----------------------------------------
        status.info("Validating repository URLs...")
        progress.progress(10)

        # -----------------------------------------
        # Trigger Pipeline
        # -----------------------------------------
        status.info("Triggering Databricks workflow...")
        run_id = trigger_pipeline(repo1,repo2,analysis_window)
        progress.progress(25)

        # -----------------------------------------
        # Wait for Completion
        # -----------------------------------------
        status.info("⏳ Running the medallion pipeline...")
        completed = wait_for_completion(run_id)
        progress.progress(85)
        if completed:
            status.info("Loading analytics")
            df = get_repository_comparison()
            progress.progress(100)
            st.write(df)
            st.write(f"Rows returned: {len(df)}")
            status.success("Repository comparison completed successfully!")
            render_dashboard(df)

        else:
            progress.empty()
            status.error("Pipeline execution failed.")

st.divider()


# ============================================================
# Footer
# ============================================================

st.markdown(
"""
<div class="footer">

Built by Varnika Sasi Magesh using Azure Databricks • Delta Lake • GitHub API • Streamlit

</div>
""",
unsafe_allow_html=True
)