def read_book(titile_path):
    """
    Read a book and return it as a  string.
    """
    with open(titile_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text 

    text = read_book(".\Books\English\shakespeare\Romeo and Juliet.txt")
    print(text)