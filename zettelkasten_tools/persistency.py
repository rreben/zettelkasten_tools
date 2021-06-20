# persistency.py
# Copyright (c) 2021 Dr. Rupert Rebentisch
# Licensed under the MIT license

import os
import logging


def rename_file(directory, oldfilename, newfilename):
    """renames a file in a directory

    :param directory: the name of the directory containing the file
                      to be renamed
    :type directory: string
    :param oldfilename: original name of the file
    :type oldfilename: string
    :param newfilename: new name of the file
    :type newfilename: string
    """
    if os.path.exists(directory):
        oldfile = directory + '/' + oldfilename
        newfile = directory + '/' + newfilename
        os.rename(oldfile, newfile)
        print('renamed: ', oldfile, ' with: ', newfile)
    else:
        logging.error(
            "rename-error: directrory "
            + directory + " not found")


def list_of_filenames_from_directory(directory):
    """returns a list of all files in a directory

    Hidden files are excluded from the list

    :param directory: name of the directory
    :type directory: string
    :return: list of the names of the files in the directory
    :rtype: list
    """
    list_of_filenames = []
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            # do not process hidden files
            if not (filename[0] == '.'):
                list_of_filenames.append(filename)
    else:
        logging.error(
            "input directrory" + " not found")
    return list_of_filenames
