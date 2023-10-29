from PIL import Image

def resize(imagePath):

    # Open the image
    image = Image.open(imagePath)

    # Reduce the image size by 50%
    new_image = image.resize((image.width // 7, image.height // 7))

    # Save the resized image
    new_image.save("artwork_resized.jpg", quality=99)

    return new_image