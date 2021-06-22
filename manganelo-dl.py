import urllib
from html.parser import HTMLParser
import manganelo.rewrite as manganelo
import sys, os
import requests, shutil
from PIL import Image
from array import *
import re

"""
def rangechap():
    ranchap = x.split(x, "-")

    fichap = ranchap[0]
    lachap = ranchap[1]

    while fichap <= lachap:
        selchap.append(fichap)
        fichap += 1
"""


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


def research():
    results = manganelo.search(title=x)
    j = 0

    if not shores:
        for i in results:
            chapters = i.chapter_list()
            print("{0}:\t{1};\t{2}\t{3}\t\t{4}".format(j, i.title, i.authors, chapters[-1].chapter, i.rating))
            j += 1
    else:
        for i in results:
            j += 1

    return results


def folderpath():
    rootpath = os.path.dirname(os.path.realpath(__file__))
    mangapath = str(rootpath) + "\\chapters\\" + str(result.title)
    ebookpath = str(rootpath) + "\\ebook\\" + str(result.title)
    if not os.path.isdir(mangapath):
        os.makedirs(mangapath)
        os.makedirs(ebookpath)
    return rootpath, mangapath, ebookpath


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
        while text.endswith("_"):
            l = len(text)
            text = text[:l-1]
    return text


def getimages():
    for i in result.chapter_list():
        d = {" ": "_",
             "  ": "_",
             '"': "_",
             "!": "_",
             ":": "_",
             ".": "_",
             ",": "_",
             "____": "_",
             "___": "_",
             "__": "_"}
        cleantitle = replace_all(i.title, d)
        chappath = "{0}\\chap{1}_{2}.pdf".format(mangapath, str(i.chapter), str(cleantitle))
        print(chappath)
        i.download(path=chappath)


if __name__ == "__main__":
    shores = False
    noselman = False
    # format manganelo-dl "Manga Name" 3 6-9 12 65
    if len(sys.argv) >= 2:
        print(str(sys.argv) + "\n")

        for x in sys.argv:
            if x != sys.argv[0]:
                results = research()
    else:
        print("Please give an argument")
        exit(0)
    selman = input("Select a manga")
    result = results[int(selman)]
    rootpath, mangapath, ebookpath = folderpath()
    getimages()
