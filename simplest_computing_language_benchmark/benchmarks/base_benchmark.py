import time
import statistics
import tempfile
import os
import shutil
from abc import ABC, abstractmethod
from typing import Dict, Callable

class BaseBenchmark(ABC):
    def __init__(self, iterations: int = 1000):
        self.iterations = iterations
        self.language = self.__class__.__name__.lower().replace('benchmark', '')
        self.temp_dir = None

    def __enter__(self):
        """Create temporary directory when entering context."""
        self.temp_dir = tempfile.mkdtemp(prefix=f'benchmark_{self.language}_')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up temporary directory and files when exiting context."""
        if self.temp_dir and os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def time_operation(self, func: Callable) -> float:
        """Time a single operation with proper warm-up."""
        # Warm-up phase
        for _ in range(10):
            func()
        
        # Actual timing
        times = []
        for _ in range(self.iterations):
            start = time.perf_counter_ns()
            func()
            end = time.perf_counter_ns()
            times.append((end - start) / 1e9)
        
        return statistics.median(times)

    @abstractmethod
    def run(self) -> Dict[str, float]:
        """Run all benchmarks for this language."""
        pass
