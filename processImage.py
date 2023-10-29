from Utilities.Resize import resize
from Utilities.Overlay import overlay

def ProcessImage(imagePath, isMen):

    resized_image = resize(imagePath)
    if isMen:
        overlayed_image_man = overlay(resized_image, True)
        return overlayed_image_man
    else:
        overlayed_image_woman = overlay(resized_image, False)
        return overlayed_image_woman

def main():
    return ProcessImage("/Users/afshanahmed/overlay/artwork.jpeg", False)

main()