import os

basepath = "/home/potter/Downloads/"
entries = os.scandir(basepath)

for entry in entries:
    if entry.is_file():
        if entry.name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            os.rename(entry.path, basepath + "images/" + entry.name)

        if entry.name.lower().endswith(('pdf')):
            os.rename(entry.path, basepath + "pdfs/" + entry.name)

    if entry.is_dir():
        sub_entries = os.scandir(entry.path)

        for sub_entry in sub_entries:
            try:
                if sub_entry.is_dir() and sub_entry.name == ".git":
                    os.rename(entry.path, basepath + "git/" + entry.name)

                if sub_entry.name.lower().endswith(('mkv', 'mp4', 'mov', 'wmv', 'webm')):
                    os.rename(entry.path, basepath + "movies/" + entry.name)

            except FileNotFoundError:
                pass
