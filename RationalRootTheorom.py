class rationality_theorom:
 def __init__(self, p , q):
  self.q, self.p = q , p
 def factors1(self):
  l=[]
  [l.append(i) for i in range(1,abs(self.p) + 1) if abs(self.p) % i == 0]
  return l
 def factors2(self):
  l2=[]
  [l2.append(i) for i in range(1, abs(self.q) + 1) if abs(self.q) % i == 0]
  return l2
rationals = rationality_theorom(3,-1) # first element is p and second is q
a,b = (rationals.factors1()), (rationals.factors2())
final_list,l=[],[]
crude_fractions=((['{}/{}'.format(x, y) for x in a for y in b]))
[final_list.append(eval(i)) for i in crude_fractions]
p = sorted(list(set(final_list)))
[l.append(i*-1.0) for i in p]
[p.append(i) for i in l]
print([i for i in p if ((-1*i**3) + (-5*i**2) + (-1*i) + 3) == 0.0])
