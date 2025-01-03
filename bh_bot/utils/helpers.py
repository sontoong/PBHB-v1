# pylint: disable=C0114,C0116,C0301
import os
import sys


def path_prefix(image_list, prefix):
    """
    Adds a prefix to each image path in the given image list.

    :param image_list: List of tuples where the first element is the image path and the other elements are offsets or additional parameters.
    :param prefix: The prefix to add to each image path.
    :return: A new list with the prefixed image paths.
    """
    return [(prefix + path, *params) for path, *params in image_list]


def extract_file_name(image_path):
    image_name = image_path.split(
        '/')[-1] if '/' in image_path else image_path.split('\\')[-1]
    image_name = image_name.replace('_', ' ').rsplit('.', 1)[0]
    return image_name


def resource_path(resource_folder_path, resource_name):
    """ Get the absolute path to the resource, works for dev and for both PyInstaller --onefile and --onedir """
    try:
        # PyInstaller creates a temp folder (_MEIPASS) in --onefile mode
        base_path = sys._MEIPASS  # pylint: disable=protected-access,no-member
        print(f"PATH INFO: {os.path.join(
            base_path, resource_folder_path, resource_name)}")
    except AttributeError:
        # In --onedir mode or development, base_path will be the directory where the script is located
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(f"PATH INFO: {os.path.join(
            base_path, resource_folder_path, resource_name)}")

    return os.path.join(base_path, resource_folder_path, resource_name)
