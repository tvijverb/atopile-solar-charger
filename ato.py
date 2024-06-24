from atopile import version
from atopile.components import _get_generic_from_db

def main():
    print(version())

if __name__ == '__main__':
    _get_generic_from_db("C1234")
    main()