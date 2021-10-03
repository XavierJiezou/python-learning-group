import requests


def down_image(image_link: str, save_path: str):
    """Download an image according to its url.

    Args:
        image_link (str): Url of the image.
        save_path (str): Path to save the image.
    """
    resp = requests.get(image_link)
    if resp.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(resp.content)
    else:
        print(f'Status Code: {resp.status_code}')


if __name__ == '__main__':
    down_image('https://cn.bing.com/th?id=OHR.Italica_EN-CN5244072694_1920x1200.jpg&rf=LaDigue_1920x1200.jpg', 'test.jpg')
