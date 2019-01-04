from ff.nltktests.fuckifier import TheFuckifier
from util.caesarcypher import CaesarCypher

def setup_all():
    print("Setting up all modules")
    setup_caesar()
    setup_ff()

def setup_caesar():
    c = CaesarCypher()
    print(
    c.get_char_posn('A'),
    c.get_char_posn(5),

    c.shift_char('A', 3),
    "Shifting string...",
    c.shift_string('A5B', 3)

    )

def setup_ff():

    f = TheFuckifier()
    test_sentence = "have a good day!"

    print("Testing the fuckifier-----")
    print(f.fuckify_string(test_sentence))


    # fparser=fingStringParser("have a good day!")
    # fparser.fuckify(fparser.getfindices())
    # print(fparser.getFuckifiedString())
    # print("Doing fuckifier stuff-------")
