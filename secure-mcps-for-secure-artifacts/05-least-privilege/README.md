# 05 — Least Privilege

## Principle

> Give an artifact only the capabilities required for its task.

For a market-news summarizer:

```text
get_bloomberg_news()   ALLOW
read_drive()           DENY
read_gmail()           DENY
send_email()           DENY
delete_file()          DENY
```

## Why it matters

A compromised model is not equivalent to a compromised environment.

If the environment gives the model only one harmless capability, the blast radius is much smaller.

## Exercise

Design an MCP for:

> "Read public market news and produce a morning brief."

Start with zero permissions.

Add only what is necessary.
