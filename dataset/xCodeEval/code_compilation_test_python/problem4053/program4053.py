    import sys
    
    braille_chars = """
    .  .  .. .. .  .. .. .   .  . .  .  .. .. .  .. .. .   .  . .  .   . .. .. .  
       .      .  . .  .. .. .  ..    .      .  . .  .. .. .  ..    .  ..     .  . 
                                  .  .  .  .  .  .  .  .  .  .  .. ..  . .. .. .. 
    """.strip().splitlines()
    
    decode_chart = {}
    for idx in range(26):
        ch = chr(idx + ord("a"))
        if ch in "is":
            continue
        shape = [braille_chars[l][(3 * idx) : (3 * idx + 2)] for l in range(3)]
        shape = [[x == "." for x in line] for line in shape]
        rows = [sum(line) for line in shape]
        cols = [sum(shape[r][c] for r in range(3)) for c in range(2)]
        code = tuple(rows) + tuple(cols)
    #     if code in decode_chart:
    #         print(ch, decode_chart[code], code)
        decode_chart[code] = ch
    #     print(ch, code)
    
    
def solve_G(codes: List[List[int]]) -> str:
        return "".join(decode_chart[tuple(code)] for code in codes)
    
    
    input_str = sys.stdin.read().strip()
    codes = [[int(x) for x in line.split()] for line in input_str.splitlines()[1:]]
    print(solve_G(codes))