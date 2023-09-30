from PIL import Image

from qrDocumentIndexer.page_info import PageInfo
from qrDocumentIndexer.scanned_page import ScannedPage
from qrDocumentIndexer.reconstituted_document import ReconstitutedDocument, BLANK_PAGE

FILENAME = 'file.pdf'

def test_unordered_pages_sorted_in_correct_order():
    im = Image.Image()

    pages = [
        ScannedPage(im),
        ScannedPage(im),
        ScannedPage(im),
    ]

    pages[0]._page_info = PageInfo(FILENAME, 3, [])
    pages[1]._page_info = PageInfo(FILENAME, 1, [])
    pages[2]._page_info = PageInfo(FILENAME, 2, [])

    doc = ReconstitutedDocument(pages, FILENAME)

    assert doc._filename == FILENAME
    assert doc.sorted_pages == [
        pages[1],
        pages[2],
        pages[0]
    ]

def test_missing_page_is_replaced_with_blank_page():
    im = Image.Image()

    pages = [
        ScannedPage(im),
        ScannedPage(im),
    ]

    pages[0]._page_info = PageInfo(FILENAME, 3, [])
    pages[1]._page_info = PageInfo(FILENAME, 1, [])

    doc = ReconstitutedDocument(pages, FILENAME)

    assert doc._filename == FILENAME
    assert doc.sorted_pages == [
        pages[1],
        BLANK_PAGE,
        pages[0],
        
    ]

def test_multiple_pages_with_same_page_number_inserted_sequentially_in_order_found():
    im = Image.Image()

    pages = [
        ScannedPage(im),
        ScannedPage(im),
        ScannedPage(im),
        ScannedPage(im),
    ]

    pages[0]._page_info = PageInfo(FILENAME, 3, [])
    pages[1]._page_info = PageInfo(FILENAME, 1, [])
    pages[2]._page_info = PageInfo(FILENAME, 2, [])
    pages[3]._page_info = PageInfo(FILENAME, 1, [])

    doc = ReconstitutedDocument(pages, FILENAME)

    assert doc._filename == FILENAME
    assert doc.sorted_pages == [
        pages[1],
        pages[3],
        pages[2],
        pages[0]
    ]

def test_blanks_still_inserted_when_multiple_pages_with_same_page_number_inserted_sequentially_in_order_found():
    im = Image.Image()

    pages = [
        ScannedPage(im),
        ScannedPage(im),
        ScannedPage(im),
    ]

    pages[0]._page_info = PageInfo(FILENAME, 3, [])
    pages[1]._page_info = PageInfo(FILENAME, 1, [])
    pages[2]._page_info = PageInfo(FILENAME, 1, [])

    doc = ReconstitutedDocument(pages, FILENAME)

    assert doc._filename == FILENAME
    assert doc.sorted_pages == [
        pages[1],
        pages[2],
        BLANK_PAGE,
        pages[0]
    ]

def test_blanks_inserted_for_first_page():
    im = Image.Image()

    pages = [
        ScannedPage(im),
        ScannedPage(im),
    ]

    pages[0]._page_info = PageInfo(FILENAME, 3, [])
    pages[1]._page_info = PageInfo(FILENAME, 2, [])

    doc = ReconstitutedDocument(pages, FILENAME)

    assert doc._filename == FILENAME
    assert doc.sorted_pages == [
        BLANK_PAGE,
        pages[1],
        pages[0],
    ]