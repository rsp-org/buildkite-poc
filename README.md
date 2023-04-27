# Trigger github actions from Buildkite

This is a simple example of how you can trigger github actions from buildkite

## Requirements

- BUILDKITE_AGENT_TOKEN
- GITHUB_TOKEN
- ID_RSA_PATH (path to your id_rsa file - used to clone the repo)


## Steps

### Set the environment variables

```sh
export BUILDKITE_AGENT_TOKEN=XXXX
export GITHUB_TOKEN=YYYYY
export ID_RSA_PATH=~/.ssh/id_rsa
```

### Start buildkite agent

```sh
docker-compose up -d
```


### Force a commit
You should force a commit to start the pipeline in Buildkite.


### Screenshots
Buildkite
![Buildkite](/docs/buildkite.png "Buildkite")

GHA
![GHA](/docs/gha.png "GHA")
