from copystatic import copy_directory
from gencontent import generate_page


def main():
    copy_directory("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
