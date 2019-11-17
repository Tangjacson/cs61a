
passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '147be620a603b33dc0450faa16b2fdda236cb7a9516770446de541a2'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()