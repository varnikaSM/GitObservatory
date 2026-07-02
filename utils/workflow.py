import os
import time
import requests

from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DATABRICKS_SERVER_HOSTNAME")
TOKEN = os.getenv("DATABRICKS_TOKEN")
JOB_ID = os.getenv("DATABRICKS_JOB_ID")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


def trigger_pipeline(repo1, repo2, analysis_window):
    """
    Starts the Databricks Workflow.

    Returns
    -------
    run_id
    """

    payload = {"job_id": int(JOB_ID),
        "job_parameters": {"repo_urls": f"{repo1},{repo2}","analysis_window": analysis_window}}

    response = requests.post(f"{HOST}/api/2.1/jobs/run-now",headers=HEADERS,json=payload)
    response.raise_for_status()
    return response.json()["run_id"]


def get_run_status(run_id):
    """
    Returns the lifecycle state and result state.
    """

    response = requests.get(f"{HOST}/api/2.1/jobs/runs/get",headers=HEADERS,params={"run_id": run_id})
    response.raise_for_status()
    data = response.json()
    state = data["state"]
    lifecycle = state.get("life_cycle_state")
    result = state.get("result_state")
    return lifecycle, result


def wait_for_completion(run_id, poll_interval=10):
    """
    Waits until the Databricks Workflow finishes.
    """

    while True:
        lifecycle, result = get_run_status(run_id)
        if lifecycle == "TERMINATED":
            return result == "SUCCESS"

        if lifecycle in ["INTERNAL_ERROR", "SKIPPED"]:
            return False

        time.sleep(poll_interval)