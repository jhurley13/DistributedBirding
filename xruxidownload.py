# https://gist.github.com/ruxi/5d6803c116ec1130d484a4ab8c00c603

__author__  = "github.com/ruxi"
__license__ = "MIT"
import requests
import tqdm     # progress bar
import os.path
def download_file(url, filename=False, verbose = False):
    """
    Download file with progressbar
    
    Usage:
        download_file('http://web4host.net/5MB.zip')  
    """
    if not filename:
        local_filename = os.path.join(".",url.split('/')[-1])
    else:
        local_filename = filename

    try:
        r = requests.get(url, stream=True)
        # print(r.headers)
        file_size = int(r.headers.get('Content-Length', 1000000)
        chunk = 1
        chunk_size=1024
        num_bars = int(file_size / chunk_size)
        if verbose:
            print(dict(file_size=file_size))
            print(dict(num_bars=num_bars))

        with open(local_filename, 'wb') as fp:
            for chunk in tqdm.tqdm(
                    r.iter_content(chunk_size=chunk_size)
                    , total= num_bars
                    , unit = 'KB'
                    , desc = local_filename
                    , leave = True # progressbar stays
            ):
                fp.write(chunk)
    except Exception as ee:
        print(r.headers)
        print(ee)
        raise

    return
    