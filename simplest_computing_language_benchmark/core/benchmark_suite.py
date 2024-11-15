from typing import Dict
from ..benchmarks.python_benchmark import PythonBenchmark
from ..benchmarks.java_benchmark import JavaBenchmark
from ..benchmarks.nodejs_benchmark import NodeJSBenchmark
from ..benchmarks.go_benchmark import GoBenchmark
from .system_info import SystemInfo

class BenchmarkSuite:
    def __init__(self, iterations: int = 1000):
        self.iterations = iterations
        self.results = {}
        self.system_info = SystemInfo()
        
        # Initialize benchmarks
        self.benchmarks = {
            'python': PythonBenchmark(iterations),
            'java': JavaBenchmark(iterations),
            'nodejs': NodeJSBenchmark(iterations),
            'go': GoBenchmark(iterations)
        }

    def run_all_benchmarks(self) -> Dict:
        """Run benchmarks for all languages."""
        for name, benchmark in self.benchmarks.items():
            print(f"\nRunning {name} benchmarks...")
            results = benchmark.run()
            self.results.update(results)
        return self.results

    def print_comparison(self):
        """Print comparison of all benchmark results."""
        print("\nBenchmark Results (median times in seconds):")
        print("-" * 50)
        
        operations = ['array_sum', 'string_concat', 'math']
        languages = ['python', 'java', 'nodejs', 'go']
        
        for op in operations:
            print(f"\nOperation: {op}")
            times = {lang: self.results[f'{lang}_{op}'] for lang in languages}
            
            # Find the fastest language for this operation
            fastest_lang = min(times, key=times.get)
            fastest_time = times[fastest_lang]
            
            # Print times and ratios
            for lang in languages:
                time = times[lang]
                ratio = time / fastest_time
                print(f"{lang.capitalize()}: {time:.6f} ({ratio:.2f}x {fastest_lang})")

def main():
    suite = BenchmarkSuite()
    suite.system_info.print_info()
    suite.run_all_benchmarks()
    suite.print_comparison()

if __name__ == "__main__":
    main()
