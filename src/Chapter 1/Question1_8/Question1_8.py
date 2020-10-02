class Question1_8:

    @staticmethod
    def is_rotation(s1, s2):
        assert(isinstance(s1, str))
        assert(isinstance(s2, str))
        n = len(s1)
        if n != len(s2):
            return False

        for i in range(n):
            if all(s1[i+j] == s2[0+j] for j in range(n-i)):
                return all(s1[0+j] == s2[n-i+j] for j in range(i))
        return False


if __name__ == '__main__':
    s1 = 'waterbottle'
    s2 = 'terbottlewa'
    actual = Question1_8.is_rotation(s1, s2)
    expected = True
    print('Test 1: actual={} expected={}'.format(actual, expected))

    s1 = 'waterbottle'
    s2 = 'terboxtlewa'
    actual = Question1_8.is_rotation(s1, s2)
    expected = False
    print('Test 2: actual={} expected={}'.format(actual, expected))

    s1 = 'abc'
    s2 = 'bca'
    actual = Question1_8.is_rotation(s1, s2)
    expected = True
    print('Test 3: actual={} expected={}'.format(actual, expected))

    s1 = 'abc'
    s2 = 'cba'
    actual = Question1_8.is_rotation(s1, s2)
    expected = False
    print('Test 4: actual={} expected={}'.format(actual, expected))

    s1 = 'abc'
    s2 = 'ab'
    actual = Question1_8.is_rotation(s1, s2)
    expected = False
    print('Test 5: actual={} expected={}'.format(actual, expected))
    print('Completed')