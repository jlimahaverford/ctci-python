class Question1_3:

    @staticmethod
    def tallyString(s):
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        return d

    @staticmethod
    def is_permnutation(string, other_string):
        return Question1_3.tallyString(string) == Question1_3.tallyString(other_string)


if __name__ == '__main__':
    print('1 Actual:', Question1_3.tallyString('abcab'))
    print('1 Expected:', "{'a': 2, 'b': 2, 'c': 1}")

    print('2 Actual:', Question1_3.is_permnutation('abcab', 'cabab'))
    print('2 Expected:', True)

    print('3 Actual:', Question1_3.is_permnutation('abcab', 'cacab'))
    print('3 Expected:', False)

    print('4 Actual:', Question1_3.is_permnutation('abcab', 'abcabd'))
    print('4 Expected:', False)

#  Compilation Errors
#  "@staticmethod" not "@static_method"