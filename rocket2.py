def cal_roc(h,g,f,a,v):
    a = -g + f
    h = h + v + a * 0.5
    v = v + a
h=100
v=0
f=100
g=10
print "h:",h, "v:",v, "f:",f
while h>=0 :
    print "Set thrusters:"
    thrusters = int(raw_input())
    if f<thrusters :
        print "out of fuel! Thrusters at ",f
        cal_roc(h, g, f, a, v)
        f=0

        print "h:", h, "v:", v, "f:", f
    if f == 0:
        while h > 0:
            print "No fuel --rocket is in free-fall!"
            cal_roc(h, g, f, a, v)
            f = 0
            if h>=0 :
                print "h:", h, "v:", v, "f:", f
            elif h<0 :
                print "h:", 0, "v:", v, "f:", 0
                h=0
    if h==0 :
        if v>=3 and v<=-3 :
            print "landing Success"
        else:
            print "you crushed, Velocity was ",v
        break

    if thrusters<=20 and thrusters>=0 :
        f = f - thrusters
        cal_roc(h, g, f, a, v)
        print "h:",h, "v:",v, "f:",f
    elif thrusters > 20 :
        f=f-20
        a=-g+20
        h = h + v + a * 0.5
        v = v + a
        print "thruster should be less than 20"
        print "h:", h, "v:", v, "f:", f

    elif thrusters< 0 :
        f=f
        a=-g
        h = h + v + a * 0.5
        v = v + a
        print "thruster should be more than 0"
        print "h:", h, "v:", v, "f:", f
if h<0 :
    print "rocket is crushed"

