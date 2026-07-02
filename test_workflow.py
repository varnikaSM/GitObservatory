from utils.workflow import trigger_pipeline, wait_for_completion

run_id = trigger_pipeline(
    "https://github.com/pallets/click",
    "https://github.com/pallets/itsdangerous",
    "15d"
)

print(run_id)

status = wait_for_completion(run_id)

print(status)