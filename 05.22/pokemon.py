from typing import List
from dataclasses import dataclass


@dataclass
class Statistic:
    base_stat: str
    name: str


@dataclass
class Pokemon:
    name: str
    stats: List[Statistic]

    def get_statistic_base_stat(self, stat_name: str):
        for statistic in self.stats:
            if statistic.name == stat_name:
                return statistic.base_stat
        return 0