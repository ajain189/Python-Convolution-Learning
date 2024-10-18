# Image Convolution with Custom Kernel

This project applies a convolution operation to a grayscale image using a custom kernel. The program demonstrates the core concepts of kernel convolution, which is commonly used in computer vision and convolutional neural networks (CNNs) for image filtering and feature extraction.

## Project Structure
```
├── images/                 # Directory for input images
│   ├── dog_picture.jpg     # Example image used for convolution
├── lernel_convolution.py   # Python script implementing the convolution operation
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Features
- **Convolution Operation**: Applies a 5x5 Gaussian blur filter using a custom kernel.
- **Image Padding**: Pads the original image with zeros to handle edge pixels during convolution.
- **Pixel Processing**: Each pixel in the image is processed using the convolution operation, and a new filtered image is generated.
- **Output**: The filtered image is displayed after applying the convolution.

## Requirements
- Python 3.8+
- Pillow (PIL)

You can install the dependencies by running:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your input image in the `images/` directory.
2. Modify the `kernel_convolution.py` script to load your image file.
3. Run the script to apply the convolution:
   ```bash
   python kernel_convolution.py
   ```
   The script reads the input image, converts it to grayscale, applies a 5x5 Gaussian blur kernel, and displays the resulting filtered image.

## Learning Objectives
This project was used to understand:
- How convolution works in image processing.
- The role of kernels in feature extraction and image filtering.
- The fundamental concepts behind convolutional neural networks (CNNs).

## Future Work
- Experiment with different kernels for edge detection, sharpening, and other image transformations.
- Extend the project to process images in batches or integrate it into a more complex CNN pipeline.
