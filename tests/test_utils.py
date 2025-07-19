"""
test_utils.py
-------------
This file contains unit tests for the utility functions in utils.py.

Purpose:
- Verify the correctness of time conversion functions used in subtitle generation.
- Ensure reliable conversion between seconds (float) and SRT time format (hh:mm:ss,ms).
- Catch potential edge cases and rounding issues.
- Maintain code quality and prevent regressions when updating utils.py.

How to run:
- Run directly: python tests/test_utils.py
- Or use pytest for advanced testing: pytest tests/test_utils.py
"""

from subtitle_generation.utils import seconds_to_srt_time, srt_time_to_seconds

def test_seconds_to_srt_time():
    """
    Test the conversion from seconds (float) to SRT time format string.
    Checks normal values and boundary conditions.
    """
    assert seconds_to_srt_time(0.0) == "00:00:00,000"
    assert seconds_to_srt_time(1.234) == "00:00:01,234"
    assert seconds_to_srt_time(65.78) == "00:01:05,780"
    assert seconds_to_srt_time(3661.789) == "01:01:01,789"
    assert seconds_to_srt_time(3599.999) == "00:59:59,999"  # Boundary test

def test_srt_time_to_seconds():
    """
    Test the conversion from SRT time format string to seconds (float).
    Checks normal values and boundary conditions.
    """
    assert srt_time_to_seconds("00:00:00,000") == 0.0
    assert srt_time_to_seconds("00:00:01,234") == 1.234
    assert srt_time_to_seconds("00:01:05,780") == 65.78
    assert srt_time_to_seconds("01:01:01,789") == 3661.789
    assert srt_time_to_seconds("00:59:59,999") == 3599.999  # Boundary test

def test_inverse_conversion():
    """
    Test the round-trip conversion accuracy:
    Converting seconds to SRT format and back should return the original seconds (within a small tolerance).
    """
    seconds_values = [0.0, 1.234, 65.78, 3661.789, 3599.999]
    for seconds in seconds_values:
        srt_time = seconds_to_srt_time(seconds)
        result = srt_time_to_seconds(srt_time)
        # Allow minor rounding differences due to milliseconds precision
        assert abs(result - seconds) < 0.001

if __name__ == "__main__":
    test_seconds_to_srt_time()
    test_srt_time_to_seconds()
    test_inverse_conversion()
    print("All utils tests passed.")
