import os
import os.path


def list_images():
    path_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
    path_files = os.listdir(path_files)
    path_files.remove("logo.png")
    path_files.remove("question.png")
    return path_files


def open_image(image):
    archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images", image)
    return archivo
