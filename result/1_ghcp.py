def sort_string_by_frequency(s):
    # Count the frequency of each character
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    # Sort the characters by frequency
    sorted_chars = sorted(freq, key=freq.get, reverse=True)
    
    # Build the sorted string
    sorted_string = ''
    for c in sorted_chars:
        sorted_string += c * freq[c]
    
    return sorted_string

assert sort_string_by_frequency('hello world') == 'llloohe wrd'
assert sort_string_by_frequency('tree') == 'eetr'
assert sort_string_by_frequency('') == ''
assert sort_string_by_frequency('a') == 'a'
assert sort_string_by_frequency('ab') == 'ab'