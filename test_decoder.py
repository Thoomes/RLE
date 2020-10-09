from RL_decoder import decode


def test_decoder():
    assert decode('2k3b') == 'kkbbb'
    assert decode('6u1i') == 'uuuuuui'
