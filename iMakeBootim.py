from PIL import Image
import argparse
import os
from colorama import Fore

def main(picture, identifier, blob, padding):

    #This dictionary holds all 
    #of the widths for all 64 bit checkm8 
    #compatible iDevices. This is 
    #used to get the correct width, 
    #and also scale the image correctly

    #The reason that it's only 64 bit checkm8 is because I couldn't get a valid img3 from a png.
    #Theoretically however, it is possible.
    #This program will most likely not get updated to support img3 creation
    Resolutions = {
        #Identifier|Width (Physical Pixels)
        "iphone6,1": 640,
        "iphone6,2": 640,
        "ipad4,1": 1536,
        "ipad4,2": 1536,
        "ipad4,3": 1536,
        "ipad4,4": 1536,
        "ipad4,5": 1536,
        "ipad4,6": 1536,
        "ipad4,7": 1536,
        "ipad4,8": 1536,
        "ipad4,9": 1536,
        "iphone7,1": 1080,
        "iphone7,2": 750,
        "ipad5,1": 1536,
        "ipad5,2": 1536,
        "ipad5,3": 1536,
        "ipad5,4": 1536,
        "iphone8,1": 750,
        "iphone8,2": 1080,
        "iphone8,4": 640,
        "ipad6,3": 2048,
        "ipad6,4": 2048,
        "ipad6,7": 2048,
        "ipad6,8": 2048,
        "ipad6,11": 1536,
        "ipad6,12": 1536,
        "iphone9,1": 750,
        "iphone9,2": 1080,
        "iphone9,3": 750,
        "iphone9,4": 1080,
        "ipad7,1": 2048,
        "ipad7,2": 2048,
        "ipad7,3": 1668,
        "ipad7,4": 1668,
        "ipad7,5": 1536,
        "ipad7,6": 1536,
        "ipad7,11": 1620,
        "ipad7,12": 1620,
        "iphone10,1": 750,
        "iphone10,2": 1080,
        "iphone10,3": 1125,
        "iphone10,4": 750,
        "iphone10,5": 1080,
        "iphone10,6": 1125,
        "ipod7,1": 640,
        "ipod9,1": 640,
        #TODO: Apple Watch Series 1, 2, and 3, Apple TV 4 & 4K
    }

    #Check if the identifier exists before continuing
    if identifier.lower() in Resolutions:
        print(Fore.GREEN + "{!} Your identifier was found in the local dictionary!")
    else:
        print(Fore.RED + "\n{!} Your identifier, " + Fore.GREEN + identifier + Fore.RED + ", was not found in the local dictionary!")
        print(Fore.CYAN + "\nOpen up an issue on GitHub with your device's " + Fore.GREEN + "identifier" + Fore.RESET + ", " + Fore.GREEN + "model" + Fore.RESET + ", and " + Fore.GREEN + "resolution!")
        exit()

    #Get origional properties
    img = Image.open(picture)
    origional_width = img.size[0]
    origional_height = img.size[1]

    #Define the target width & height and resize
    target_width = Resolutions[identifier.lower()]
    if padding != None:
        print(Fore.YELLOW)
        print("{} Applying specified padding of {}".format("{!}", padding))
        print(Fore.RESET)
        target_width -= padding
    wpercent = (target_width / float(origional_width))
    hsize = int((float(origional_height) * float(wpercent)))
    resized_img = img.resize((target_width, hsize))
    if not os.path.exists("work"):
        os.system("mkdir work")
    resized_img.save("work/{}_bootlogo.png".format(identifier))

    #Convert the resized image into an ibootim and into an img4 if the user specefied signing with a blob
    outputted_img = ""

    print(Fore.YELLOW + "{!} Running chmod just in case" + Fore.RESET)
    os.system("chmod +x Resources/Darwin/ibootim && chmod +x Resources/Darwin/img4tool")
    print(Fore.YELLOW + "{!} Converting PNG to iBoot Image" + Fore.RESET)
    os.system("Resources/Darwin/ibootim work/{}_bootlogo.png work/bootlogo.ibootim".format(identifier))
    print(Fore.YELLOW + "{!} Converting iBoot Image to IM4P" + Fore.RESET)
    os.system("Resources/Darwin/img4tool -c work/bootlogo.im4p -t logo work/bootlogo.ibootim")
    outputted_img = "im4p"

    #Convert to signed img4 if the user provided a blob
    if blob != None:
        print(Fore.YELLOW + "{!} Signing and converting to IMG4" + Fore.RESET)
        os.system("Resources/Darwin/img4tool -c work/bootlogo.img4 -p work/bootlogo.im4p -s {}".format(blob))
        outputted_img = "img4"
    #Move the new im4p/img4 to the Done folder
    print(Fore.YELLOW + "{!} Moving your result" + Fore.RESET)
    if not os.path.exists("Done".format(identifier)):
        os.system("mkdir Done")
        os.system("mkdir Done/{}".format(identifier))
    elif not os.path.exists("Done/{}".format(identifier)):
        os.system("mkdir Done/{}".format(identifier))
    os.system("mv work/bootlogo.{} Done/{}/bootlogo.{}".format( outputted_img, identifier, outputted_img))

    print(Fore.YELLOW + "{!} Cleaning" + Fore.RESET)
    os.system("rm -rf work")
    print(Fore.YELLOW + "{!} Done!" + Fore.RESET)
    print(Fore.GREEN + "\nYou can find your bootlogo at " + Fore.RED + "Done/{}/bootlogo.{}".format(identifier, outputted_img) + Fore.RESET + "!")
    print(Fore.RESET + "\nThanks for using iMakeBootim!")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python program to create correctly scaled iBoot images from a picture")
    parser.add_argument("-p", "--picture", type=str, help="input picture", required=True)
    parser.add_argument("-id", "--identifier", type=str, help="Identifier of your iDevice", required=True)
    parser.add_argument("-t", "--blob", help="Blob if you want to sign and convert your image to an img4", required=False)
    parser.add_argument("--padding", type=int,help="Specify a padding horizontally for your image (default padding is 100 pixels)", required=False)
    args = parser.parse_args()

    print(args)


    print("iMakeBootim by XboxOneSogie720\n")
    print(Fore.MAGENTA + "For the best outcome, make the background of your picture black.\n" + Fore.MAGENTA + "\nIf your image doesn't work but this program didn't output any errors, your picture was too tall!")
    input(Fore.BLUE + "Press ENTER/RETURN to continue! Otherwise, press CTRL + C: " + Fore.RESET)
    main(args.picture, args.identifier, args.blob, args.padding)
