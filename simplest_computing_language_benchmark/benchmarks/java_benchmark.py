import os
import subprocess
import json
from typing import Dict
from .base_benchmark import BaseBenchmark
from ..templates.java_template import JAVA_CODE

class JavaBenchmark(BaseBenchmark):
    def run(self) -> Dict[str, float]:
        with self:  # Use context manager for temp directory
            # Write Java code to temp directory
            java_file = os.path.join(self.temp_dir, "Benchmarks.java")
            with open(java_file, "w") as f:
                f.write(JAVA_CODE)
            
            # Compile Java code
            print("Compiling Java code...")
            subprocess.run(["javac", java_file], check=True, cwd=self.temp_dir)
            
            # Run Java benchmarks
            print("Running Java benchmarks...")
            result = subprocess.run(
                ["java", "-cp", self.temp_dir, "Benchmarks"],
                capture_output=True,
                text=True,
                check=True
            )
            
            return json.loads(result.stdout)
