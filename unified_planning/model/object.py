# Copyright 2021 AIPlan4EU project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
This module defines an Object of a planning problem.
An Object is represented by a name and by its type.
"""

from typing import Optional
from unified_planning.environment import Environment, get_env
import unified_planning.model.types


class Object:
    """Represents an object."""

    def __init__(
        self,
        name: str,
        typename: "unified_planning.model.types.Type",
        env: Optional[Environment] = None,
    ):
        self._name = name
        self._typename = typename
        self._env = get_env(env)
        assert self._env.type_manager.has_type(
            typename
        ), "type of the object does not belong to the same environment of the object"

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, oth: object) -> bool:
        if isinstance(oth, Object):
            return (
                self._name == oth._name
                and self._typename == oth._typename
                and self._env == oth._env
            )
        else:
            return False

    def __hash__(self) -> int:
        return hash(self._name) + hash(self._typename)

    @property
    def name(self) -> str:
        """Returns the object name."""
        return self._name

    @property
    def type(self) -> "unified_planning.model.types.Type":
        """Returns the object type."""
        return self._typename

    @property
    def environment(self) -> "Environment":
        """Return the object environment"""
        return self._env

    #
    # Infix operators
    #

    def Equals(self, right):
        return self._env.expression_manager.Equals(self, right)
