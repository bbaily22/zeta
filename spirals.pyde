import math

# My code is garbage because I wrote this as quickly as possible. 
class Complex():
    def __init__(self, sigma, t):
        self.re = sigma
        self.im = t
    
    #n^s = s.exp(n)
    def expo(self, n):
        rad = math.pow(n, self.re)
        c = Complex(rad * math.cos(self.im * math.log(n)), rad * math.sin(self.im * math.log(n)))
        return c
    
    def add(self, s):
        return Complex(self.re + s.re, self.im + s.im)
    
    def zeta(self, n):
        s = Complex(0-self.re, 0-self.im)
        L = [Complex(0,0)]
        for i in range(1, n):
            L.append(L[i-1].add(s.expo(i)))
        return L
     
C = 0
s = None
L = None
st = ""
i = 1

#color is a reserved word, so I'm breaking out the UK spelling
def colour(x):
    parity = (x//150)%2
    return 105 + ((150*parity) + ((-1)**parity)*(x%150))

def setup():
    size(1440, 900)
    background(0)
    strokeWeight(3)
    stroke(255)
    line(width/2, 0, width/2, height)
    line(0, height/2, width, height/2)
    strokeWeight(1)
    text("Input of the form \"a,b,n\" with a, b floats, n int, will calculate out to n terms for a + bi.", 25, 25)
    text("Recommended starting input: \"0.5,10000,10000\". Start typing to input, hit \"e\" to enter", 25, 50)

def draw():
    global L, s, i, st
    if not L:
        text(st, 25, 75)
    elif i<C:
        r = colour(i)
        g = colour(3*i)
        b = colour(5*i)
        stroke(r,g,b)
        line(width/2 + (width/6 * L[i-1].re), height/2 + (width/6 * L[i-1].im), width/2 + (width/6 * L[i].re), height/2 + (width/6 * L[i].im))
        i+=1

def keyPressed():
    global L, s, st, C
    if key == "e" or key == "E":
        vals = st.split(",")
        s = Complex(float(vals[0]), float(vals[1]))
        C = int(vals[2])
        L = s.zeta(C)
    # this felt better than [str(x) for x in range(10)] + [".","."]
    elif key in ["0","1","2","3","4","5","6","7","8","9",".", ","]:
                st += key
