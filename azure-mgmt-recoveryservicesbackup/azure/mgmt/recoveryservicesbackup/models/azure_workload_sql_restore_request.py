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

from .azure_workload_restore_request import AzureWorkloadRestoreRequest


class AzureWorkloadSQLRestoreRequest(AzureWorkloadRestoreRequest):
    """AzureWorkload SQL -specific restore. Specifically for full/diff restore.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureWorkloadSQLPointInTimeRestoreRequest

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_type: OLR/ALR, RestoreDisks is invalid option. Possible
     values include: 'Invalid', 'OriginalLocation', 'AlternateLocation',
     'RestoreDisks'
    :type recovery_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryType
    :param source_resource_id: Fully qualified ARM ID of the VM on which
     workload that was running is being recovered.
    :type source_resource_id: str
    :param property_bag: Workload specific property bag.
    :type property_bag: dict[str, str]
    :param should_use_alternate_target_location: Default option set to true.
     If this is set to false, alternate data directory must be provided
    :type should_use_alternate_target_location: bool
    :param is_non_recoverable: SQL specific property where user can chose to
     set no-recovery when restore operation is tried
    :type is_non_recoverable: bool
    :param target_info: Details of target database
    :type target_info:
     ~azure.mgmt.recoveryservicesbackup.models.TargetRestoreInfo
    :param alternate_directory_paths: Data directory details
    :type alternate_directory_paths:
     list[~azure.mgmt.recoveryservicesbackup.models.SQLDataDirectoryMapping]
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_type': {'key': 'recoveryType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'property_bag': {'key': 'propertyBag', 'type': '{str}'},
        'should_use_alternate_target_location': {'key': 'shouldUseAlternateTargetLocation', 'type': 'bool'},
        'is_non_recoverable': {'key': 'isNonRecoverable', 'type': 'bool'},
        'target_info': {'key': 'targetInfo', 'type': 'TargetRestoreInfo'},
        'alternate_directory_paths': {'key': 'alternateDirectoryPaths', 'type': '[SQLDataDirectoryMapping]'},
    }

    _subtype_map = {
        'object_type': {'AzureWorkloadSQLPointInTimeRestoreRequest': 'AzureWorkloadSQLPointInTimeRestoreRequest'}
    }

    def __init__(self, **kwargs):
        super(AzureWorkloadSQLRestoreRequest, self).__init__(**kwargs)
        self.should_use_alternate_target_location = kwargs.get('should_use_alternate_target_location', None)
        self.is_non_recoverable = kwargs.get('is_non_recoverable', None)
        self.target_info = kwargs.get('target_info', None)
        self.alternate_directory_paths = kwargs.get('alternate_directory_paths', None)
        self.object_type = 'AzureWorkloadSQLRestoreRequest'
