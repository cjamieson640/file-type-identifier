# File Type Identifier (Magic Number Scanner)

**Summary**
Identifies the true file type by inspecting magic numbers, helping detect disguised or malicious files.

---

## Overview
This File Type Identifier is designed to help users verify the true file type of a file they are working with. Attackers often attempt to hide malicious code through **Masquerading Attacks** (**File Extension Spoofing**) by renaming an executable file to something harmless such as changing an `.exe` to `.jpg`.

If a user unknowingly downloads and opens a disguised file, it could result in malware infections, data loss, or even compromise an entire system. This tool helps prevent that by confirming whether a file actually matches the file type it claims to be.

---

## How it Works
This project identifies file types using their **magic numbers**, which are the first bits of a file which uniquely identify the type of file.

The process:
1. The user inputs the file they want to verify.
2. The program opens the file in binary mode and reads the first 16 bytes.
3. The bytes are converted into a hexadecimal string which is the file's magic number.
4. The program compares the hexadecimal string to a JSON database of known magic numbers and the corresponding file types.
5. The tool outputs the file's *actual* type based on its signature and allows the user to compare to the original file extension.

This method identifies the real file type **even if the extension has been tampered with**.

---

## Tools and Data Sources
- **Python**: Uses to build the identifier and perform bindary/hex processing.
- **JSON Magic Number Database**: A list of known magic numbers and associated file types sourced from [GitGist](https://gist.github.com/TotallyNotAHaxxer/4c971ea9fd8fe78f862a27fa9ba96762)

---

## Business and Personal Application
A file type identifier provides value to both individuals and organizations:

### Security and Threat Prevention
Attackers frequently disguise malicious files as harmless images or documents. This tool helps users validate unfamiliar files before they open or download them, reducing the risk of malware infections.

### Digital Forensics and Incident Response
Forensic analysts often come across unknown or mislabeled files during investigations. This tool lets them quickly determine whether a file is what it claims to be before performing deeper analysis.

### Accurate and Safe File Handling
Verifying file types ensures system integrity, prevents workflow errors, and supports safer file processing.

By checking file signatures instead of relying on file extensions, this tool strengthens security and improves confidence when dealing with unfamiliar or suspicious files.

---
