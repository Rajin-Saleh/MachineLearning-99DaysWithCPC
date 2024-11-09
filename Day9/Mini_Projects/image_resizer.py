# 99DaysWithCPC - Machine Learning - Day 9


from PIL import Image
import os


def resize_image(input_path, output_path, size=(800, 800)):
    """
    Resize the input image and save it to the output path with the specified size.

    :param input_path: Path to the input image
    :param output_path: Path where the resized image will be saved
    :param size: Tuple of the new image size (default is 800x800)
    """
    try:
        with Image.open(input_path) as img:
            # Resize the image
            img_resized = img.resize(size)

            # Save the resized image
            img_resized.save(output_path)
            print(f"Image successfully resized and saved at {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def resize_images_in_folder(input_folder, output_folder, size=(800, 800)):
    """
    Resize all images in a folder and save them to another folder.

    :param input_folder: Folder containing the input images
    :param output_folder: Folder where the resized images will be saved
    :param size: Tuple of the new image size (default is 800x800)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        # Only process files with image extensions
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"resized_{filename}")
            resize_image(input_path, output_path, size)


if __name__ == "__main__":
    input_folder = "Day9/Mini_Projects/"  # Set the path to your images
    output_folder = (
        "Day9/Mini_Projects/"  # Set the path where resized images will be saved
    )
    size = (800, 800)  # Specify the desired size (default is 800x800)

    resize_images_in_folder(input_folder, output_folder, size)
