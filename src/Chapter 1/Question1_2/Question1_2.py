class Question1_2:

    @staticmethod
    def reverse_string(s):
        assert(isinstance(s, str))
        return ''.join([x for x in s[::-1]])


print('1 Actual:', Question1_2.reverse_string('abc'))
print('1 Expected:', 'cba')

print('2 Actual:', Question1_2.reverse_string(''))
print('2 Expected:', '')

print('3 Actual:', Question1_2.reverse_string('aaa'))
print('3 Expected:', 'aaa')

print('4 Actual:', Question1_2.reverse_string('123'))
print('4 Expected:', '321')

try:
    Question1_2.reverse_string(123)
except AssertionError:
    print('Caught expected exception')
