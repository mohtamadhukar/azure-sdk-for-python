# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .azure_workload_recovery_point_py3 import AzureWorkloadRecoveryPoint


class AzureWorkloadSQLRecoveryPoint(AzureWorkloadRecoveryPoint):
    """SQL specific recoverypoint, specifcally encaspulates full/diff
    recoverypoint alongwith extended info.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureWorkloadSQLPointInTimeRecoveryPoint

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_point_time_in_utc: UTC time at which recoverypoint was
     created
    :type recovery_point_time_in_utc: datetime
    :param type: Type of restore point. Possible values include: 'Invalid',
     'Full', 'Log', 'Differential'
    :type type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RestorePointType
    :param extended_info: Extended Info that provides data directory details.
     Will be populated in two cases:
     When a specific recovery point is accessed using GetRecoveryPoint
     Or when ListRecoveryPoints is called for Log RP only with ExtendedInfo
     query filter
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.AzureWorkloadSQLRecoveryPointExtendedInfo
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_point_time_in_utc': {'key': 'recoveryPointTimeInUTC', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AzureWorkloadSQLRecoveryPointExtendedInfo'},
    }

    _subtype_map = {
        'object_type': {'AzureWorkloadSQLPointInTimeRecoveryPoint': 'AzureWorkloadSQLPointInTimeRecoveryPoint'}
    }

    def __init__(self, *, recovery_point_time_in_utc=None, type=None, extended_info=None, **kwargs) -> None:
        super(AzureWorkloadSQLRecoveryPoint, self).__init__(recovery_point_time_in_utc=recovery_point_time_in_utc, type=type, **kwargs)
        self.extended_info = extended_info
        self.object_type = 'AzureWorkloadSQLRecoveryPoint'
