import urllib.request
from compat_ import urlopen
from download import download


def get(url=None, streaming=False, headers=False,chunk_size= 8 * 1024):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)

    if streaming:
        return stream_response(response, chunk_size)
    elif headers:
        # https://github.com/nficano/pytube/issues/160
        return {k.lower(): v for k, v in response.info().items()}
    return (
        response
        .read()
        .decode('utf-8')
    )
    
def stream_response(response, chunk_size=8 * 1024):
    """Read the response in chunks."""
    while True:
        buf = response.read(chunk_size)
        if not buf:
            break
        yield buf

def on_progress(chunk, file_handler, bytes_remaining):
    file_handler.write(chunk)
    print(bytes_remaining)


def download_(url=None, path=None):
    bytes_remaining = int(get(url, headers=True)['content-length'])
    with open(path, 'wb') as fh:
        for chunk in get(url, streaming=True):
            bytes_remaining -= len(chunk)
            print(bytes_remaining)
            # reduce the (bytes) remainder by the length of the chunk.
            # send to the on_progress callback.
            on_progress(chunk, fh)

def on_progress(chunk, file_handler):
    file_handler.write(chunk)




