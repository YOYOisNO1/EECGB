from program906 import driver
def test0():
  assert driver("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/", [["2016", "09", "02"]]) == "FAILED"

def test1():
  assert driver("https://www.indiatoday.in/movies/celebrities/story/wp/2020/11/03/odeof-sushant-singh-rajput-s-death-his-brother-in-law-shares-advice-for-fans-1749646/", [["2020", "11", "03"]]) == "FAILED"

def test2():
  assert driver("https://economictimes.indiatimes.com/news/economy/2020/12/29/finance/pension-assets-under-pfrda-touch-rs-5-32-lakh-crore/articleshow/79736619.cms", [["2020", "12", "29"]]) == "FAILED"

