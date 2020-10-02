class Question1_1:

    @staticmethod
    def has_unique_chars(x):
        assert isinstance(x, str)
        return len(x) == len(set(x))

    @staticmethod
    def has_unique_chars_no_data_structures(x):
        assert isinstance(x, str)
        return not any(a == b for i, a in enumerate(x) for b in x[i+1::])


print('1 Actual:', Question1_1.has_unique_chars('abc'))
print('1 Expected:', True)

print('2 Actual:', Question1_1.has_unique_chars('abc1'))
print('2 Expected:', True)

print('3 Actual:', Question1_1.has_unique_chars('abca'))
print('3 Expected:', False)

print('4 Actual:', Question1_1.has_unique_chars(''))
print('4 Expected:', True)


print('5 Actual:', Question1_1.has_unique_chars_no_data_structures('abc'))
print('5 Expected:', True)

print('6 Actual:', Question1_1.has_unique_chars_no_data_structures('abc1'))
print('6 Expected:', True)

print('7 Actual:', Question1_1.has_unique_chars_no_data_structures('abca'))
print('7 Expected:', False)

print('8 Actual:', Question1_1.has_unique_chars_no_data_structures(''))
print('8 Expected:', True)

try:
    Question1_1.has_unique_chars(123)
except AssertionError:
    print('AssertionError expected and found.')