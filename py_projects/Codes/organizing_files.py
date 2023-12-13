import os
import shutil

#get the path of the folder that will organize it 
current_folder = os.path.dirname(os.path.realpath(__file__))

#get the files in the current folder
for files_name in os.listdir(current_folder):
    #organize image
    if files_name.endswith(("png", "jpg", "jpeg")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.move(files_name, "Images")
        print("Images is done")
    #organize Codes
    elif files_name.endswith(("py", "cpp", "js", "css", "php", "html", "db")):
        if not os.path.exists("Codes"):
            os.mkdir("Codes")
        shutil.move(files_name, "Codes")
        print("Codes is done")
    #organize Docs
    elif files_name.endswith(("txt", "docx")):
        if not os.path.exists("Docs"):
            os.mkdir("Docs")
        shutil.move(files_name, "Docs")
        print("Docs is done")
    #organize PDF
    elif files_name.endswith("pdf"):
        if not os.path.exists("PDFs"):
            os.mkdir("PDFs")
        shutil.move(files_name, "PDFs")
        print("PDFs is done")
    #organize Excel
    elif files_name.endswith("xlsx"):
        if not os.path.exists("Excels"):
            os.mkdir("Excels")
        shutil.move(files_name, "Excels")
        print("Excels is done")
    #organize Power point
    elif files_name.endswith(("pptx", "ppt")):
        if not os.path.exists("Power points"):
            os.mkdir("Power points")
        shutil.move(files_name, "Power points")
        print("Power points is done")
    #organize Apps
    elif files_name.endswith("exe"):
        if not os.path.exists("Apps"):
            os.mkdir("Apps")
        shutil.move(files_name, "Apps")
        print("Apps is done")
    #organize Zip
    elif files_name.endswith("zip"):
        if not os.path.exists("Zips"):
            os.mkdir("Zips")
        shutil.move(files_name, "Zips")
        print("Zips is done")
    #organize mp3
    elif files_name.endswith("mp3"):
        if not os.path.exists("Audios"):
            os.mkdir("Audios")
        shutil.move(files_name, "Audios")
        print("Audios is done")
    #organize movie
    elif files_name.endswith("mp4"):
        if not os.path.exists("Movies"):
            os.mkdir("Movies")
        shutil.move(files_name, "Movies")
        print("Movies is done")
    else:
        print("There are not files to organize them.")
print("All file in this directories is organized.")