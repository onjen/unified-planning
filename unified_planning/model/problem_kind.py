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

from functools import partialmethod, total_ordering
from typing import Dict, List, Set
import unified_planning as up


# TODO: This features map needs to be extended with all the problem characterizations.
FEATURES = {
    "PROBLEM_CLASS": ["ACTION_BASED", "HIERARCHICAL"],
    "TIME": [
        "CONTINUOUS_TIME",
        "DISCRETE_TIME",
        "INTERMEDIATE_CONDITIONS_AND_EFFECTS",
        "TIMED_EFFECT",
        "TIMED_GOALS",
        "DURATION_INEQUALITIES",
    ],
    "EXPRESSION_DURATION": ["STATIC_FLUENTS_IN_DURATION", "FLUENTS_IN_DURATION"],
    "NUMBERS": ["CONTINUOUS_NUMBERS", "DISCRETE_NUMBERS"],
    "CONDITIONS_KIND": [
        "NEGATIVE_CONDITIONS",
        "DISJUNCTIVE_CONDITIONS",
        "EQUALITY",
        "EXISTENTIAL_CONDITIONS",
        "UNIVERSAL_CONDITIONS",
    ],
    "EFFECTS_KIND": ["CONDITIONAL_EFFECTS", "INCREASE_EFFECTS", "DECREASE_EFFECTS"],
    "TYPING": ["FLAT_TYPING", "HIERARCHICAL_TYPING"],
    "FLUENTS_TYPE": ["NUMERIC_FLUENTS", "OBJECT_FLUENTS"],
    "QUALITY_METRICS": ["ACTIONS_COST", "FINAL_VALUE", "MAKESPAN", "PLAN_LENGTH"],
    "SIMULATED_ENTITIES": ["SIMULATED_EFFECTS"],
}


class ProblemKindMeta(type):
    """Meta class used to interpret the nodehandler decorator."""

    def __new__(cls, name, bases, dct):
        def _set(self, feature, possible_features):
            assert feature in possible_features
            self._features.add(feature)

        def _has(self, feature):
            return feature in self._features

        obj = type.__new__(cls, name, bases, dct)
        for m, l in FEATURES.items():
            setattr(obj, "set_" + m.lower(), partialmethod(_set, possible_features=l))
            for f in l:
                setattr(obj, "has_" + f.lower(), partialmethod(_has, feature=f))
        return obj


@total_ordering
class ProblemKind(up.AnyBaseClass, metaclass=ProblemKindMeta):
    def __init__(self, features: Set[str] = set()):
        self._features: Set[str] = set(features)

    def __repr__(self) -> str:
        features_gen = (f"'{feature}'" for feature in self._features)
        return f'ProblemKind([{", ".join(features_gen)}])'

    def __str__(self) -> str:
        features_mapped: Dict[str, List[str]] = {}
        for k, fl in FEATURES.items():
            for feature in self._features:
                if feature in fl:
                    feature_list = features_mapped.get(k, None)
                    if feature_list is None:
                        features_mapped[k] = [feature]
                    else:
                        feature_list.append(feature)
        result_str: List[str] = [f"{k}: {fl}" for k, fl in features_mapped.items()]
        return "\n".join(result_str)

    def __eq__(self, oth: object) -> bool:
        if isinstance(oth, ProblemKind):
            return self._features == oth._features
        else:
            return False

    def __hash__(self) -> int:
        res = 0
        for f in self._features:
            res += hash(f)
        return res

    def __le__(self, oth: object):
        if not isinstance(oth, ProblemKind):
            raise
        return self._features.issubset(oth._features)

    @property
    def features(self) -> Set[str]:
        return self._features

    def union(self, oth: "ProblemKind") -> "ProblemKind":
        return ProblemKind(self.features.union(oth.features))


basic_classical_kind = ProblemKind()
basic_classical_kind.set_problem_class("ACTION_BASED")
basic_classical_kind.set_typing("FLAT_TYPING")

hierarchical_kind = ProblemKind()
hierarchical_kind.set_typing("HIERARCHICAL_TYPING")

classical_kind = ProblemKind()
classical_kind.set_problem_class("ACTION_BASED")
classical_kind.set_typing("FLAT_TYPING")
classical_kind.set_conditions_kind("NEGATIVE_CONDITIONS")
classical_kind.set_conditions_kind("DISJUNCTIVE_CONDITIONS")
classical_kind.set_conditions_kind("EQUALITY")

full_classical_kind = ProblemKind()
full_classical_kind.set_problem_class("ACTION_BASED")
full_classical_kind.set_typing("FLAT_TYPING")
full_classical_kind.set_conditions_kind("NEGATIVE_CONDITIONS")
full_classical_kind.set_conditions_kind("DISJUNCTIVE_CONDITIONS")
full_classical_kind.set_conditions_kind("EQUALITY")
full_classical_kind.set_conditions_kind("EXISTENTIAL_CONDITIONS")
full_classical_kind.set_conditions_kind("UNIVERSAL_CONDITIONS")
full_classical_kind.set_effects_kind("CONDITIONAL_EFFECTS")

object_fluent_kind = ProblemKind()
object_fluent_kind.set_fluents_type("OBJECT_FLUENTS")

basic_numeric_kind = ProblemKind()
basic_numeric_kind.set_problem_class("ACTION_BASED")
basic_numeric_kind.set_typing("FLAT_TYPING")
basic_numeric_kind.set_numbers("DISCRETE_NUMBERS")
basic_numeric_kind.set_numbers("CONTINUOUS_NUMBERS")
basic_numeric_kind.set_fluents_type("NUMERIC_FLUENTS")

full_numeric_kind = ProblemKind()
full_numeric_kind.set_problem_class("ACTION_BASED")
full_numeric_kind.set_typing("FLAT_TYPING")
full_numeric_kind.set_numbers("DISCRETE_NUMBERS")
full_numeric_kind.set_numbers("CONTINUOUS_NUMBERS")
full_numeric_kind.set_fluents_type("NUMERIC_FLUENTS")
full_numeric_kind.set_effects_kind("INCREASE_EFFECTS")
full_numeric_kind.set_effects_kind("DECREASE_EFFECTS")

basic_temporal_kind = ProblemKind()
basic_temporal_kind.set_problem_class("ACTION_BASED")
basic_temporal_kind.set_typing("FLAT_TYPING")
basic_temporal_kind.set_time("CONTINUOUS_TIME")

temporal_kind = ProblemKind()
temporal_kind.set_problem_class("ACTION_BASED")
temporal_kind.set_typing("FLAT_TYPING")
temporal_kind.set_time("CONTINUOUS_TIME")
temporal_kind.set_time("INTERMEDIATE_CONDITIONS_AND_EFFECTS")
temporal_kind.set_time("TIMED_EFFECT")
temporal_kind.set_time("TIMED_GOALS")
temporal_kind.set_time("DURATION_INEQUALITIES")
temporal_kind.set_expression_duration("STATIC_FLUENTS_IN_DURATION")

quality_metrics_kind = ProblemKind()
quality_metrics_kind.set_quality_metrics("ACTIONS_COST")
quality_metrics_kind.set_quality_metrics("FINAL_VALUE")
