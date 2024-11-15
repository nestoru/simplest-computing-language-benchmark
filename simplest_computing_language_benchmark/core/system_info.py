import platform
import psutil
import subprocess
import os
import sys
from typing import Dict

class SystemInfo:
    def __init__(self):
        self.info = self._gather_system_info()

    def _get_cpu_info(self) -> Dict:
        """Get CPU information based on the operating system."""
        cpu_info = {}
        if platform.system() == "Darwin":  # macOS
            try:
                cpu_brand = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string']).decode().strip()
            except:
                cpu_brand = "Apple Silicon"
            cpu_info = {
                'brand': cpu_brand,
                'cores': os.cpu_count()
            }
        else:
            cpu_info = {
                'brand': platform.processor(),
                'cores': os.cpu_count()
            }
        return cpu_info

    def _gather_system_info(self) -> Dict:
        """Gather all system information."""
        memory = psutil.virtual_memory()
        
        # Get language versions
        python_version = sys.version.split()[0]
        java_version = subprocess.check_output(['java', '-version'], 
                                           stderr=subprocess.STDOUT).decode().split('\n')[0].split('"')[1]
        node_version = subprocess.check_output(['node', '--version']).decode().strip()
        go_version = subprocess.check_output(['go', 'version']).decode().strip().split(" ")[2]

        return {
            'system': platform.system(),
            'machine': platform.machine(),
            'cpu': self._get_cpu_info(),
            'memory_total': f"{memory.total / (1024**3):.1f}GB",
            'memory_available': f"{memory.available / (1024**3):.1f}GB",
            'python_version': python_version,
            'java_version': java_version,
            'node_version': node_version,
            'go_version': go_version
        }

    def print_info(self):
        """Print system information in a formatted way."""
        print("\nHardware & Software Configuration:")
        print("-" * 50)
        print(f"System: {self.info['system']} {self.info['machine']}")
        print(f"CPU: {self.info['cpu']['brand']}")
        print(f"CPU Cores: {self.info['cpu']['cores']}")
        print(f"Memory: {self.info['memory_total']} (Available: {self.info['memory_available']})")
        print("\nLanguage Versions:")
        print(f"Python: {self.info['python_version']}")
        print(f"Java: {self.info['java_version']}")
        print(f"Node.js: {self.info['node_version']}")
        print(f"Go: {self.info['go_version']}")
        print("-" * 50)
