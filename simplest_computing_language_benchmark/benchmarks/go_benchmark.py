import os
import subprocess
import json
from typing import Dict
from .base_benchmark import BaseBenchmark
from ..templates.go_template import GO_CODE

class GoBenchmark(BaseBenchmark):
    def run(self) -> Dict[str, float]:
        with self:  # Use context manager for temp directory
            # Write Go code to temp directory
            go_file = os.path.join(self.temp_dir, "benchmark.go")
            with open(go_file, "w") as f:
                f.write(GO_CODE)
            
            # Compile Go code
            print("Compiling Go code...")
            subprocess.run(["go", "build", go_file], check=True, cwd=self.temp_dir)
            
            # Run Go benchmarks
            print("Running Go benchmarks...")
            result = subprocess.run(
                ["./benchmark"],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.temp_dir
            )
            
            return json.loads(result.stdout)
