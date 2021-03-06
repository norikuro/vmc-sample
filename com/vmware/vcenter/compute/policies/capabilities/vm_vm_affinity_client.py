# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.compute.policies.capabilities.vm_vm_affinity.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.compute.policies.capabilities.vm_vm_affinity_client``
module provides classes for the VM-VM affinity capability offered by vCenter.

"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class CreateSpec(VapiStruct):
    """
    The ``CreateSpec`` class contains information used to create a new VM-VM
    affinity policy, see
    :func:`com.vmware.vcenter.compute_client.Policies.create`. All virtual
    machines that share the tag indicated by :attr:`CreateSpec.vm_tag` will be
    affined to each other. **Warning:** This class is available as technical
    preview. It may be changed in a future release.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 vm_tag=None,
                 name=None,
                 description=None,
                ):
        """
        :type  vm_tag: :class:`str`
        :param vm_tag: Identifier of a tag that can be associated with a virtual machine.
            Virtual machines with this tag will be affined to each other.
            **Warning:** This attribute is available as technical preview. It
            may be changed in a future release.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag:VirtualMachine``. When methods return
            a value of this class as a return value, the attribute will be an
            identifier for the resource type:
            ``com.vmware.cis.tagging.Tag:VirtualMachine``.
        :type  name: :class:`str`
        :param name: Name of the policy. The name needs to be unique within this vCenter
            server. **Warning:** This attribute is available as technical
            preview. It may be changed in a future release.
        :type  description: :class:`str`
        :param description: Description of the policy. **Warning:** This attribute is available
            as technical preview. It may be changed in a future release.
        """
        self.vm_tag = vm_tag
        self.name = name
        self.description = description
        VapiStruct.__init__(self)


CreateSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.compute.policies.capabilities.vm_vm_affinity.create_spec', {
        'vm_tag': type.IdType(resource_types='com.vmware.cis.tagging.Tag:VirtualMachine'),
        'name': type.StringType(),
        'description': type.StringType(),
    },
    CreateSpec,
    False,
    None))



class Info(VapiStruct):
    """
    The ``Info`` class contains information about a VM-VM affinity policy, see
    :func:`com.vmware.vcenter.compute_client.Policies.get`. All virtual
    machines that share the tag indicated by :attr:`Info.vm_tag` are affined to
    each other. **Warning:** This class is available as technical preview. It
    may be changed in a future release.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 vm_tag=None,
                 name=None,
                 description=None,
                 capability=None,
                ):
        """
        :type  vm_tag: :class:`str`
        :param vm_tag: Identifier of a tag that can be associated with a virtual machine.
            Virtual machines with this tag will be affined to each other.
            **Warning:** This attribute is available as technical preview. It
            may be changed in a future release.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag:VirtualMachine``. When methods return
            a value of this class as a return value, the attribute will be an
            identifier for the resource type:
            ``com.vmware.cis.tagging.Tag:VirtualMachine``.
        :type  name: :class:`str`
        :param name: Name of the policy. **Warning:** This attribute is available as
            technical preview. It may be changed in a future release.
        :type  description: :class:`str`
        :param description: Description of the policy. **Warning:** This attribute is available
            as technical preview. It may be changed in a future release.
        :type  capability: :class:`str`
        :param capability: Identifier of the capability this policy is based on. **Warning:**
            This attribute is available as technical preview. It may be changed
            in a future release.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vcenter.compute.policies.Capability``. When methods
            return a value of this class as a return value, the attribute will
            be an identifier for the resource type:
            ``com.vmware.vcenter.compute.policies.Capability``.
        """
        self.vm_tag = vm_tag
        self.name = name
        self.description = description
        self.capability = capability
        VapiStruct.__init__(self)


Info._set_binding_type(type.StructType(
    'com.vmware.vcenter.compute.policies.capabilities.vm_vm_affinity.info', {
        'vm_tag': type.IdType(resource_types='com.vmware.cis.tagging.Tag:VirtualMachine'),
        'name': type.StringType(),
        'description': type.StringType(),
        'capability': type.IdType(resource_types='com.vmware.vcenter.compute.policies.Capability'),
    },
    Info,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

