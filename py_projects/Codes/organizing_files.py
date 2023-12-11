import os
import shutil

#get the path of the folder that will organize it 
current_folder = os.path.dirname(os.path.abspath(__file__))

#get the files in the current folder
for files_name in os.listdir(current_folder):
    #organize image
    if files_name.endswith(("png", "jpg")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.move(files_name, "Images")
        print("Images is done")
    else:
        print("There are not images in this file")
    #organize Codes
    if files_name.endswith(("py", "cpp", "js", "css", "php", "html", "db")):
        if not os.path.exists("Codes"):
            os.mkdir("Codes")
        shutil.move(files_name, "Codes")
        print("Codes is done")
    else:
        print("There are not codes in this file")
    #organize Docs
    if files_name.endswith(("txt", "docx")):
        if not os.path.exists("Docs"):
            os.mkdir("Docs")
        shutil.move(files_name, "Docs")
        print("Docs is done")
    else:
        print("There are not docs in this file")
    #organize PDF
    if files_name.endswith("pdf"):
        if not os.path.exists("PDF"):
            os.mkdir("PDF")
        shutil.move(files_name, "PDF")
        print("PDF is done")
    else:
        print("There are not pdf in this file")
    #organize Excel
    if files_name.endswith("xlsx"):
        if not os.path.exists("Excel"):
            os.mkdir("Excel")
        shutil.move(files_name, "Excel")
        print("Excel is done")
    else:
        print("There are not excel in this file")
    #organize Power point
    if files_name.endswith("pptx"):
        if not os.path.exists("Power point"):
            os.mkdir("Power point")
        shutil.move(files_name, "Power point")
        print("Power point is done")
    else:
        print("There are not power point in this file")
    #organize Apps
    if files_name.endswith("exe"):
        if not os.path.exists("Apps"):
            os.mkdir("Apps")
        shutil.move(files_name, "Apps")
        print("Apps is done")
    else:
        print("There are not apps in this file")
    #organize Zip
    if files_name.endswith("zip"):
        if not os.path.exists("Zip"):
            os.mkdir("Zip")
        shutil.move(files_name, "Zip")
        print("Zip is done")
    else:
        print("There are not zip in this file")