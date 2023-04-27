import requests
import os
import time
import json

github_token = os.environ.get("GITHUB_TOKEN", "")
github_owner = os.environ.get("rsp-org", "")
github_repo = os.environ.get("buildkite-poc", "")

headers = {
    "authorization": f"token {github_token}",
    "Content-Type": "application/json"
}
r = requests.post(f"https://api.github.com/repos/{github_owner}/{github_repo}/dispatches", data=json.dumps({
    "event_type": "buildkite"
}), headers=headers)

time.sleep(5)

if r.status_code == 200 or r.status_code == 204:
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
                
else:
    print(r.status_code)
    print(r.text)
    exit(1)