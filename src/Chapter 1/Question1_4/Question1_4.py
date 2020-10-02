class Question1_4:

    @staticmethod
    def replace_spaces(l, length):
        # Assume l is list of characters, with some spaces.
        num_spaces = sum([x == " " for x in l[:length]])
        new_length = 2 * num_spaces + length

        out_pointer = new_length - 1
        in_pointer = new_length - 1

        while out_pointer > 0:
            # Find a word
            while l[in_pointer] == ' ':
                in_pointer -= 1

            # Copy the word
            while l[in_pointer] != ' ' and out_pointer > 0:
                l[out_pointer] = l[in_pointer]
                in_pointer -= 1
                out_pointer -= 1

            # Deal with the space
            if out_pointer > 0:
                l[out_pointer] = '0'
                l[out_pointer-1] = '2'
                l[out_pointer-2] = '%'
                out_pointer -= 3
                in_pointer -= 1


if __name__ == '__main__':
    s1 = 'Mr. John Smith    '
    s2 = 'Mr.%20John%20Smith'
    print('1 Input:', s1)
    l1 = list(s1)
    l2 = list(s2)
    Question1_4.replace_spaces(l1, 14)
    print('1 Output:', ''.join(l1))
    print('Success:', all([x == y for x, y in zip(l1, l2)]))