#This is a python script to return the file type and content based on the
#file extension subbitted by the user.

def main():
    file_type = input("What is the name of the file? ")
    file_type = file_type.rstrip().split(".")
    match file_type[1]:
        case "txt":
            print("text/plain")
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "zip":
            print("application/zip")
        case _:
            print("file type not recognized")

main()