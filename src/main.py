import argparse
import pyperclip

program_version = "pr1.0.0"


parser = argparse.ArgumentParser(prog=f"Dump To Clipboard (DTC) - {program_version}",
                                 description="Doesn't the name explain what it does?")

parser.add_argument("filename", type=str, help="Enter the filename of the file data you'd like to copy")

parser.add_argument("-f", "--force", action="store_true", help="Removes the program set limitation")