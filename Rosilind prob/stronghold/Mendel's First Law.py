def percentDomAllele(x,y,z):
    total = x + y + z
    zz = (z/total) * ((z-1)/(total-1))
    rh = (z/total) * (y/(total -1)) + (y/total) * (z/(total -1))
    hh = (y/total) * ((y-1)/(total-1))
    probDom = 1- (zz + hh/4 + rh/2)
    return probDom

print(percentDomAllele(18,28,20))
