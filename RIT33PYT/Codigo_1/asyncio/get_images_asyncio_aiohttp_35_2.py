import atexit
import sys
from os import sep

import asyncio
import aiohttp
from pyaio.gevent import aioFile

from bs4 import BeautifulSoup
from urllib.parse import urlparse

from timeit import timeit


async def wget(session, url):
    with aiohttp.Timeout(1):
        async with session.get(url) as response:
            assert response.status == 200
            return await response.read()


async def download(session, uri):
    """
    Guarda en disco un archivo indicado por una URL

    Argumento :
    > uri (str, por ejemplo 'http://www.inspyration.org/logo.png')

    Retorno :
    > contenido de un archivo (bytes, archivo textual o binario)
    """
    print("Write {} started".format(uri))
    content = await wget(session, uri)
    if content is None:
        return None
    with aioFile(uri.split(sep)[-1], "wb") as f:
        f.write(content)
        print("Write {} ended".format(uri))
        return uri


def get_images_src_from_html(html_doc):
    """Recupera todo el contenido de los atributos src de las etiquetas img"""
    soup = BeautifulSoup(html_doc, "html.parser")
    return (img.get('src') for img in soup.find_all('img'))


def get_uri_from_images_src(base_uri, images_src):
    """Retorna una a una cada URL de imagen a descargar"""
    parsed_base = urlparse(base_uri)
    for src in images_src:
        parsed = urlparse(src)
        if parsed.netloc == '':
            path = parsed.path
            if parsed.query:
                path += '?' + parsed.query
            if path[0] != '/':
                if parsed_base.path == '/':
                    path = '/' + path
                else:
                    path = '/' + '/'.join(parsed_base.path.split('/')[:-1]) + '/' + path
            yield parsed_base.scheme + '://' + parsed_base.netloc + path
        else:
            yield parsed.geturl()

def get_images(page_uri):
    #
    # Recuperación de las URL de todas las imágenes de una página
    #
    print("### GET_IMAGES")
#    import pdb; pdb.set_trace()
    loop = asyncio.get_event_loop()
    with aiohttp.ClientSession(loop=loop) as session:
        print("### GET IMAGES: HTML")
        html = loop.run_until_complete(wget(session, page_uri))
        print("### GET IMAGES: HTML Done")

        if not html:
            print("Error: La página web no se ha encontrado o analizado", sys.stderr)
            return None
        images_src_gen = get_images_src_from_html(html)
        images_uri_gen = get_uri_from_images_src(page_uri, images_src_gen)

        print("### GET IMAGES")
        loop.run_until_complete(
            asyncio.wait([download(session, image_uri) for image_uri in images_uri_gen]))
        #loop.close()
        print("### GET IMAGES Done")

#    import pdb; pdb.set_trace()
    #
    # Recuperación de las imágenes
    #
#    for image_uri in images_uri_gen:
#        print('Descarga de %s' % image_uri)
#        await download(image_uri)

def close_loop():
    loop = asyncio.get_event_loop()
    loop.close()
atexit.register(close_loop)


if __name__ == '__main__':
    print('--- Starting standard download ---')
    web_page_uri = 'http://www.formation-python.com/'
    print(timeit('get_images(web_page_uri)',
                 number=10,
                 setup="from __main__ import get_images, web_page_uri"))

