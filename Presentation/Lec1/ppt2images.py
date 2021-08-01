from pptx_tools import utils
import os
import comtypes

def export_presentation(path_to_ppt, path_to_folder):
    if not (os.path.isfile(path_to_ppt) and os.path.isdir(path_to_folder)):
        raise "Please give valid paths!"

    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")

    # Needed for script to work, though I don't see any reason why...
    powerpoint.Visible = True

    powerpoint.Open(path_to_ppt)

    # Or some other image types
    powerpoint.ActivePresentation.Export(path_to_folder, "JPG")

    powerpoint.Presentations[1].Close()
    powerpoint.Quit()

# pptfile = r'/home/xunjie/Study/CPT_DBS/Presentation/DBS103.pptx'
# png_folder = r'./DBS103_Lec1_images'
# utils.save_pptx_as_png(png_folder, pptfile, overwrite_folder=True)

if __name__ == "__main__":
    pptfile = r'/home/xunjie/Study/CPT_DBS/Presentation/DBS103.pptx'
    png_folder = r'./DBS103_Lec1_images'
    export_presentation(pptfile, png_folder)