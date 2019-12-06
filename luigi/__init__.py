# -*- coding: utf-8 -*-
#
# Copyright 2012-2015 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Package containing core luigi functionality.
"""

from luigi import configuration, event, interface, local_target, parameter, rpc, target, task
from luigi.__meta__ import __version__
from luigi.event import Event
from luigi.execution_summary import LuigiStatusCode
from luigi.interface import build, run
from luigi.local_target import LocalTarget
from luigi.parameter import (BoolParameter, ChoiceParameter, DateHourParameter, DateIntervalParameter, DateMinuteParameter, DateParameter, DateSecondParameter,
                             DictParameter, EnumParameter, FloatParameter, IntParameter, ListParameter, MonthParameter, NumericalParameter, OptionalParameter,
                             Parameter, TaskParameter, TimeDeltaParameter, TupleParameter, YearParameter)
from luigi.rpc import RemoteScheduler, RPCError
from luigi.target import Target
from luigi.task import Config, ExternalTask, Task, WrapperTask, auto_namespace, namespace

__all__ = [
    'task', 'Task', 'Config', 'ExternalTask', 'WrapperTask', 'namespace', 'auto_namespace',
    'target', 'Target', 'LocalTarget', 'rpc', 'RemoteScheduler',
    'RPCError', 'parameter', 'Parameter', 'DateParameter', 'MonthParameter',
    'YearParameter', 'DateHourParameter', 'DateMinuteParameter', 'DateSecondParameter',
    'DateIntervalParameter', 'TimeDeltaParameter', 'IntParameter',
    'FloatParameter', 'BoolParameter', 'TaskParameter',
    'ListParameter', 'TupleParameter', 'EnumParameter', 'DictParameter',
    'configuration', 'interface', 'local_target', 'run', 'build', 'event', 'Event',
    'NumericalParameter', 'ChoiceParameter', 'OptionalParameter', 'LuigiStatusCode',
    '__version__',
]

if not configuration.get_config().has_option('core', 'autoload_range'):
    import warnings
    warning_message = '''
        Autoloading range tasks by default has been deprecated and will be removed in a future version.
        To get the behavior now add an option to luigi.cfg:

          [core]
            autoload_range: false

        Alternately set the option to true to continue with existing behaviour and suppress this warning.
    '''
    warnings.warn(warning_message, DeprecationWarning)

if configuration.get_config().getboolean('core', 'autoload_range', True):
    from .tools import range  # noqa: F401    just makes the tool classes available from command line
    __all__.append('range')
