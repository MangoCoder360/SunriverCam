"""
Copyright (C) 2020 Reuben Schiopu All Rights Reserved
"""

from easygui import *
import wget
import os
def main():
    url = 'https://www.tripcheck.com/roadcams/cams/LavaButte_pid631.jpg'
    wget.download(url, 'SunriverCam.jpg')
    image = "SunriverCam.jpg"
    msg = "Highway 97 Camera Image       Choose 'Delete Image' to close the program"
    choices = ["Update Image","Delete Image","Save Image","Delete Saved Image"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Update Image":
        os.remove("SunriverCam.jpg")
        main()
    if reply == "Save Image":
        wget.download(url, 'SavedImage.jpg')
        os.remove("SunriverCam.jpg")
        main()
    if reply == "Delete Saved Image":
        os.remove("SavedImage.jpg")
        os.remove("SunriverCam.jpg")
        main()
main()
os.remove("SunriverCam.jpg")
