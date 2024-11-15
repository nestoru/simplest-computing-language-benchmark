# Simplest Computing Language Benchmark
This project aims at a minimalistic way to show how different computing languages compare with each other.

While it is written in python it invokes the same three simple algorithms in several computing languages that I had to use recently.

* The array benchmark tries to measure the performance for memory and CPU intensive processing..
* The string concat benchmark tries to measure the performance for memory intensive processing.
* The math benchmark tries to measure the performance for CPU intensive processing.

## Project structure
```
.
├── README.md
├── poetry.lock
├── pyproject.toml
└── simplest_computing_language_benchmark
    ├── __init__.py
    ├── benchmarks
    │   ├── __init__.py
    │   ├── base_benchmark.py
    │   ├── go_benchmark.py
    │   ├── java_benchmark.py
    │   ├── nodejs_benchmark.py
    │   └── python_benchmark.py
    ├── core
    │   ├── __init__.py
    │   ├── benchmark_suite.py
    │   └── system_info.py
    └── templates
        ├── __init__.py
        ├── go_template.py
        ├── java_template.py
        └── nodejs_template.py
```

## Intall
```
poetry install
```

## Usage
```
poetry run run-benchmark
```
