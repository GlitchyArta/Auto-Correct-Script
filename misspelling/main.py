import difflib
from multiprocessing import Process, Manager
import time
from difflib import *
import string

# Declaring variables
nn = []
vv = []
pvv = []
qq = []
pprr = []
ppee = []
ad = []
fin = []

# All functions to lead words from different file
def read_nouns_verbs(nn, vv, pvv, qq):
    with open("words", "r") as ff:
        for i in ff.readlines():
            s = i
            word = ""
            for ii in s:
                if ii == "\t" or ii == " " or ii == "\n":
                    nn.append(word)
                    word = ""
                else:
                    word += ii
        nn.append(word)
    with open("verbs", "r") as sf:
        for j in sf.readlines():
            s = j
            word = ""
            for jj in s:
                if jj == "\t" or jj == " " or jj == "\n":
                    vv.append(word)
                    word = ""
                else:
                    word += jj
        vv.append(word)
    with open("past_verbs", "r") as ssf:
        for p in ssf.readlines():
            s = p
            word = ""
            for pp in s:
                if pp == " " or pp == "\t" or pp == "\n":
                    if word != "":
                        pvv.append(word)
                        word = ""
                else:
                    word += pp
        pvv.append(word)
    with open("quantity", "r") as tf:
        for k in tf.readlines():
            qq.extend(k.splitlines())


def read_the_rest(pprr, ppee, ad):
    with open("preposition", "r") as fff:
        for l in fff.readlines():
            pprr.extend(l.splitlines())
    with open("perspective", "r") as ff4:
        for m in ff4.readlines():
            ppee.extend(m.splitlines())
    with open("adjectives", "r") as ff5:
        for m in ff5.readlines():
            s = m
            word = ""
            for add in s:
                if add == "\t" or add == " " or add == "\n":
                    ad.append(word)
                    word = ""
                else:
                    word += add
        ad.append(word)


# Checks for misspelling
def check_for_misspelling(file1, file2, file3, file4, file5, file6, file7):
    # Declaring variables
    word = ""
    correct = ""
    big = file1 + file2 + file3 + file4 + file5 + file6 + file7

    # Opens file
    with open("practice", "r") as result:
        # Goes through the written sentence in the practice file
        for lt in result.readlines():
            sen = lt
            if difflib.IS_LINE_JUNK(lt):
                correct += "Empty sentence"
            # Goes through the sentence
            for jkl in sen:
                if jkl == " " or jkl == "\n" or jkl in string.punctuation:
                    if jkl == '\'':
                        word += jkl
                        continue

                    if len(word) == 0:
                        correct += " "
                    elif jkl == "\n":
                        correct += jkl
                    elif word[0].isupper():
                        if word in difflib.get_close_matches(word, big):
                            if jkl in string.punctuation:
                                correct += word + jkl
                                word = ""
                            elif jkl not in string.punctuation:
                                correct += word + " "
                                word = ""
                        elif word not in difflib.get_close_matches(word, big):
                            if jkl in string.punctuation:
                                correct += word + jkl
                                word = ""
                            elif jkl not in string.punctuation:
                                correct += word + " "
                                word = ""
                    elif word in difflib.get_close_matches(word, big):
                        if word.endswith("ing"):
                            if word.endswith("eing"):
                                if jkl in string.punctuation:
                                    correct += f'{word[:-1]}ing' + jkl
                                elif jkl != ".":
                                    correct += f'{word[:-1]}ing '
                                continue
                            elif word[-4] != 'e':
                                if jkl in string.punctuation:
                                    correct += word + jkl
                                elif jkl not in string.punctuation:
                                    correct += word
                                word = ""
                                continue
                            if jkl in string.punctuation:
                                correct += word + jkl
                                word = ""
                            elif jkl not in string.punctuation:
                                correct += word + " "
                                word = ""
                            continue
                        if jkl in string.punctuation:
                            correct += word + jkl
                            word = ""
                        elif jkl not in string.punctuation:
                            correct += word + " "
                            word = ""
                    elif word not in difflib.get_close_matches(word, big):
                        if word.endswith('s') or word.endswith("es") and word[-2] != 's':
                            if jkl in string.punctuation:
                                correct += word + jkl
                                word = ""
                            elif jkl not in string.punctuation:
                                correct += word + " "
                                word = ""
                            continue

                        if jkl in string.punctuation:
                            correct += f'{difflib.get_close_matches(word, big)[0]}{jkl}'
                            word = ""
                        elif jkl not in string.punctuation:
                            correct += f'{difflib.get_close_matches(word, big)[0]} '
                            word = ""
                else:
                    if jkl == '\'':
                        word += jkl
                        continue
                    word += jkl

        # Works on the last word
        if word == "":
            pass
        elif word != "":
            if word in difflib.get_close_matches(word, big):
                correct += word + '.'
                word = ""
            elif word.endswith("ing"):
                if word.endswith("eing"):
                    correct += f'{word[:-1]}ing '
                else:
                    correct += word + '.'
                word = ""
            elif word not in difflib.get_close_matches(word, big):
                if len(word) == 0:
                    pass
                else:
                    if len(word) > 1 and word.endswith('s') or word.endswith("es") and word[-2] != 's':
                        correct += word + '.'
                        word = ""
                    elif word[0].isupper():
                        if word in difflib.get_close_matches(word, big):
                            correct += word + '.'
                            word = ""
                        elif word not in difflib.get_close_matches(word, big):
                            correct += word + '.'
                            word = ""
                    else:
                        if len(list(difflib.get_close_matches(word, big))) == 0:
                            pass
                        else:
                            correct += f'{difflib.get_close_matches(word, big)[0]}.'
                word = ""
        word = ""

    # Prints the final result
    print(correct)

# Starts the program
start = time.time()
if __name__ == "__main__":
    # Works with list
    with Manager() as manager:
        nnn = manager.list()
        vvv = manager.list()
        qqq = manager.list()
        pppvv = manager.list()
        pprrp = manager.list()
        ppeep = manager.list()
        add = manager.list()
        p1 = Process(target=read_nouns_verbs, args=(nnn, vvv, pppvv, qqq))
        p2 = Process(target=read_the_rest, args=(pprrp, ppeep, add))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        print("We set up the app ...")

        check_for_misspelling(list(nnn), list(vvv), list(qqq), list(pppvv), list(pprrp), list(ppeep), list(add))

    # End of the program
    end = time.time()
    elapse = end - start
    print(elapse)
