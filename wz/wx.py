import concurrent.futures as cf
from tqdm import tqdm
import requests
import os


class TouxiangDownloader(object):
    """Downloading heros' images from https://pvp.qq.com/ based on Muti-thread

    Args:
        dir (str): The dir all imgs saved in. Default to './heros/'
    """

    def __init__(self, dir: str = './heros/'):
        """Init method

        Args:
            dir (str): The dir all images saved in. Default to './heros/'
        """
        self.dir = dir
        os.makedirs(dir, exist_ok=True)
        self.api = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.tmp = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{ename}/{ename}.jpg'

    def __save__(self, link: str, path: str):
        """Save method

        Args:
            link (str): Url of the image
            path (str): Save path of the image
        """
        if os.path.exists(path):  # Skip if the image has been downloaded
            pass
        else:
            res = requests.get(link)
            with open(path, 'wb') as f:
                f.write(res.content)

    def __main__(self, max_workers: int = os.cpu_count()):
        """Main method

        Args:
            max_workers (int): The maximum number of threads that can be used to
                execute the given calls. Default to cpu cores on your machine.
        """
        res = requests.get(self.api).json()
        with tqdm(total=len(res)) as pbar:
            with cf.ThreadPoolExecutor(max_workers) as tp:
                for item in res:
                    ename = item['ename']
                    cname = item['cname']
                    link = self.tmp.format(ename=ename)
                    path = self.dir+cname+self.tmp[-4:]
                    tp.submit(self.__save__, link, path).add_done_callback(
                        lambda func: pbar.update()
                    )
        os.system('pause')


if __name__ == '__main__':
    TouxiangDownloader().__main__()
