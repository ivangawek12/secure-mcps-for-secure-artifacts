# 07 — Security Checklist

Before running an artifact connected to MCP:

- [ ] I know every MCP server it uses.
- [ ] I know every tool exposed by those servers.
- [ ] I know what private data the tools can access.
- [ ] I know which tools can change or delete data.
- [ ] I know which tools can communicate externally.
- [ ] I have removed capabilities the task does not require.
- [ ] Read and write capabilities are separated where practical.
- [ ] Sensitive actions require human approval where appropriate.
- [ ] I treat web pages, emails, documents and RSS as untrusted input.
- [ ] I have considered the lethal trifecta.
- [ ] I have considered the blast radius of an indirect prompt injection.
- [ ] I have reviewed the artifact before connecting real accounts.

## Golden rule

> If you don't need the capability, don't expose the capability.
