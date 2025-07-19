"""
test_str_builder.py
-------------------
This file contains unit tests for the functions in str_builder.py.

Purpose:
- Ensures that the SRT building and saving functions work as expected.
- Helps catch bugs in subtitle formatting and file output.
- Keeps the codebase reliable as you make changes.

How to run:
- Run directly with: python tests/test_str_builder.py
- Or use pytest for more advanced testing: pytest tests/test_str_builder.py
"""

from subtitle_generation.srt_builder import build_srt, save_srt_file
import os

def test_build_srt():
    """
    Test the build_srt function to ensure it formats subtitles correctly.
    """
    test_subs = [
        {"start": 0.0, "end": 2.5, "text": "Hello world!"},
        {"start": 2.5, "end": 5.0, "text": "This is an example."}
    ]
    srt = build_srt(test_subs)
    assert "1\n00:00:00,000 --> 00:00:02,500\nHello world!" in srt
    assert "2\n00:00:02,500 --> 00:00:05,000\nThis is an example." in srt

def test_save_srt_file():
    """
    Test the save_srt_file function to ensure it writes SRT content to a file.
    """
    srt_content = "1\n00:00:00,000 --> 00:00:02,500\nHello world!\n"
    file_path = "test_output.srt"
    save_srt_file(srt_content, file_path)
    # Check if file exists and content is correct
    assert os.path.exists(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == srt_content
    # Clean up test file
    os.remove(file_path)

if __name__ == "__main__":
    test_build_srt()
    test_save_srt_file()
    print("All str_builder tests passed.")