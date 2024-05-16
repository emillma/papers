import sympy as sp
from sympy.printing import latex

sin, cos, tan = sp.sin, sp.cos, sp.tan
I, p, chi, psi = sp.symbols("I,p,\chi,\psi")


a, b = sp.symbols("a,b")


def f(d):
    return (a * cos(d)) ** 2 + (b * sin(d)) ** 2


x = sp.symbols("x")
d0 = x
d45 = d0 - sp.pi / 4
d90 = d45 - sp.pi / 4
d135 = d90 - sp.pi / 4

i0 = f(d0)
i45 = f(d45)
i90 = f(d90)
i135 = f(d135)


i = (a * cos(x) - b * sin(x)) ** 2
j = (a * sin(x) + b * cos(x)) ** 2

s1 = (i0 - i90).trigsimp().simplify()
s2 = (i45 - i135).trigsimp().simplify()

(i0 + i90).simplify()
s0 = (i0 + i90).trigsimp().simplify()
s1 = (i0 - i90).trigsimp().simplify()
s2 = (i45 - i135).trigsimp().simplify()
aolp = (sp.atan(s2 / s1) / 2).simplify()
print(aolp)
aolp = sp.atan2(s2, s1) / 2


pt: sp.Matrix = rot * scale * circ

a, b, c, d = sp.symbols("a,b,c,d")
xt = pt[0]
yt = pt[1]
sp.solve((xt**2).diff(t).simplify())

sp.solve(pt.diff(t)[0], t)[0].simplify()
