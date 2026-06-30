# -Bulk-Image-Resizer
Bulk Image Resizer is a Python desktop application that resizes multiple images at once while maintaining high quality. It supports popular image formats such as JPG, JPEG, PNG, BMP, GIF, TIFF, and WebP. Users can resize images by specifying custom width and height, choose an output folder, and process hundreds of images in a single click. 

Bulk Image Resizer

A simple Python desktop application that allows users to resize multiple images at once while preserving image quality.

Features

• Resize hundreds of images in one click
• Supports JPG, JPEG, PNG, BMP, GIF, TIFF, and WebP
• Choose custom width and height
• Select multiple images at once
• Save resized images to a separate folder
• Maintains image quality using high-quality resampling
• Simple and beginner-friendly GUI built with Tkinter
• Cross-platform (Windows, Linux, macOS)

Technologies Used

- Python 3
- Tkinter
- Pillow (PIL)

Project Structure

```
Bulk-Image-Resizer/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── output/
```

Installation

Clone the repository

```
git clone https://github.com/yourusername/Bulk-Image-Resizer.git
```

Move into the project

```
cd Bulk-Image-Resizer
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python main.py
```

Requirements

```
Pillow
```

Usage

1. Open the application.
2. Click Select Images.
3. Choose one or more images.
4. Enter Width and Height.
5. Select an Output Folder.
6. Click Resize Images.
7. Resized images will be saved automatically.

Supported Formats

- JPG
- JPEG
- PNG
- BMP
- GIF
- TIFF
- WebP

Future Improvements

- Drag and Drop support
- Percentage resizing
- Maintain aspect ratio option
- Compression quality slider
- Batch image conversion
- Rename files while resizing
- Dark mode
- Preview before resizing

License

This project is licensed under the MIT License.

Author

Shoheb Mulla
