from PIL import Image
from pillow_heif import register_heif_opener
import pillow_heif 
from tkinter.filedialog import askdirectory
import os
import argparse

#start the HEIF opener
register_heif_opener()


def convert_heic_to_jpg(heic_path:str,metadata:bool=True,jpg_path:str=None):
    """Converts heic image to jpg
    Args:
        heic_path (str): Path to the folder with heic images
    """
    heic: pillow_heif.as_plugin.HeifImageFile  = Image.open(heic_path)

    # Extract metadata from HEIC file
    exif_data: bytes = heic.info.get('exif')

    # path for exporting jpg image
    if jpg_path is None:
        jpg_path:str = heic_path.replace('.heic', '.jpg').replace(".HEIC",".jpg")

    if exif_data and metadata: 
        # Save the image as jpg with exif data
        heic.save(jpg_path, 'JPEG', exif=exif_data)
        print("Converted:",jpg_path, "with metadata")
    else:
        heic.save(jpg_path, 'JPEG')
        print("Converted:",jpg_path)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert HEIC to JPG')

    parser.add_argument("-he",'--heic', help='Path to HEIC file',type=str,default=None)
    parser.add_argument("-j",'--jpg', help='Path to save converted JPG file',type=str,default=None)
    parser.add_argument("-f",'--folder', help='Path to HEIC folder',type=str,default=None)
    parser.add_argument("-m",'--metadata', help='Export metadata',type=bool,default=True)

    args: argparse.Namespace = parser.parse_args()

    imagedirectory:str = args.folder

    if args.heic:
        convert_heic_to_jpg(args.heic,metadata=args.metadata,jpg_path=args.jpg)
    elif args.folder is None:
        # Select HEIC file folder interactively
        imagedirectory = askdirectory(title='Select directory to convert HEIC to JPG images')

    if imagedirectory is not None:
        for imagepath in os.listdir(imagedirectory):
            if imagepath.endswith('.HEIC') or imagepath.endswith('.heic'):
                convert_heic_to_jpg(os.path.join(imagedirectory, imagepath))