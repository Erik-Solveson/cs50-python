from PIL import Image
import sys

def main():
    in_file, out_file = read_in_from_command_line()
    overlay_image(in_file, out_file)

# error handling to check if:
def read_in_from_command_line():
    ACCEPTED_FILE_TYPES = ("jpeg", "jpg", "png")
    #Check if the correct number of command line arguments
    if len(sys.argv) != 3:
        print(len (sys.argv))
        print('incorrect number of command line arguments')
        sys.exit()
    #Check if the file type is a image format
    elif not sys.argv[1].endswith(ACCEPTED_FILE_TYPES):
        print('files suppled are not of an approved file type')
        sys.exit()
    #Check if the file endings match
    elif sys.argv[1][-1:-4:-1] != sys.argv[2][-1:-4:-1]:
        print('two different files types were supplied')
        sys.exit()
    else:
        return sys.argv[1], sys.argv[2]

def overlay_image(file_1, file_2):
    try:
        with Image.open(file_1) as img1:
            with Image.open(file_2) as img2:
                img1.paste(img2)
                img1.save("newimage.png")

    except FileNotFoundError:
        print('File not found')
        sys.exit()

if __name__ == "__main__":
    main()