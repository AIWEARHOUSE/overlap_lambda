from PIL import Image

def overlay(resizedImage, isMen):

    # Open the base image and the overlay image
    base_image = None

   #Check if it is Men 
    if not isMen:
        base_image = Image.open("men-retail.png")
    else:
        base_image = Image.open("women-retail.png")

    # Set up overlay image same as the resized image
    overlay_image = resizedImage

    # Create a new image that is the size of the base image
    new_image = Image.new("RGB", base_image.size)
    new_image.paste(base_image, (0,0))

    # Paste the overlay image onto the new image at the specified coordinate
    new_image.paste(overlay_image, (460, 500))

    # Save the new image
    new_image.save("overlayed_image.jpg")

    return new_image
