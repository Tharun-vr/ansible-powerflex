# Copyright: (c) 2022, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock ApiException for PowerFlex Test modules"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }


class MockApiException(Exception):
    body = "PyPowerFlex Error message"
    status = "500"
