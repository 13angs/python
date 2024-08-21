# File Renaming Script

This script iterates through all file files in a specified directory and renames any files that contain spaces (` `) in their filenames, replacing the spaces with hyphens (`-`).

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Notes](#notes)

## Requirements

This script is written in Python and requires Python 3.x to run. It only uses standard libraries, so no additional installations are required.

## Installation

1. Clone this repository or download the script.

```bash
git clone https://github.com/13angs/file-renaming-script.git
cd file-renaming-script
```

2. Ensure you have a `data` directory in the same location as the script. This directory should contain the file files you want to process.

## Usage

1. Place all the files you want to rename into a directory named `data`.

2. Run the script by executing the following command in your terminal:

```bash
python rename_files.py
```

This will rename all files in the `data` directory that contain spaces in their names, replacing the spaces with hyphens.

### Example

Assume you have the following files in your `data` directory:

```
data/
├── file one.jpg
├── file two.png
└── file three.jpeg
```

After running the script, the files will be renamed as follows:

```
data/
├── file-one.jpg
├── file-two.png
└── file-three.jpeg
```

### Notes

- The script does not differentiate between file types. It will rename any file in the `data` directory that contains spaces in its name, not just file files.
- If you need to limit the renaming to specific file types (e.g., `.jpg`, `.png`), you can modify the script accordingly.
- Ensure that the script has the necessary permissions to rename files in the `data` directory.

### Customization

If you need to customize the script further, such as filtering by file types or handling different directories, you can edit the `rename_files.py` script according to your requirements.