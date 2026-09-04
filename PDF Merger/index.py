import os
from PyPDF2 import PdfWriter
from errors import *


def get_pdf_list():
    """Prompt the user for file count and names, with retry-safe validation."""
    while True:
        pdfs = []  # reset every attempt so failed runs don't leave stale entries
        try:
            ask_n_of_pdfs = int(input('How many PDF(s) you want to merge: '))

            if ask_n_of_pdfs < 0:
                raise NegativeIntegerError

            elif ask_n_of_pdfs in (0, 1):
                raise ZeroOrOneFilesError

            for i in range(ask_n_of_pdfs):
                # each filename gets its OWN retry loop, separate from the
                # "how many files" question above
                while True:
                    ask_file_name = input(f'Enter the name of PDF {i + 1} (accurately): ').strip()

                    if not ask_file_name.lower().endswith('.pdf'):
                        ask_file_name += '.pdf'

                    if not os.path.isfile(ask_file_name):
                        print(f' # "{ask_file_name}" not found! Please try again.\n')
                        continue  # only re-asks THIS filename

                    pdfs.append(ask_file_name)
                    break

            return pdfs

        except ValueError:
            print(' # Invalid value. Please enter a number.\n')
        except NegativeIntegerError:
            print(' # Negative numbers are not allowed!\n')
        except ZeroOrOneFilesError:
            print(' # The entered number of files cannot be merged.\n')


def merge_pdfs(pdfs, output_name="merged-pdf.pdf"):
    merger = PdfWriter()
    try:
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(output_name)
        print(f'\n✅ Merged {len(pdfs)} file(s) into "{output_name}"')
    finally:
        merger.close()


def main():
    pdfs = get_pdf_list()
    merge_pdfs(pdfs)


if __name__ == '__main__':
    main()