from RL_encoder import encode

def test_encoder():
    assert encode('aa') == '2a'
    assert encode('wwwwwwbbbb') == '6w4b'