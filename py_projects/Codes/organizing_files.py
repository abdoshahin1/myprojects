import os
import shutil

#get the path of the folder that will organize it 
current_folder = os.path.dirname(os.path.abspath(__file__))

#get the files in the current folder
for files_name in os.listdir(current_folder):
    #organize image
    if files_name.endswith(("png", "jpg", "jpeg")):
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
        if not os.path.exists("PDFs"):
            os.mkdir("PDFs")
        shutil.move(files_name, "PDFs")
        print("PDFs is done")
    else:
        print("There are not pdfs in this file")
    #organize Excel
    if files_name.endswith("xlsx"):
        if not os.path.exists("Excels"):
            os.mkdir("Excels")
        shutil.move(files_name, "Excels")
        print("Excels is done")
    else:
        print("There are not excels in this file")
    #organize Power point
    if files_name.endswith("pptx"):
        if not os.path.exists("Power points"):
            os.mkdir("Power points")
        shutil.move(files_name, "Power points")
        print("Power points is done")
    else:
        print("There are not power points in this file")
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
        if not os.path.exists("Zips"):
            os.mkdir("Zips")
        shutil.move(files_name, "Zips")
        print("Zips is done")
    else:
        print("There are not zips in this file")  
    #organize mp3
    if files_name.endswith("mp3"):
        if not os.path.exists("Audios"):
            os.mkdir("Audios")
        shutil.move(files_name, "Audios")
        print("Audios is done")
    else:
        print("There are not audios in this file")
    #organize movie
    if files_name.endswith("mp4"):
        if not os.path.exists("Movies"):
            os.mkdir("Movies")
        shutil.move(files_name, "Movies")
        print("Movies is done")
    else:
        print("There are not movies in this file")
