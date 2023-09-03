from PIL.Image import Image
from fitz.fitz import Page, Pixmap
from qreader import QReader
import numpy as np

from qrDocumentIndexer.page_info import PageInfo

class ScannedPage:
    def __init__(self, page: Image | Page) -> None:
        if isinstance(page, Image):
            self._image = page
        elif isinstance(page, Page):
            self._pdf_page = page
        else:
            raise TypeError('Page type is not valid')
    
    def _scan_page_info(self):
        qreader = QReader()
        results = ()
        if hasattr(self, '_image') and self._image:
            pix_array = np.array(self._image.convert("RGB"))
            results = qreader.detect_and_decode(pix_array)
        elif hasattr(self, '_pdf_page') and self._pdf_page:
            image: Pixmap = self._pdf_page.get_pixmap()
            pix_array = np.frombuffer(buffer=image.samples, dtype=np.uint8).reshape((image.height, image.width, -1))
            results = qreader.detect_and_decode(pix_array)

        for code in results:
            try:
                decoded: PageInfo = PageInfo.fromJson(code)
            except:
                continue

            self._page_info: PageInfo = decoded
            return

        self._page_info: PageInfo = None

    @property
    def page_info(self) -> PageInfo:
        if not hasattr(self, '_page_info'):
            self._scan_page_info()

        return self._page_info