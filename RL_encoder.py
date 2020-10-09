def encode(mess):
    """ Run length encoding - convert string from 'wwwwwwbbbb' til '6w4b'"""

    res = []
    old_val = mess[0]
    count = 0
    for char in mess:
        if char == old_val:
            count += 1
        else:
            res.append('%d%c' % (count, old_val))
            old_val = char
            count = 1
    res.append('%d%c' % (count, char))
    return ''.join(res)  # listen bliver returneret med .join() funktion = 6w4b og IKKE 6w 4b
