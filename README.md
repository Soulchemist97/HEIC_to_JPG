# HEIC to JPG converter
A short Pillow based script to convert HEIC (High efficiency Image Codec) to JPEG

- Works with Terminal Command or with interactive folder Dialog


## Terminal Commands

`python HEIC_JPG_Converter.py -h`

No flag will start `askdirectory` from `tkinter.filedialog`

### Options

| Option                      | Description                        |
|-----------------------------|------------------------------------|
| `-h, --help`                | Show help message and exit         |
| `-he HEIC, --heic HEIC`     | Path to HEIC file                  |
| `-j JPG, --jpg JPG`         | Path to save converted JPG file    |
| `-f FOLDER, --folder FOLDER`| Path to HEIC folder                |
| `-m METADATA, --metadata METADATA` | Export metadata (Default=True)             |

## Requirements

| Package       | Version |
|---------------|---------|
| Pillow        | 10.4.0   |
| pillow-heif   | 0.18.0   |
