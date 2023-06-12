import argparse
import os

from termcolor import colored

from qrDocumentIndexer.pdf_ingest import QR_POSITION, PDFIngest

def main():
    parser = argparse.ArgumentParser()
    mutual_exclusive = parser.add_mutually_exclusive_group()
    mutual_exclusive.add_argument('-i', '--insert-qr-codes', help ="""Insert QR codes into a given PDF. PDF will save over the original PDF""",
                                  action='store_true')
    
    parser.add_argument('-p', '--position', help="Location to insert QR code into document. Default is top left.",
                        type=QR_POSITION, choices=list(QR_POSITION), default=QR_POSITION.TOP_LEFT)
    
    parser.add_argument('-s', '--size', help="Size of QR code in multiples of page width. Default is 0.1.",
                        type=float, default=0.1)
    
    parser.add_argument('-o', '--offset', help="Offset of the QR code from the corner of the document. Size in mm, default is 5.",
                        type=int, default=5)
    
    parser.add_argument

    args = parser.parse_args()
    if not args.insert_qr_codes:
        print("No action selected, terminating.")
        return
    else:
        while True:
            filenames = input("Paste filepath and hit enter to insert QR codes into a file. Hit enter with no filepath to close:")
            if filenames.strip() == '':
                print("\tNo filepath found. Terminating.")
                return
            filepath = filenames.strip('"\'& ')
            print(f'\tAttempting to load file: {filepath}')
            if not os.path.isfile(filepath):
                text = colored(f'\tFilepath "{filepath}" could not be found. Please ensure you are providing a valid filepath.', 'red')
                print(text)
                continue
            try:
                ingester = PDFIngest(filepath)
                print(f'\tSuccessfully loaded file. Found {len(ingester.page_metadata)} pages. Attempting to insert QR codes.')
                ingester.insert_qr_codes(args.position, True, args.offset, args.size)
                text = colored(f'\tSuccessfully inserted QR codes for file: "{filepath}"', 'green')
                print(text)
            except Exception as ex:
                text = colored(f'\tFailed to insert QR codes. Received exception: {ex}', 'red')
                print(text)



if __name__ == '__main__':
    main()