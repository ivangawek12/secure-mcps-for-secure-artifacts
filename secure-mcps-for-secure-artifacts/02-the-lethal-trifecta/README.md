# 02 — The Lethal Trifecta

## Three conditions

Risk becomes especially serious when an agent combines:

1. access to private data;
2. exposure to untrusted content;
3. ability to communicate externally or cause side effects.

## Example

```text
Malicious webpage
       |
       v
     Agent
       |
       +----> read private document
       |
       +----> send externally
```

The content does not need to be trusted merely because the agent was asked to read it.

## Discussion

Ask:

- Can the agent read private information?
- Can untrusted content influence it?
- Can it perform an external action?

If all three are true, the architecture deserves careful review.
