def read_file_first_line(filename):
    fileref = open("apache_log.txt", "r")

    # Read the first line
    first_line = fileref.readline().strip()

    # Close the file
    fileref.close()

    return first_line
