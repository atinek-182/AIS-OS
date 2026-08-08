#!/usr/bin/env python3
"""
Composio CLI Runner - 1000+ App Tool Router Engine for AIOS
Powered by Composio CLI (composio-community/skills)
"""

import sys
import os
import json
import shutil
import subprocess
import argparse
from typing import Dict, Any, Optional

# Ensure UTF-8 stdio configuration on Windows OS
sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def resolve_composio_binary() -> Optional[str]:
    """Resolve composio CLI executable binary path on Windows OS."""
    binary = shutil.which("composio") or shutil.which("composio.cmd") or shutil.which("composio.exe")
    if binary:
        return binary
    # Check default global npm / user paths
    user_home = os.path.expanduser("~")
    npm_path = os.path.join(user_home, "AppData", "Roaming", "npm", "composio.cmd")
    if os.path.exists(npm_path):
        return npm_path
    return None


def run_composio_cmd(cmd_args: list) -> Dict[str, Any]:
    """Execute composio CLI command with JSON formatting and error handling."""
    binary = resolve_composio_binary()
    if not binary:
        return {
            "status": "error",
            "message": "Composio CLI is not installed. Run 'curl -fsSL https://composio.dev/install | bash' or 'npm install -g composio-core' to install."
        }

    try:
        full_cmd = [binary] + cmd_args
        result = subprocess.run(
            full_cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=False
        )

        stdout_str = result.stdout.strip()
        stderr_str = result.stderr.strip()

        if result.returncode != 0:
            return {
                "status": "error",
                "returncode": result.returncode,
                "message": stderr_str or stdout_str or "Composio CLI execution failed."
            }

        # Try parsing JSON if available
        try:
            parsed_json = json.loads(stdout_str)
            return {
                "status": "success",
                "data": parsed_json
            }
        except Exception:
            return {
                "status": "success",
                "output": stdout_str
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


def search_tools(query: str) -> Dict[str, Any]:
    """Search Composio 1000+ app tools by natural language query."""
    return run_composio_cmd(["search", query])


def link_app(app_name: str, no_wait: bool = True) -> Dict[str, Any]:
    """Generate account connection OAuth link for external app."""
    args = ["link", app_name]
    if no_wait:
        args.append("--no-wait")
    return run_composio_cmd(args)


def execute_tool(tool_id: str, data_json: str, user_id: Optional[str] = None) -> Dict[str, Any]:
    """Execute a Composio tool action with JSON payload."""
    args = ["execute", tool_id, "--data", data_json]
    if user_id:
        args.extend(["--user-id", user_id])
    return run_composio_cmd(args)


def whoami() -> Dict[str, Any]:
    """Verify Composio authentication status and user details."""
    return run_composio_cmd(["whoami"])


def main():
    parser = argparse.ArgumentParser(description="ZORIXEL AIOS Composio Tool Router Runner")
    subparsers = parser.add_subparsers(dest="action", help="Action to execute")

    # Search action
    s_parser = subparsers.add_parser("search", help="Search 1000+ app tools")
    s_parser.add_argument("--query", required=True, help="Search query string")

    # Link action
    l_parser = subparsers.add_parser("link", help="Link an external app account")
    l_parser.add_argument("--app", required=True, help="App name (e.g. gmail, github, linear, slack)")
    l_parser.add_argument("--wait", action="store_true", help="Wait for interactive browser login")

    # Execute action
    e_parser = subparsers.add_parser("execute", help="Execute a tool action")
    e_parser.add_argument("--tool", required=True, help="Tool ID (e.g. GMAIL_SEND_EMAIL)")
    e_parser.add_argument("--data", required=True, help="JSON string payload")
    e_parser.add_argument("--user-id", help="Optional user ID context")

    # Whoami action
    subparsers.add_parser("whoami", help="Check authentication status")

    args = parser.parse_args()

    if args.action == "search":
        res = search_tools(args.query)
        print(json.dumps(res, indent=2))
    elif args.action == "link":
        res = link_app(args.app, no_wait=not args.wait)
        print(json.dumps(res, indent=2))
    elif args.action == "execute":
        res = execute_tool(args.tool, args.data, user_id=args.user_id)
        print(json.dumps(res, indent=2))
    elif args.action == "whoami":
        res = whoami()
        print(json.dumps(res, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
