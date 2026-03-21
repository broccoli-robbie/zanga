import os
import shutil


def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    contents = os.listdir(src)
    for entry in contents:
        src_path = os.path.join(src, entry)
        dst_path = os.path.join(dst, entry)
        if os.path.isfile(src_path):
            print(f"Copying: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            copy_directory(src_path, dst_path)
