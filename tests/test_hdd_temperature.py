#!/usr/bin/env python

import pytest
from nas_hddfun_ctrl.hdd_temperature import get_hdd_temperature


# @pytest.mark.parametrize('temp_str, temp_val', [
#     ('194 Temperature_Celsius     0x0002   193   193   000    Old_age   Always       -       31 (Min/Max 10/77)', 31),
#     ('Temperature:                        45 Celsius', 45)
# ])
# def test_get_hdd_temperature(temp_str, temp_val):
def test_get_hdd_temperature():
    smartctl_result = ""
    result = get_hdd_temperature('/dev/sda')
    assert result
