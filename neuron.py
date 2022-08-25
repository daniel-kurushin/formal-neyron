from data import *

def foo_s(x):
    return 1 / (1 + 2.78**(-x))

def foo_l(x):
    return x

def foo_p(x):
    if x > 0:
        return 1
    else:
        return 0

def normal_sum(X, W, b, activate):
    s = b
    for i in range(len(X)):
      s += W[i] * X[i]
    return activate(s)
    

class Neuron(object):
  a =  0.02
  b = -0.4

  def __learn(self,D):
    """
    Обучение
    """
    w = self.w[:]
    f = self.__call__
    for d in D:
      x = d[0]
      y = d[1]
      for j in range(len(x)):
        self.w[j] += self.a * (y - f(x)) * x[j]
    return self.__diff__(w, self.w)

  def __diff__(self, w1, w2):
    s = 0
    for a, b in zip(w1, w2):
      s += abs(a-b)
    return s > 0.001

  def __call__(self,X):
    return self.__call_f(X, self.w, self.b, self.__act_f)

  def __init__(self, D, a = 0.02, b = -0.04, 
                     act_f = foo_p, 
                     call_f = normal_sum):
    """
    Создание и обучение
    """
    self.w = [0]*len(D[0][0])

    self.a = a
    self.b = b
    self.c = 0
    self.__call_f = call_f
    self.__act_f  = act_f
    while self.__learn(D):
      self.c += 1
      if self.c > 10000: break

if __name__ == '__main__':
    f = Neuron(D5, act_f=foo_l)
    print ("Weights are = %s, c = %s" % ([round(_,2) for _ in f.w], f.c))
    for x, y in D5:
        print ("y' = %s, y = f(%s) = %s" % (y, x, round(f(x))))

