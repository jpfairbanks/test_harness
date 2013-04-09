from __future__ import print_function

def vprint(string, obj):
    """ verbosely prints object with a name
    :string: a name
    :obj: an object that can be converted to a str
    :returns: the printed string 

    """
    out = '{0}:\n{1}\n'.format(string, obj)
    print(out)
    return out

