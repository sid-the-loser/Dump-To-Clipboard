import argparse
import os
import custom_errors
import pyperclip

program_version = "r1.0.0"

clipboard_filesize_limit = 1073741824

parser = argparse.ArgumentParser(prog=f"Dump To Clipboard (dtcb) - {program_version}",
                                 description="Doesn't the name explain what it does?")

parser.add_argument("filename", type=str, help="Enter the filename of the file data you'd like to copy")

parser.add_argument("-b", "--bin", action="store_true", help="Tells the program to open the file as a binary file rather than a plain text file")
parser.add_argument("-f", "--force", action="store_true", help=f"Removes the program set limitation of {clipboard_filesize_limit}")

args = parser.parse_args()

filename = args.filename
_force = args.force
_bin = args.bin

filesize = os.path.getsize(filename)

if (filesize > clipboard_filesize_limit) and (not _force):
    raise custom_errors.TooBigForMeToHandle(f"{filename} is too big! ({clipboard_filesize_limit} bytes is the limit, the file you choose was {filesize} bytes)")

if not _bin:
    file_data = open(filename).read()
else:
    file_data = open(filename, "rb").read()

pyperclip.copy(str(file_data))
print(f"{filename} copied to clipboard!")