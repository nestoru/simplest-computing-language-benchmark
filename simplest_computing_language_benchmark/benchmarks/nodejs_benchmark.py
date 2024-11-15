import os
import subprocess
import json
from typing import Dict
from .base_benchmark import BaseBenchmark
from ..templates.nodejs_template import NODEJS_CODE

class NodeJSBenchmark(BaseBenchmark):
    def run(self) -> Dict[str, float]:
        with self:  # Use context manager for temp directory
            # Write Node.js code to temp directory
            js_file = os.path.join(self.temp_dir, "benchmark.js")
            with open(js_file, "w") as f:
                f.write(NODEJS_CODE)
            
            # Run Node.js benchmarks
            print("Running Node.js benchmarks...")
            result = subprocess.run(
                ["node", js_file],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.temp_dir
            )
            
            return json.loads(result.stdout)
