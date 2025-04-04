import zipfile
import pytest
import os



def test_compress_file():


    output_folder = ""
    input_folder = ""

    with zipfile.ZipFile(output_folder, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_folder):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, input_folder)
                zipf.write(file_path, rel_path), os.path.join(output_folder, input_folder)

    print(f"compressed folder{output_folder}")




