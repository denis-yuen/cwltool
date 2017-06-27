# Stubs for galaxy.jobs.metrics.collectl.processes (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def generate_process_statistics(collectl_playback_cli, pid, statistics: Any = ...): ...

class CollectlProcessSummarizer:
    pid = ...  # type: Any
    statistics = ...  # type: Any
    columns_of_interest = ...  # type: Any
    tree_statistics = ...  # type: Any
    process_accum_statistics = ...  # type: Any
    interval_count = ...  # type: int
    def __init__(self, pid, statistics) -> None: ...
    def handle_interval(self, interval): ...
    def get_statistics(self): ...

class CollectlProcessInterval:
    rows = ...  # type: Any
    def __init__(self) -> None: ...
    def row_is_in(self, row): ...
    def add_row(self, row): ...
