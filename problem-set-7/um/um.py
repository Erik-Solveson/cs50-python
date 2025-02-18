import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(s) -> int:
    pattern = r"\bum\b|\bUm\b|\bUM\b"
    matches = re.findall(pattern, s)
    if len(matches) > 0:
        return len(matches)
    else:
        return 'no "um"s found'


if __name__ == "__main__":
    main()
