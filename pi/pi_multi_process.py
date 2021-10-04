import concurrent.futures as cf
from tqdm import tqdm
import random
import os


class PI(object):
    """Calculate the value of π by multi process

    Args:
        num_iterations (int): Number of iterations. Default: 100000
        max_workers (int): Maximum number of processes. Default: the number of processors on the machine.
    """

    def __init__(self, num_iterations: int = int(1e7), max_workers: int = os.cpu_count()) -> None:
        """Initialization

        Args:
            num_iterations (int): Number of iterations. Default: 100000
            max_workers (int): Maximum number of processes. Default: the number of processors on the machine.
        """
        self.num_iterations = num_iterations
        self.max_workers = max_workers

    def __calc__(self, start: int, end: int) -> float:
        """Calculate the value of π according to formula

        Args:
            start (int): Starting value for the iterations
            end (int): Ending value for the iterations

        Returns:
            float: Value of π
        """
        N = 0
        for i in tqdm(range(start, end)):
            x = random.random()
            y = random.random()
            d = (x-0.5)**2+(y-0.5)**2
            if d <= 0.5**2:
                N += 1
            else:
                pass
        return N

    def __main__(self) -> float:
        """Calulate the value of π by multi process

        Returns:
            float: Value of π
        """
        N = 0
        with cf.ProcessPoolExecutor(self.max_workers) as p:
            futures = []
            for i in range(self.max_workers):
                start = i*self.num_iterations//self.max_workers
                end = (i+1)*self.num_iterations//self.max_workers
                futures.append(p.submit(self.__calc__, start, end))
            for future in cf.as_completed(futures):
                N += future.result()
        return 4*N/self.num_iterations


if __name__ == '__main__':
    print(PI().__main__())
