import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from main import start_application

if __name__ == "__main__":
    start_application()