# qrDocumentIndexer
A python library for tagging PDF documents with QR codes so that they can be rebuilt into the same document structure after being printed and scanned back.

## Purpose

This library is intended to be used where documents may be printed and then subsequently scanned back to digital format. Normally
this process would result in the loss of any format structure. The documents may even be scanned back in different orders. This
can be particularly common in the cases where documents being printed are technical drawings and they may be re-ordered for
review or other purposes before being scanned again.

This library is intended to store the following information about each page of a PDF in a QR code:
- Filename
- Page number
- Bookmarks (including nesting)

This information can then be used to restructure the documents after scanning. This should even be possible if documents
are scanned into multiple PDFs or image files.

Additional metadata that could be included in future could include:
- Pagesizes
- Paper orientation
