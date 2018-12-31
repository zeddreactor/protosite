from ff.nltktests.fuckifier import theFuckifier

def setup_all():
    print("Setting up all modules")
    setup_ff()

def setup_ff():

    f = theFuckifier()
    test_sentence = "have a good day!"

    print("Testing the fuckifier-----")
    print(f.fuckify_string(test_sentence))


    # fparser=fingStringParser("have a good day!")
    # fparser.fuckify(fparser.getfindices())
    # print(fparser.getFuckifiedString())
    # print("Doing fuckifier stuff-------")
