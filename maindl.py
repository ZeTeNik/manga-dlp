import manganelo.rewrite as manganelo
import sys
import re


def research():
    results = manganelo.search(title=x.replace("_", " "))

    for i in results:
        print("{0}: {1}; {2}")
        totresults.append(i.title)

    # print(totresults)
    return totresults


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print(sys.argv)
        totresults = []
        fichap = None

        for x in sys.argv:
            if re.search("[a-z]|[A-Z]]", x):
                totresults = research()
            elif re.search("^[0-9]*", x):
                if fichap is None:
                    fichap = x
                lachap = x

        print("manga: {0}\nfirstchap: {1}\nlachap: {2}\n".format(str(totresults), fichap, lachap))
        y = 0
        for x in totresults:
            y+=1
            print()
