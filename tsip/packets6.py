# -*- coding: utf-8 -*-

"""
TSIP packets in the 0x6? range.

* 0x69 - Receiver Acquisition Sensitivity Mode report.
* 0x6d - All-In-View Satellite Selection report.

"""


import struct

from tsip.constants import *

from tsip.base import *


class Report_69(_Report):
    """
    Receiver Acquisition Sensitivity Mode report

    """

    _format = '>B'
    _values = []


class Report_6d(_Report):
    """
    All-In-View Satellite Selection report

    """

    _format = '>Bffff'
    _values = []

