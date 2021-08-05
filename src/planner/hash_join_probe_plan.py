# coding=utf-8
# Copyright 2018-2020 EVA
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

from typing import List

from src.planner.types import PlanOprType
from src.planner.abstract_join_plan import AbstractJoin
from src.parser.types import JoinType
from src.catalog.models.df_column import DataFrameColumn
from src.expression.abstract_expression import AbstractExpression


class HashJoinProbePlan(AbstractJoin):
    """
    This plan is used for storing information required for
    hash join probe side. It scans over the preferably larger relation
    and uses build side hash table to join.
    Arguments:
        join_type: JoinType
        probe_keys (List[DataFrameColumn]) : list of equi-key columns.
                        Must be equal to build side keys.
        predicate (AbstractExpression)
    """

    def __init__(self,
                 join_type: JoinType,
                 probe_keys: List[DataFrameColumn],
                 predicate: AbstractExpression
                 ):
        super().__init__(PlanOprType.HASH_JOIN,
                         join_type,
                         probe_keys,
                         predicate
                         )
