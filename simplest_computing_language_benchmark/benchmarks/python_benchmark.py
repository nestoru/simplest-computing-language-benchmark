from typing import Dict
import numpy as np
from .base_benchmark import BaseBenchmark

class PythonBenchmark(BaseBenchmark):
    def run(self) -> Dict[str, float]:
        results = {}

        # Array operations
        arr = list(range(1000000))
        results['python_array_sum'] = self.time_operation(
            lambda: sum(x * 2 for x in arr)
        )
        
        # String operations
        def string_concat_test():
            # Test 1: String building with join
            parts = []
            for i in range(10000):
                parts.append(f"{i}hello")
            result1 = "".join(parts)
            
            # Test 2: String splitting and processing
            text = "hello,world,this,is,a,test" * 1000
            words = text.split(",")
            processed = [word.upper() for word in words]
            result2 = ",".join(processed)
            
            # Test 3: String replacements
            template = "The quick brown fox" * 100
            result3 = template.replace("quick", "slow").replace("brown", "red").replace("fox", "dog")
            
            return result1 + result2 + result3

        results['python_string_concat'] = self.time_operation(string_concat_test)
        
        # Math operations
        results['python_math'] = self.time_operation(
            lambda: sum(np.sqrt(x) + np.sin(x) for x in range(10000))
        )

        return results
