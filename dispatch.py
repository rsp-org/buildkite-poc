import requests
import os
import time
import json

github_token = os.environ.get("GITHUB_TOKEN", "")
github_owner = os.environ.get("GITHUB_OWNER", "rsp-org")
github_repo = os.environ.get("GITHUB_REPO", "buildkite-poc")

headers = {
    "authorization": f"token {github_token}",
    "Content-Type": "application/json"
}
print("trigger")
r = requests.post(f"https://api.github.com/repos/{github_owner}/{github_repo}/dispatches", data=json.dumps({
    "event_type": "buildkite"
}), headers=headers)

print("wait")
time.sleep(5)

if r.status_code == 200 or r.status_code == 204:
    print("get workflow runs")
    r = requests.get(f"https://api.github.com/repos/{github_owner}/{github_repo}/actions/runs", data=json.dumps({
        "event_type": "buildkite"
    }), headers=headers)

    result = r.json()

    for workflow_run in result['workflow_runs']:
        id = workflow_run['id']
        status = workflow_run['status']
        if status == 'queued' or status == "in_progress":
            pending = True

            while pending:
                print(f'Workflow {id} still executing')
                time.sleep(10)
                r = requests.get(f"https://api.github.com/repos/{github_owner}/{github_repo}/actions/runs/{id}", data=json.dumps({
                    "event_type": "buildkite"
                }), headers=headers)
                result = r.json()

                pending = result['status'] == 'queued' or result['status'] == "in_progress"
    print("Workflows finished")           
else:
    print("error")
    print(r.status_code)
    print(r.text)
    exit(1)