# 01 — What is MCP?

## Goal

Understand MCP without starting with protocol details.

Use this mental model:

```text
AI application
      |
      | MCP
      v
MCP server
      |
      +-- tools
      +-- resources
      +-- prompts
      |
      v
external systems
```

For this course, focus on **tools**.

A tool is a capability exposed to the model.

Example:

```python
@mcp.tool()
def get_bloomberg_news():
    ...
```

The important security question is:

> What does this tool allow the agent to do?

## Exercise

For each hypothetical tool, classify the capability:

```text
get_news()
read_gmail()
read_drive()
send_email()
delete_file()
```

Then rank them from lowest to highest impact.
