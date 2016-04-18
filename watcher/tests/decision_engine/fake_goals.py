# -*- encoding: utf-8 -*-
# Copyright (c) 2016 b<>com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from watcher.decision_engine.goal import base as base_goal


class FakeGoal(base_goal.Goal):

    NAME = NotImplemented
    DISPLAY_NAME = NotImplemented

    @classmethod
    def get_name(cls):
        return cls.NAME

    @classmethod
    def get_display_name(cls):
        return cls.DISPLAY_NAME

    @classmethod
    def get_translatable_display_name(cls):
        return cls.DISPLAY_NAME


class FakeDummy1(FakeGoal):
    NAME = "dummy_1"
    DISPLAY_NAME = "Dummy 1"


class FakeDummy2(FakeGoal):
    NAME = "dummy_2"
    DISPLAY_NAME = "Dummy 2"


class FakeOtherDummy2(FakeGoal):
    NAME = "dummy_2"
    DISPLAY_NAME = "Other Dummy 2"
