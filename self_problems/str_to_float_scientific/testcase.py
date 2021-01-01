import unittest
from function import *
import time


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('testcase.txt', 'r') as fp:
            lines = fp.readlines()
        out = []

        start = time.perf_counter()
        for l in lines:
            out.append(str_to_float_scientific(l[:-1], None))

        end = time.perf_counter()
        print(f"{len(lines)} handled in {end - start}")

        with open('output.csv', 'w') as fp:
            out_lines = [f"{lines[i][:-1]},{out[i]}\n" for i in range(0, len(lines))]
            fp.writelines(out_lines)


if __name__ == '__main__':
    unittest.main()
