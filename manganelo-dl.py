import os
import sys
# from tqdm import tqdm
import progressbar
from progressbar import ProgressBar
from PyPDF2 import PdfFileWriter, PdfFileReader
import re
import shutil
from progress.bar import Bar

import manganelo.rewrite as manganelo

# in the manganelo lib modify line 28 in chapterdownloader.py if you want to directly get the images and not the pdf
"""
	for i, url in enumerate(urls):
			# remove ads
			if url.endswith(".jpg"):
"""

"""
def rangechap():
    ranchap = x.split(x, "-")

    fichap = ranchap[0]
    lachap = ranchap[1]

    while fichap <= lachap:
        selchap.append(fichap)
        fichap += 1
"""


def research():
    results = manganelo.search(title=x)

    if shores:
        j = 0
        for i in results:
            chapters = i.chapter_list()
            print("{0}:\t{1};\t{2}\t{3}\t\t{4}".format(j, i.title, i.authors, chapters[-1].chapter, i.rating))
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
            text = text[:l - 1]
    return text


def getimages(chapls):
    print("Searching for chapters")
    reschapls = result.chapter_list()
    if not chapls:
        i = 0
        while i < len(reschapls):
            chapls.append(i)
            i += 1

    reschapls2 = []
    for i in chapls:
        reschapls2.append(reschapls[i])

    for i in reschapls2:
        d = {" ": "_",
             "  ": "_",
             "\\": "_",
             "/": "_",
             ":": "_",
             "*": "_",
             "?": "_",
             '"': "_",
             "<": "_",
             ">": "_",
             "|": "_",
             "____": "_",
             "___": "_",
             "__": "_"}
        cleantitle = replace_all(i.title, d)
        chappath = "{0}\\{1}.pdf".format(mangapath, str(cleantitle))
        print(chappath)
        i.download(path=chappath)
        # pdfmanagerdel(chappath)


def ebookcreator():
    print()


def pdfmanagerdel(source):
    infile = PdfFileReader(source, 'rb')
    output = PdfFileWriter()
    pages_to_delete = [0, int(infile.getNumPages()) - 1]  # page numbering starts from 0

    for i in range(infile.getNumPages()):
        if i not in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)

    with open(source, 'wb') as f:
        output.write(f)


def createpub():
    print()


def checkduplicates(lst):
    if len(set(lst)) == len(lst):
        print("success")
    else:
        print("duplicate found")


if __name__ == "__main__":
    print("""
    ___    ___                              __               ____
   /  |   /  /__ ____  ___ ____ ____  ___ _/ /____  ________/ / /
  /  /|__/  / _ `/ _ \/ _ `/ _ `/ _ \/ _ `/ __/ _ \/____/ _  / / 
 /__/   /__/\_,_/_//_/\_, /\_,_/_//_/\_,_/\__/\___/     \_,_/_/  
    using manganelo  /___/  unofficial API
    """)
    shores = False
    graphi = False
    chapls = []
    # format manganelo-dl "Manga Name" 3 6-9 12 65
    if len(sys.argv) >= 2:
        print(str(sys.argv) + "\n")

        for x in sys.argv:
            if x.startswith("-"):
                if x == "-r":
                    shores = True
            elif re.search("^[0-9]+.[0-9]+$", x):
                chapr = x.split("-")
                i = int(chapr[0])
                while i <= int(chapr[-1]):
                    chapls.append(i)
                    i += 1
                chapls = [int(j) for j in chapls]
                chapls.sort()
            elif re.search("^[0-9]+", x):
                chapls.append(x)
            elif x != sys.argv[0]:
                results = research()
    else:
        print("Please give an argument")
        exit(0)
    if shores:
        result = results[int(input("Select a manga:\t"))]
    else:
        chapls = list(dict.fromkeys(chapls))
        result = results[0]

    rootpath, mangapath, ebookpath = folderpath()
    getimages(chapls)
