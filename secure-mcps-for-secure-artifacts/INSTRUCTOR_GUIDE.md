# Instructor Guide

## Suggested 60-minute flow

### 0–10 min — MCP basics

Show:

```text
Artifact -> MCP -> Tool -> External system
```

Ask students what changes when an AI can call a tool.

### 10–20 min — Build

Run the read-only Bloomberg RSS MCP with the local fixture.

Have students inspect the single exposed tool.

### 20–35 min — Attack

Run the malicious fixture.

Ask:

> What is the injected instruction trying to make the agent do?

Then ask:

> Can it actually do that with the current capability set?

### 35–45 min — Expand the permissions

On the whiteboard, add:

```text
read_drive()
read_gmail()
send_email()
```

Discuss the increased blast radius.

### 45–55 min — Defend

Students apply:

- least privilege;
- capability separation;
- read/write separation;
- human approval.

### 55–60 min — Debrief

End with:

> Don't secure the prompt. Secure the capabilities.

## Important teaching point

Do not present MCP as inherently insecure.

MCP is a protocol for exposing capabilities and context.

The security problem comes from architecture, permissions, trust boundaries, tool design, authentication/authorization, and how an agent combines capabilities with untrusted input.
