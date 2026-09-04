import os

def arrange_files(files, ext, dest='images'):
    files_with_ext = [f for f in files if os.path.isfile(f) and f.lower().endswith(ext.lower())]
    print(files_with_ext)

    os.makedirs(dest, exist_ok=True)

    for i, file in enumerate(files_with_ext):
        dest_path = os.path.join(dest, f'photo-{i+1}{ext}')
        os.rename(file, dest_path)

if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files, '.jpg')