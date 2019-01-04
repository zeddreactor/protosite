ascii_vocab = [chr(i) for i in range(128)]


class CaesarCypher():

    def __init__(self, alphabet=ascii_vocab):
        self.alphabet = alphabet
        print(self.alphabet)

    def get_char_posn(self, char):
        char = str(char)

        for ix, item in enumerate(self.alphabet):
            if item == char:
                return ix

    def shift_char(self, char, shift_amount=0, bkwd=True):
        max_alphabet_index = len(self.alphabet) - 1

        posn = self.get_char_posn(char)
        print("original: ", posn)
        if posn in range(len(self.alphabet)):
            if bkwd == True:
                shifted_posn = posn - shift_amount
            else:
                shifted_posn = posn + shift_amount

            if (shifted_posn) <= 0:
                shifted_posn = max_alphabet_index - (shifted_posn % max_alphabet_index)

            elif (shifted_posn) > max_alphabet_index:
                shifted_posn = (shifted_posn % max_alphabet_index) - max_alphabet_index

            print("shifted: ", shifted_posn, self.alphabet[shifted_posn])
            return self.alphabet[shifted_posn]

        else:
            print("not in dict: ", char)

    def shift_string(self, input_string, shift_amount=0, bkwd=True):
        """Use to cypher/decypher entire string."""

        new_string = [self.shift_char(item, shift_amount) for item in input_string]

        return ("".join(new_string))
