from PIL import Image, ImageOps     

def sum_kernel_region(kernel, region):
    height = len(region)
    width = len(region[0])
    total = 0

    for i in range(height):
        for j in range(width):
            x = kernel[i][j] * region[i][j]
            total += x
    
    return total

def create_0_array(height, width):
    return [[0] * width for _ in range(height)]

def pad0s(img,layers):
    original_height = img.height
    original_width = img.width

    new_height = original_height + 2 * layers
    new_width = original_width + 2 * layers

    padded_image = create_0_array(new_height, new_width)

    for i in range(original_height):
        for j in range(original_width):
            padded_image[i + layers][j + layers] = int(img.getpixel((j, i)))
    
    return padded_image

def convolve(image, kernel):
    image_height = image.height
    image_width = image.width  
    kernel_height = len(kernel)
    kernel_width = len(kernel[0])

    pad_amount = kernel_height // 2
    padded_image = pad0s(image, pad_amount)
    output_image = create_0_array(image_height, image_width)

    for i in range(image_height):
        for j in range(image_width):
            region = [row[j:j+kernel_width] for row in padded_image[i:i+kernel_height]]
            output_value = sum_kernel_region(kernel, region)
            if (i % 50 == 0 and j % 50 == 0):  # Print every 50th value for debugging
                print(f"Region: {region}")
                print(f"Output Value: {output_value}")
            output_image[i][j] = max(0, min(255, int(output_value)))

    return output_image

im1 = Image.open(r"C:/Users/tarun/Downloads/Python Convolution Learning/dog_picture.jpg") 

im2 = ImageOps.grayscale(im1)

kernel = [
    [1/256,  4/256,  6/256,  4/256,  1/256],
    [4/256, 16/256, 24/256, 16/256,  4/256],
    [6/256, 24/256, 36/256, 24/256,  6/256],
    [4/256, 16/256, 24/256, 16/256,  4/256],
    [1/256,  4/256,  6/256,  4/256,  1/256]
]

convolved_image = convolve(im2, kernel)

output_image = Image.new("L", (im2.width, im2.height))
output_image.putdata([pixel for row in convolved_image for pixel in row])
output_image.show()