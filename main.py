from src.join_pdf import join_pdf
from src.utils import list_files
from src.config import PATH, OUTPUT

def main(path, output):
    files = list_files(path)
    print(files)
    join_pdf(files, output)


if __name__ == '__main__':
    main(PATH, OUTPUT)