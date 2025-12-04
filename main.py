import json
import os
import magic

# reads signatures.json to get a list of dictionaries of file types
def load_signatures():
    with open('signatures.json', 'r') as f:
        signatures = json.load(f)
        return signatures

# reads the first 16 bytes of the file in binary, then converts to hex
def read_file_magic(filename):
    with open(filename, mode='rb') as f:
        file_content_binary = f.read(16)
        file_content_hex = file_content_binary.hex().upper()
        return file_content_hex

# takes the list of signature dicts and the file hex to identify the actual file type
def detect_file_type(signatures, file_content_hex):
    for fileType in signatures:
        if fileType['sign'] in file_content_hex:
            return fileType['format']
    return "Unknown or text file"

def detect_file_extension(filename):
    extension = os.path.splitext(filename)[1]
    return extension

def cmd_output(filename):
    file_cmd_output = magic.from_file(filename)
    return file_cmd_output

def main():
    # user enters the file that they want to verify
    filename = input("Enter the file name you want to analyze: ")

    # calling functions to create variables
    signatures = load_signatures()
    file_content_hex = read_file_magic(filename)

    # calling detect_file_type to find the actual file type
    file_type = detect_file_type(signatures, file_content_hex)
    # calling detect_file_extension to find the assumed file extension
    file_extension = detect_file_extension(filename)
    # calling cmd_file to find the file command output
    cmd_file = cmd_output(filename)

    print(f"Magic Number Analysis:",
          f"\nRaw hex: {file_content_hex}",
          f"\nDetected file type: {file_type}",
          f"\n\nFile extension:{file_extension}",
          f"\n\nFile command output:\n{cmd_file}",
          f"\n\nNote: Before proceeding make sure that the magic number matches the file extension!"
          )

if __name__ == "__main__":
    main()