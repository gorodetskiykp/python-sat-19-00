# main.py
# __name__ - роль модуля (основно - __main__ ИЛИ библиотека)

# styles - flake8 + wemake
# pip install flake8
# pip install wemake-python-styleguide
# pip install black

import libs

TEMPS = (1, 4, 5, 3)
TEMP_KOEF = 3.15


def conv(temp):
    return temp * TEMP_KOEF


def main():
    print(libs.summ(1, 5) + conv(TEMPS[0]))  # noqa WPS421


if __name__ == "__main__":
    main()
