class Question1_5:

    @staticmethod
    def check_compressed_length(s):
        current_output_length = 0
        current_char = s[0]
        current_count = 1
        for x in s[1:]:
            if x == current_char:
                current_count += 1
            else:
                current_output_length += (1 + len(str(current_count)))
                current_char = x
                current_count = 1
        current_output_length += (1 + len(str(current_count)))
        return current_output_length

    @staticmethod
    def compress_string(s):
        output_string_list = []
        current_char = s[0]
        current_count = 1
        for x in s[1:]:
            if x == current_char:
                current_count += 1
            else:
                output_string_list.append(current_char)
                output_string_list.append(str(current_count))
                current_char = x
                current_count = 1
        output_string_list.append(current_char)
        output_string_list.append(str(current_count))
        return ''.join(output_string_list)

    @staticmethod
    def conditionally_compress_string(s):
        if Question1_5.check_compressed_length(s) < len(s):
            return Question1_5.compress_string(s)
        else:
            return s


if __name__ == '__main__':
    s = 'aaaabbbbbbbbbbbccc'
    actual = Question1_5.check_compressed_length(s)
    expected = 7
    print('Test 1: actual={}, expected={}'.format(actual, expected))

    s = 'aaaabbbbbbbbbbbccc'
    actual = Question1_5.compress_string(s)
    expected = 'a4b11c3'
    print('Test 2: actual={}, expected={}'.format(actual, expected))

    s = 'aaaabbbbbbbbbbbccc'
    actual = Question1_5.conditionally_compress_string(s)
    expected = 'a4b11c3'
    print('Test 3: actual={}, expected={}'.format(actual, expected))

    s = 'a'
    actual = Question1_5.conditionally_compress_string(s)
    expected = 'a'
    print('Test 4: actual={}, expected={}'.format(actual, expected))