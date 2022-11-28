# iMakeBootim
Python program to create correctly scaled iBoot images from a picture

# Installing Dependencies
- You will need the latest version of python3
- You will need pip/pip3
- You will need an Intel Mac (M1 macs DO NOT work), and ONLY A MAC!
- macOS 10.15 Catalina or higher is recommended

- After you have installed python3 and pip/pip3, open a terminal window and cd into the downloaded directory. Then run: `pip3 install -r requirements.txt`.
- If your command is pip instead of pip3: `pip install -r requirements.txt`

# Notes
- This only works for 64 bit checkm8 compatible devices! Img3 creation is NOT supported!
- Extremely tall pictures will most likely not work, so find one that is reasonable. If the program outputs no errors but your picture doesn't work, it was probably too tall.

# Usage

|       Option       |              What does this do?                  |
|--------------------|--------------------------------------------------|
|   -p or --picture  |                Input picture                     |
| -id or --identifier|          Identifier of your device               |
|   -t or --blob     | Your blob if you want to sign your outputted file|
|    --padding       |    Specify padding in pixels for the width.      |

## Example 1: 
- `python3 iMakeBootim.py -p picture.png -id iPhone8,4`
- Result: This gives us a .im4p file that was created from the resized picture that fits perfectly on the screen width wise

## Example 2: 
- `python3 iMakeBootim.py -p picture.png -id iPhone1,1`
- Result: This gives us an error because devices that aren't 64 bit and checkm8 compatible don't use .img4, therefore aren't compatible

## Example 3: 
- `python3 iMakeBootim.py -p picture.jpg -id iPhone8,4 -t blob.shsh2`
- Result: This gives us a signed .img4 file that can be uploaded straigt to the iPhone and is able to appear on screen like this: ```irecovery -c "setpicture 0x1"``` (Command through shell is just ```setpicture 0x1```)

## Example 4:
- `python3 iMakeBootim.py -p picture.png -id iPhone8,4 -t blob.shsh2 --padding 150`
- Result: This gives us a signed and correctly scaled img4 file that puts 150 pixels of space between each side of the device's screen and your picture

# Issues
**iBootim or img4tool cannot be opened**

![Issue iBootim](https://github.com/XboxOneSogie720/iMakeBootim/blob/main/Other/Error_ibootim.png)
![Issue img4tool](https://github.com/XboxOneSogie720/iMakeBootim/blob/main/Other/Error_img4tool.png)

**If you see either of these errors, take these steps to solve the problem:**
- Open your iMakeBootim folder, and head to the `Resources/Darwin` folder
- While holding **Command (Windows key if you're keyboard isn't made by Apple)**, click on both binaries you see.
- Once they're both highlighted, right click on both of them and hit **Open**
- In the security popup window, hit **Open** again
- Now iMakeBootim will work

