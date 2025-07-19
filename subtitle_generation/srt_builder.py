"""
srt_builder.py
--------------
This module provides functions to build SRT subtitle content from a list of subtitle entries.

Usage in project:
- Converts a list of subtitle segments (with start, end, and text) to SRT format.
- Can be used to generate SRT files for videos after transcription.

Example input:
[
    {"start": 0.0, "end": 2.5, "text": "Hello world!"},
    {"start": 2.5, "end": 5.0, "text": "This is an example."}
]
"""

from .utils import seconds_to_srt_time

def build_srt(subtitles):
    """
    Build SRT content from a list of subtitle dicts.
    Each dict should have 'start', 'end', and 'text' keys.

    Returns:
        str: SRT formatted string.
    """
    srt_lines = []
    for idx, sub in enumerate(subtitles, 1):
        start = seconds_to_srt_time(sub["start"])
        end = seconds_to_srt_time(sub["end"])
        text = sub["text"]
        srt_lines.append(f"{idx}\n{start} --> {end}\n{text}\n")
    return "\n".join(srt_lines)

def save_srt_file(srt_content, file_path):
    """
    Save SRT content to a file.

    Args:
        srt_content (str): The SRT formatted string.
        file_path (str): Path to save the SRT file.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
