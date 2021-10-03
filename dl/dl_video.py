import requests
from tqdm import tqdm


def down_video(video_link, save_path):
    """Download a video according to its url.

    Args:
        video_link (str): Url of the video.
        save_path (str): Path to save the video.
    """
    resp = requests.get(video_link, stream=True)
    if resp.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in tqdm(resp.iter_content(1024*1024), total=int(int(resp.headers['Content-Length'])/1024/1024)+1):
                f.write(chunk)
    else:
        print(f'Status Code: {resp.status_code}')


if __name__ == '__main__':
    down_video('https://kol-fans.fp.ps.netease.com/file/615728e2c44ad6671b58dff1IkcYWaSQ03', 'test.mp4')
