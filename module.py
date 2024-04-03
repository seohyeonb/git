discount_rate = 0
def set_rate(rate):
  global discount_rate
  discount_rate=rate

def get_rate():
  return discount_rate

def to_beforeprice(p):
  return p/((100-discount_rate)/100)

