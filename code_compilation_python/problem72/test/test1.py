from ..program72 import program72
def test1():
    assert program72(18
1
0 2 3
2
1 0 3
3
1 2 0
1
0 3 2
3
1 0 2
2
1 3 0
2
0 1 3
1
2 0 3
3
2 1 0
2
0 3 1
3
2 0 1
1
2 3 0
3
0 1 2
1
3 0 2
2
3 1 0
3
0 2 1
2
3 0 1
1
3 2 0) == ['\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nYES\n\nYES\n\nYES\n\nYES\n\nYES\n\nYES\n\nNO\n\nNO\n\nNO\n', '\nno\n\nno\n\nno\n\nno\n\nno\n\nno\n\nno\n\nno\n\nno\n\nyes\n\nyes\n\nyes\n\nyes\n\nyes\n\nyes\n\nno\n\nno\n\nno\n', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nyes\nyes\nyes\nyes\nyes\nyes\nNO\nNO\nNO\n', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO\n', 'No\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nYes\nYes\nYes\nYes\nYes\nYes\nNo\nNo\nNo\n', 'no\nno\nno\nno\nNO\nNO\nNO\nNO\nno\nyes\nyes\nyes\nyes\nyes\nyes\nNO\nno\nNO\n', 'No\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nYES\nYES\nYES\nYES\nYES\nYES\nNo\nNo\nNo\n', '\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO', 'no\nno\nno\nno\nno\nno\nno\nno\nno\nyes\nyes\nyes\nyes\nyes\nyes\nno\nno\nno', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nyes\nYES\nYES\nYES\nNO\nNO\nNO\n', 'NO \nNO \nNO \nNO \nNO \nNO \nNO \nNO \nNO \nYES \nYES \nYES \nYES \nYES \nYES \nNO \nNO \nNO \n', 'NO NO NO NO NO NO NO NO NO Yes YES YES YES YES YES NO NO NO ', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO\n', 'no\nno\nno\nno\nno\nno\nno\nno\nno\nyes\nyes\nyes\nyes\nyes\nyes\nno\nno\nno\n', 'NO \nNO \nNO \nNO \nNO \nNO \nNO \nNO \nNO \nYES\nYES\nYES\nYES\nYES\nYES\nNO \nNO \nNO \n', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO\n\n', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYes\nYes\nYes\nYes\nYes\nYes\nNO\nNO\nNO\n', 'No\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nYes\nYes\nYes\nYes\nYes\nYes\nNo\nNo\nNo\n', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO\n\n', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO\n', 'No\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nNo\nyes\nyes\nyes\nyes\nyes\nyes\nNo\nNo\nNo\n', 'NO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nYES\n\nYES\n\nYES\n\nYES\n\nYES\n\nYES\n\nNO\n\nNO\n\nNO\n\n', 'NO NO NO NO NO NO NO NO NO YES YES YES YES YES YES NO NO NO ', 'NO\nNO\nNO\nNo\nNO\nNO\nNO\nNO\nNo\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNo\nNO\n', 'NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES\nYES\nNO\nNO\nNO', 'NO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nNO\n\nYES\n\nYES\n\nYES\n\nYES\n\nYES\n\nYES\n\nNO\n\nNO\n\nNO\n\n', 'no\nno\nno\nno\nno\nno\nno\nno\nno\nYes\nYes\nYes\nYes\nYes\nYes\nno\nno\nno\n']