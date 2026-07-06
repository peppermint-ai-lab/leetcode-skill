#!/usr/bin/env python3
"""
Calculate elapsed time for interview sessions.

Usage:
    python session_time.py                    # Get elapsed time for current session
    python session_time.py --session <file>  # Get time from archived session
"""

import json
import time
import argparse
from pathlib import Path

INTERVIEW_DIR = Path(__file__).parent.parent.parent.parent.parent / ".interview"
SESSION_FILE = INTERVIEW_DIR / ".session.json"


def get_elapsed_minutes(start_time: int, end_time: int = None) -> float:
    """Calculate elapsed minutes between start and end time."""
    if end_time is None:
        end_time = int(time.time())
    return (end_time - start_time) / 60


def get_current_session_time() -> dict:
    """Get elapsed time for the current active session."""
    if not SESSION_FILE.exists():
        return {"error": "No active session"}

    with open(SESSION_FILE) as f:
        session = json.load(f)

    start = session.get("start_time")
    if not start:
        return {"error": "No start_time in session"}

    elapsed = get_elapsed_minutes(start)
    return {
        "start_time": start,
        "current_time": int(time.time()),
        "elapsed_minutes": round(elapsed, 1)
    }


def get_archived_session_time(session_file: str) -> dict:
    """Get time from an archived session file."""
    path = Path(session_file)
    if not path.exists():
        # Try in interview directory
        path = INTERVIEW_DIR / session_file

    if not path.exists():
        return {"error": f"Session file not found: {session_file}"}

    with open(path) as f:
        session = json.load(f)

    start = session.get("start_time")
    end = session.get("end_time")

    if not start:
        return {"error": "No start_time in session"}

    elapsed = get_elapsed_minutes(start, end)
    return {
        "start_time": start,
        "end_time": end,
        "elapsed_minutes": round(elapsed, 1)
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate interview session time")
    parser.add_argument("--session", "-s", help="Archived session file to check")
    args = parser.parse_args()

    if args.session:
        result = get_archived_session_time(args.session)
    else:
        result = get_current_session_time()

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Elapsed: {result['elapsed_minutes']} minutes")
        if "end_time" in result:
            print(f"Start: {result['start_time']}, End: {result['end_time']}")
        else:
            print(f"Start: {result['start_time']}, Now: {result['current_time']}")
