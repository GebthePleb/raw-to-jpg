import os
import glob
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Convert Cannon Raw (CR2) to JPG')
parser.add_argument('-i', '--input', help='Input directory of cr2 files', required=True)
parser.add_argument('-o', '--output', help='Output directory of jpg files.', required=False, default="")
args = parser.parse_args()

input_dir = args.input
output_dir = args.output
def raw_to_jpg(input, output):
    """
    :param input: the input directory of cr2 images
    :param output: the output  directory of jpg images
    :return: void
    """
    if output == "":
        output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output")

        try:
            os.mkdir(output_dir)
        except OSError as e:
            pass
        os.chdir(output_dir)
        
    else:
        print(os.path.join(output))
        os.chdir(os.path.join(output))

    raw_images = []
    for file in glob.glob(os.path.join(os.path.join(input) + "\*.CR2"), recursive=True):
        raw_images.append(file)

    for image in raw_images:
        image_name = os.path.basename(image)
        print("Converting " + image_name + " to jpg.")

        cr2_image = Image.open(image)
        convert_image = cr2_image.convert('RGB')
        convert_image.save((image_name.split(".")[0] + ".jpg"), format="jpeg")


if __name__ == '__main__':
    raw_to_jpg(input_dir, output_dir)
