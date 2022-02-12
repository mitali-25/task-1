# Problem Set 4A


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1:
        return sequence
    perm = get_permutations(sequence[1:])
    list = []
    first_element = sequence[0]
    for letters in perm:
        for i in range(0, len(letters) + 1):
            all = letters[:i] + first_element + letters[i:]
            list.append(all)
    return list


list2 = []
for elements in get_permutations('book'):
    if elements not in list2:
        list2.append(elements)
print(list2)




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    def test_get_permutations(sequence):
        """
           Unit test for get_permutations
           """
        failure = False
        words = {("it"): ['it', 'ti'] , ("car"): ['rac', 'arc', 'acr', 'rca', 'cra', 'car'],
                 ("book"): ['koob', 'okob', 'ookb', 'oobk', 'kobo', 'okbo', 'obko', 'obok', 'kboo', 'bkoo', 'boko', 'book']}

        for (word) in words.keys():
            permutations = get_permutations(sequence)
            if permutations != words[(word)]:
                print("FAILURE: test_get_permutations()")
                print("Output:" + get_permutations((word)))
                print("Expected", words[(word)],)
                failure = True
        if not failure:
            print("SUCCESS: test_get_permutations()")
