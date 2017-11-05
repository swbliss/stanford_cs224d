class Test():
  var1 = 1

  def fun1(self):
    self.var2 = 2

  def fun2(self):
    return self.var2 + 1

  def __init__(self):
    self.fun1()

if __name__ == "__main__":
  t = Test()
  print(t.var2)