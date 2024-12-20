import sys
sys.path.append('../')
from program_153 import Strongest_Extension
def test_1():
    assert Strongest_Extension('Watashi', ['tEN', 'niNE', 'eIGHt8OKe']) == 'Watashi.eIGHt8OKe'
def test_2():
    assert Strongest_Extension('Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']) == 'Boku123.YEs.WeCaNe'
def test_3():
    assert Strongest_Extension('__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']) == '__YESIMHERE.NuLl__'
def test_4():
    assert Strongest_Extension('K', ['Ta', 'TAR', 't234An', 'cosSo']) == 'K.TAR'
def test_5():
    assert Strongest_Extension('__HAHA', ['Tab', '123', '781345', '-_-']) == '__HAHA.123'
def test_6():
    assert Strongest_Extension('YameRore', ['HhAas', 'okIWILL123', 'WorkOut', 'Fails', '-_-']) == 'YameRore.okIWILL123'
def test_7():
    assert Strongest_Extension('finNNalLLly', ['Die', 'NowW', 'Wow', 'WoW']) == 'finNNalLLly.WoW'
def test_8():
    assert Strongest_Extension('_', ['Bb', '91245']) == '_.Bb'
def test_9():
    assert Strongest_Extension('Sp', ['671235', 'Bb']) == 'Sp.671235'