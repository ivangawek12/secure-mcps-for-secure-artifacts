"""Minimal, read-only MCP server for a classroom Bloomberg RSS example.

The RSS endpoint is intentionally configurable. Use an authorized Bloomberg
feed or the included local fixture for classroom demonstrations.
"""

import os
from pathlib import Path

import feedparser
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Bloomberg News - Read Only")

RSS_URL = os.getenv("BLOOMBERG_RSS_URL", "")
RSS_MODE = os.getenv("RSS_MODE", "remote").lower()
FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "malicious_feed.xml"


def load_feed():
    """Load the configured RSS source."""
    if RSS_MODE == "fixture":
        return feedparser.parse(FIXTURE.read_text(encoding="utf-8"))

    if not RSS_URL:
        raise RuntimeError(
            "Set BLOOMBERG_RSS_URL to an authorized RSS endpoint, "
            "or set RSS_MODE=fixture for the classroom fixture."
        )

    return feedparser.parse(RSS_URL)


@mcp.tool()
def get_bloomberg_news(limit: int = 10) -> list[dict]:
    """Return recent market-news entries from the configured RSS feed.

    This is intentionally read-only. It does not access private accounts,
    write data, send messages, or execute arbitrary commands.
    """
    if not 1 <= limit <= 20:
        raise ValueError("limit must be between 1 and 20")

    feed = load_feed()

    return [
        {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
        }
        for entry in feed.entries[:limit]
    ]


if __name__ == "__main__":
    mcp.run()
