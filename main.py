# A python steganography tool for images.
# A fun exercise!
from pyfiglet import print_figlet
from PIL import Image
import stepic


# user_choice() function pulled from Python-Port-Scanner project on my Github.
# Modified for the python steganography tool.
# Runs chosen function based upon user input.
# If the user inputs an incorrect file path, it is caught and the user is informed.
def user_choice():
    while True:
        try:
            choice = input("\nDo you want to encode,decode, or view an image? If not, type 'exit' to exit the tool. \n "
                           "Enter input:")
            # encode choice requires a full file path to the user's chosen file, including the file type.
            # Example: C:\Users\*Name Here*\Desktop\image.jpg
            if choice == 'encode':
                user_file = input("Please provide the file path to the image you wish to encode: ")
                # If the user inputs an incorrect file path, the following line will throw an IOError.
                user_image = Image.open(user_file)
                encode_image(user_image)
            # decode choice requires a full file path to the user's chosen file, including the file type.
            # Example: C:\Users\*Name Here*\Desktop\image.jpg
            # Effectively the same as the encode counterpart.
            elif choice == 'decode':
                user_file = input("Please provide the file path to the image you wish to decode: ")
                # If the user inputs an incorrect file path, the following line will throw an IOError.
                user_image = Image.open(user_file)
                decode_image(user_image)
            # exit option for the user in the event they wish to terminate the program at this point.
            elif choice == 'view':
                user_file = input("Please provide the file path to the image you wish to view: ")
                user_image = Image.open(user_file)
                view_image(user_image)
            elif choice == 'exit':
                print("Exiting \n")
                break
            # Catches invalid options. Anything that is not 'encode' or 'decode' or 'view' is invalid.
            else:
                print("Not a valid option.")
                print("Restarting! \n")
                continue
        # Catches an error thrown by inputting an incorrect file path.
        except IOError as e:
            print('Your file path was incorrect. Please enter a valid file path.')
            print('Restarting! \n')
            continue
        else:
            break


# encode_image(user_image) function that encodes the user's chosen message into their chosen image.
def encode_image(user_image):
    while True:
        try:
            message = input("Enter message to encode: ")
            # Coverts user's message into bytes, so it is usable by stepic.encode.
            bytes_message = message.encode('utf-8')
            # Encodes the user's chosen image with their chosen message.
            encoded_image = stepic.encode(user_image, bytes_message)
            # Allows for user to set new file name.
            file_name = input("Enter a name for the file: ")
            # The encoded file is saved as a PNG with the user's chosen file name.
            encoded_image.save(file_name, 'PNG')
            break

        # General exception catch to ensure that no error is missed.
        # At time of creation, there are no known exceptions for this section, this is just a precaution.
        except Exception as e:
            print(e)
            print("Restarting! \n")
            continue

    # Prints success message.
    print("Image encoded and saved as PNG.")
    # Returns user to the user_choice() function
    user_choice()


# decode_image(user_image) decodes a user's chosen image.
def decode_image(user_image):
    # Decodes user's chosen image and prints result.
    message = stepic.decode(user_image)
    print(message)
    # Returns user to the user_choice() function.
    user_choice()


# view_image(user_image) displays a user's chosen image.
def view_image(user_image):
    # Displays the user's chosen image.
    user_image.show()
    # Returns user to the user_choice() function.
    user_choice()


# Establishes a basic welcome screen and calls user choice function.
# Welcome screen is the same as the one used in both Python-Port-Scanner and Python-Packet-Sniffer
if __name__ == '__main__':
    colors = "95;197;220:"
    print_figlet("Python Steganography", font='slant', colors=colors)
    print("Welcome to a Python Steganography Tool")

    user_choice()