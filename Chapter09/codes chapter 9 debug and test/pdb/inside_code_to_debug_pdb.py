import pdb


class Pdb_test(object):
    def __init__(self, parameter):
        self.counter = parameter

    def go(self):
        for j in range(self.counter):
            pdb.set_trace()
            print("--->", j)
        return


if __name__ == "__main__":
    Pdb_test(10).go()
