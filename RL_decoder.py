def decode(mess):
    """Run length decoding - convert string from '2k3b' to 'kkbbb'"""
    res = []
    num = ''
    for char in mess:
        # IF character is an integer, add it to current num
        if char.isdigit():
            num += char
        else:
            # 'a'* int('3') = 'aaa' expand on this
            # after expanding num is set to empty
            res.append(char*int(num))
            num = ''
    return ''.join(res)
