T=0.5

h=[100,200]

v=[0,0]

a=[0,0]

f=[100,135]

G=10

thrusters = [0,0]

print "h0:",h[0], "v0:",v[0], "f0:",f[0]

print "h1:",h[1], "v1:",v[1], "f1:",f[1]



while h[0]>=0 or h[1]>=0 :

    for i in range(0,2) :

        if h[i] >= 0:

            thrusters[i] = int(raw_input("set thrusters(0-20): "))

            if thrusters[i] > 20:

                thrusters[i] = min(thrusters[i], 20)

                print "thrusters at max(20)"

            if thrusters[i] < 0:

                thrusters[i] = max(thrusters[i], 0)

                print "thrusters at min(0)"

            if thrusters[i] > f[i]:

                thrusters[i] = f[i]

                print"Rocket1 is Out of fuel! Thrusters at %d" % (thrusters[i])

        else:

            print("No fuel -- rocket is in free-fall!")

            thrusters[i] = 0



    for i in range(0, 2):

        f[i] = f[i] - thrusters[i] * T

        a[i] = -G + thrusters[i]

        h[i] = h[i] + v[i] * T + 0.5 * a[i] * T ** 2

        v[i] = v[i] + a[i] * T

        if h[i] < 0:

            h[i] = 0

        print "h%d: %d v%d: %3d f%d: %3d" % (i,h[i],i, v[i],i, f[i])



for i in range(0, 2):

        if v[i] < -3:

            print "Rocket%d crashed! Velocity was"%(i),v[i]

        else:

            print "rocket%d landed successful"%(i)
