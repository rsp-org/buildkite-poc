# Trigger github actions from Buildkite

This is a simple example of how you can trigger github actions from buildkite

## Requirements

- BUILDKITE_AGENT_TOKEN
- GITHUB_TOKEN


## Steps

### Set the environment variables

```sh
export BUILDKITE_AGENT_TOKEN=XXXX
export GITHUB_TOKEN=YYYYY
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