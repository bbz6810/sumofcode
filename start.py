import sys
import time

from language import CreateFactory


def __start__():
    file_path = r'C:\E_HDFS\vmhdfs\zhaopin'
    types = 'python'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        types = sys.argv[2].lower()

    start = time.time()
    CreateFactory.get(types=types).all_file(file_path)
    print(time.time() - start)


if __name__ == '__main__':
    __start__()
