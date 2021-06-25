import os
import sys
# from tqdm import tqdm
from PyPDF2 import PdfFileWriter, PdfFileReader
import re
from time import sleep
import platform
from alive_progress import alive_bar
from tabulate import tabulate
import manganelo.rewrite as manganelo

# in the manganelo lib modify line 28 in chapterdownloader.py if you want to directly get the images and not the pdf

#line 48 in chapterdownloader.py
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
    results = manganelo.search(title=title)

    if shores:
        j = 0
        print("{:<2} {:<72} {:<42} {:<11} {:<0}".format(' ', 'title', 'author(s)', 'chapter(s)', 'rating'))
        for i in results:
            #results.title, results.author, results.rating = i
            chapters = i.chapter_list()
            #print("{:<0}: {:<1} {:<2} {:<3} {:<4}".format(j, i.title, i.authors, chapters[-1].chapter, i.rating))
            print("{:<2} {:<72} {:<42} {:<11} {:<0}".format(int(j), str(i.title), str(i.authors), str(chapters[-1].chapter), str(i.rating)))
            j += 1

    return results


def folderpath():
    rootpath = replace_all(os.path.dirname(os.path.realpath(__file__)), "path")
    result.title = replace_all(str(result.title), "manga")
    mangapath = "{1}{0}downloads{0}chapters{0}{2}".format(pathos, str(rootpath), str(result.title))
    # mangapath = str(rootpath) + "\\downloads\\chapters\\" + str(result.title)
    ebookpath = "{1}{0}downloads{0}ebook{0}{2}".format(pathos, str(rootpath), str(result.title))
    # ebookpath = str(rootpath) + "\\downloads\\ebook\\" + str(result.title)
    if not os.path.isdir(mangapath):
        os.makedirs(mangapath)
    if not os.path.isdir(ebookpath):
        os.makedirs(ebookpath)

    return rootpath, mangapath, ebookpath


def replace_all(text, dic):
    if dic == "path":
        dic = {"/": pathos,
               "\\": pathos,
               "//": pathos}
    elif dic == "manga":
        dic = {" ": "_",
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
    for i, j in dic.items():
        text = text.replace(i, j)
        while text.endswith("_"):
            l = len(text)
            text = text[:l - 1]
    return text


def getimages(chapls):
    reschapls = result.chapter_list()
    if not chapls:
        i = 0
        while i < len(reschapls):
            chapls.append(i)
            i += 1

    reschapls2 = []
    total = 0
    for i in chapls:
        for x in reschapls:
            if x.chapter == int(i):
                reschapls2.append(x)
                break
        total += 1
    print("start downloading {} ...".format(result.title))
    with alive_bar(total) as bar:
        for i in reschapls2:
            cleantitle = replace_all(i.title, "manga")
            chappath = "{1}{0}{2}.pdf".format(pathos, mangapath, str(cleantitle))
            #print(chappath)
            i.download(path=chappath)
            pdfmanagerdel(chappath)
            #bar().text(cleantitle)
            bar()



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
    if platform.system() == "Windows":
        pathos = "\\"
    else:
        os.system("clear")
        pathos = "/"
    print("""
    ___    ___                              __               ____
   /  |   /  /__ ____  ___ ____ ____  ___ _/ /____  ________/ / /
  /  /|__/  / _ `/ _ \/ _ `/ _ `/ _ \/ _ `/ __/ _ \/____/ _  / / 
 /__/   /__/\_,_/_//_/\_, /\_,_/_//_/\_,_/\__/\___/     \_,_/_/  
    using manganelo  /___/  unofficial API\n
    """)
    shores = False
    graphi = False
    chapls = []
    title = ""
    requ = input("manganato-dl$ ")
    # format manganelo-dl "Manga Name" 3 6-9 12 65
    #if len(sys.argv) >= 2:
        #print(str(sys.argv) + "\n")

    for x in requ.split(" "):
        if x == "exit":
            exit(0)
        elif x.startswith("-"):
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
        elif re.search("[a-z]*[:space:]*[A-Z]*", x):
            title = "{0} {1}".format(title, x)

    results = research()
    #else:
    #    print("Please give an argument")
    #    exit(0)
    if shores:
        result = results[int(input("\nSelect a manga:\t"))]
    else:
        chapls = list(dict.fromkeys(chapls))
        result = results[0]

    rootpath, mangapath, ebookpath = folderpath()
    getimages(chapls)
