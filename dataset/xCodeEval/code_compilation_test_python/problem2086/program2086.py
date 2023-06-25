def program2086():
    import Data.Char
    
    re :: String -> String -> Bool
    re (s:sx) (t:ts) = if s == t then re sx ts
      else re sx (t:ts)
    re [] (t:ts) = False
    re _ _ = True
    
    sw:: String -> String -> String -> Bool
    sw (s:sx) n (t:ts)  = if s == t then sw (n++sx) [] ts
      else sw sx (s:n) (t:ts)
    sw [] _ (t:ts) = False
    sw _ _ _ = True
    
    h :: String -> String -> String
    h s t
     | re s t = "automaton"
     | length t == length s && sw s [] t = "array"
     | sw s [] t = "both"
     | otherwise = "need tree"
      
    
    --main = do
    -- line <- getLine
    -- print (h line [])
    
    
    
    main = do
     line <- getLine
     --let a = (read (takeWhile (/= ' ') line) :: Int)
     --let line1 = drop 1 (dropWhile (/= ' ') line)
     --let b = (read (takeWhile (/= ' ') line1) :: Int)
     --let line2 = drop 1 (dropWhile (/= ' ') line1)
     --let c = (read (takeWhile (/= ' ') line2) :: Int)
     line2 <- getLine
     putStrLn(h line line2)
    