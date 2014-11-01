def freq_list_from_tuple_list(tuple_list):
    """ Given a list of tuples like
        ('a', 0.5), ('b', 0.25), ('c', 0.1), ('d', 0.1), ('e', 0.05)
        Constructs a list containing 'a', 'b', 'c', 'd' and 'e' with the relative frequencies
        seen above:

        'a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','c','c','d','d','e'
    """

    _, smallest_freq = sorted(tuple_list, key=lambda x: x[1])[0] 
    tuple_freq_list = [ (x, freq / smallest_freq) for x, freq in tuple_list ]
    freq_list = [ ]
    for x , freq in tuple_list:
        scale = int(freq / smallest_freq)
        freq_list.extend( [x] * scale )
    return freq_list
