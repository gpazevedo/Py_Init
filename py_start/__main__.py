import os
import sys

from py_start.py_start import fib

if __name__ == "__main__":
    runtime_env = os.environ.get("RUNTIME_ENV")
    if runtime_env is None:
        runtime_env = "dev"

    print("Run time environment:", runtime_env)

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(fib(n))
    else:
        print("Please use an integer argument!")
