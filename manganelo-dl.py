import manganelo.rewrite as manganelo
import sys
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


def research():
    results = manganelo.search(title=x)
    j = 0

    if not shores:
        for i in results:
            chapters = i.chapter_list()
            print("{0}:\t{1};\t{2}\t{3}".format(j, i.title, i.authors, chapters[-1].chapter))
            j += 1
            totresults.append(i)
    else:
        for i in results:
            j += 1
            totresults.append(i)

    # print(totresults)
    return totresults, results


if __name__ == "__main__":
    shores = False
    noselman = False
    # format manganelo-dl "Manga Name" 3 6-9 12 65
    if len(sys.argv) >= 2:
        print(str(sys.argv) + "\n")
        totresults = []

        for x in sys.argv:
            if x != sys.argv[0]:
                totresults, results = research()
    else:
        print("Please give an argument")
        exit(0)
    selman = input("Select a manga")
