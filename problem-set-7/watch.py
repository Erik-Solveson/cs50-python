import re
import sys


def main():
    url = parse(input("HTML: "))
    print(rebuild_url(url))


def parse(s):
    matches = re.search(r'^(.+)src="([^"]+)+.+$' ,s)
    print(f"============== {matches.group(2)} ================")
    return matches.group(2)


def rebuild_url(url):
    url = url.split("/")
    url[0] = "https:"
    url[2] = "www.youtu.be"
    url = "/".join(url)
    return url
    

if __name__ == "__main__":
    main()
