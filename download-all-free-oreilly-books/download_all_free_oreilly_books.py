import re
import os
import requests


def download_file(url, download_dir):
    # Adapted from http://stackoverflow.com/a/16696317
    local_filename = url.split('/')[-1]
    file_dir = "".join(local_filename.split('.')[:-1])
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    os.makedirs("./{}/{}".format(download_dir, file_dir), exist_ok=True)
    file_save_path = "./{}/{}/{}".format(download_dir, file_dir, local_filename)
    # If file is fully downloaded don't redownload it
    # This can also can update when a new version is published
    if local_file_size(file_save_path) != get_file_size(url):
        print("Downloading file")
        with open(file_save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    else:
        print("File already downloaded")


def download_all_from_urls(endings, urls, download_dir):
    combinations = (url.replace('.csp', ending)
                   .replace('/free/', '/free/files/')
                for url in urls
                for ending in endings)

    for combination in combinations:
        print(combination)
        download_file(combination, download_dir)


def get_urls(dl_type):
    data = requests.get('http://www.oreilly.com/{}/free/'.format(dl_type))

    # Other URLs
    # Don't worry, I'm not _parsing_ html with regex. Merely scraping it. :)
    pattern = re.compile('http://www.oreilly.com/{}/free.*\.csp'.format(dl_type))

    urls = pattern.findall(data.text)
    return urls


def get_main_urls():
    "A function to get all the pages that have free ebooks on"
    data = requests.get('http://www.oreilly.com/programming/free/')

    # Just match the name not the whole URL
    pattern = re.compile('(?<=oreilly\.com\/)(.*)(?=\/free\/)')

    urls = pattern.findall(data.text)
    # Remove duplicates
    urls = list(set(urls))
    return urls


def get_file_size(url):
    "Read the length of a file from the file header it is in Bytes"
    response = requests.head(url)
    return int(response.headers['Content-Length'])


def local_file_size(path_to_file):
    "Return the file size in bytes and 0 if not exist"
    try:
        return os.path.getsize(path_to_file)
    except:
        return 0


file_types = ['.pdf', '.mobi', '.epub']
download_types = get_main_urls()

for download_type in download_types:
    urls = get_urls(download_type)
    download_all_from_urls(file_types, urls, download_type)
