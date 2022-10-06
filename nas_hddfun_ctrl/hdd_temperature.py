#!/usr/bin/env python
"""
Some description
"""

import re
import subprocess


def get_hdd_temperature(disk):
    output = subprocess.check_output(["smartctl", "-A", disk])
    val = re.search("Temperature.*\s(\d+)\s*(?:\([\d\s]*\)|)$", output, re.MULTILINE).group(1)
    return int(val)
