"""
This formatter display difference between 2 files in json format.
"""

import json


def format_diff(diff):
    return json.dumps(diff)
