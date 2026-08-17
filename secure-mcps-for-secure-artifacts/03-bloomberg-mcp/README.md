# 03 — Bloomberg MCP

## Goal

Build a minimal read-only MCP server.

The server exposes exactly one tool:

```text
get_bloomberg_news()
```

## Why this is a good teaching example

The capability is narrow:

```text
public news -> agent
```

There is no private-data connector and no outbound write action.

## Run with the local fixture

```bash
export RSS_MODE=fixture
python src/server.py
```

On Windows PowerShell:

```powershell
$env:RSS_MODE="fixture"
python src/server.py
```

## Use an authorized Bloomberg feed

```bash
export BLOOMBERG_RSS_URL="YOUR_AUTHORIZED_ENDPOINT"
export RSS_MODE=remote
python src/server.py
```

Bloomberg feed access can depend on product and licensing arrangements. Do not assume a public RSS URL is authorized for redistribution or automated use.
