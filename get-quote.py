import random
def toast():
  print("Keep it logically awesome lol.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  toast()
