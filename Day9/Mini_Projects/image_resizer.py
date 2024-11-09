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


def main():
    # Get the image file paths and output directory from user
    input_path = input("Enter the full path of the image to resize: ")
    output_dir = input("Enter the output directory to save the resized image: ")

    if not os.path.exists(input_path):
        print("Input file does not exist.")
        return

    if not os.path.exists(output_dir):
        print("Output directory does not exist.")
        return

    # Ask for desired image size (default is 800x800)
    size_input = input(
        "Enter the desired size (width height) or press Enter for default (800x800): "
    )
    if size_input:
        width, height = map(int, size_input.split())
        size = (width, height)
    else:
        size = (800, 800)

    # Extract the filename and create the output path
    filename = os.path.basename(input_path)
    output_path = os.path.join(output_dir, f"resized_{filename}")

    # Resize and save the image
    resize_image(input_path, output_path, size)


if __name__ == "__main__":
    main()
