"""
utils.py
---------
This file contains utility functions for time conversion used in subtitle generation.

Purpose in the project:
- Provides helper functions to convert between seconds (float) and SRT time format (hh:mm:ss,ms).
- Keeps the code DRY and organized by centralizing common operations needed for building subtitles.
- Makes it easy to reuse time conversion logic in other modules (like srt_builder.py) without code duplication.
"""

def seconds_to_srt_time(seconds: float) -> str:
    """
    Convert seconds (float) to SRT time format (hh:mm:ss,ms).
    Example: 75.345 -> "00:01:15,345"

    Usage in project:
    - Used when generating SRT files to format the start and end times of each subtitle line.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def srt_time_to_seconds(srt_time: str) -> float:
    """
    Convert SRT time format (hh:mm:ss,ms) to seconds (float).
    Example: "00:01:15,345" -> 75.345

    Usage in project:
    - Useful for parsing SRT files or when you need to do calculations with subtitle timings.
    """
    hours, minutes, rest = srt_time.split(":")
    secs, millis = rest.split(",")
    total_seconds = (
        int(hours) * 3600 +
        int(minutes) * 60 +
        int(secs) +
        int(millis) / 1000
    )
    return total_seconds
