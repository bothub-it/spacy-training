import click
import os
import requests


def download(url, name, path):
    print('Downloading: {0}'.format(name))

    request = requests.get(url, stream=True)
    if request.status_code != requests.codes.ok:
        request.raise_for_status()

    total_size = int(request.headers.get('Content-Length'))
    dir_name = os.path.dirname(path)
    temp_name = path + '.temp'

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if os.path.exists(temp_name):
        os.remove(temp_name)
    with click.progressbar(request.iter_content(1024), length=total_size) as bar, open(temp_name, 'wb') as file:
        for chunk in bar:
            file.write(chunk)
            bar.update(len(chunk))
    os.rename(temp_name, path)
