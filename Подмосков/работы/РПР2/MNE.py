numbers = [-1.33,-1.8,-1.67,-3.44,-2.46,-1.76,-1.22,0.92,1.83,-3.68,-0.92,-2.39,
-0.86,-3.20,-0.53,-3.96,-3.3,-0.94,0.93,-1.18,-3.2,-0.62,-0.53,-3.96,
-0.28,-3.26,-1.46,-0.64,-1.04,-5.49,-0.03,-3.88,-4.46,-1.66,0.18,-0.72,
-1.31,-3.74,0.21,0.06,-0.64,-3.99,-0.09,-0.55,-3.85,2.48,0.34,-0.18,
-0.83,-1.45,-0.56,-2.58,-1.3,-2.28,-4.43,-5.3,-3.56,-2.42,-2.58,-3.75,
-1.42,0.23,-4.59,-5.92,-3.16,-0.98,-0.36,-1.99,0.73,1.23,-1.84,-4.22,1.5,1.63,-5.1,0.51,
-1.29,-2.43,-3.58,-0.5,0.18,-3.4,0.48,1.59,-2.56,-0.6,-3.92,-4.52,
-4.07,-2.13,-6.2,-0.94,-1.93,-2.1,-2.66,0.52,-2.53,-5.28,-0.28,-1.68]

R = (max(numbers)-min(numbers))/10

gr1 = min(numbers)
gr2 = gr1 + R
gr3 = gr1 + 2*R
gr4 = gr1 + 3*R
gr5 = gr1 + 4*R
gr6 = gr1 + 5*R
gr7 = gr1 + 6*R
gr8 = gr1 + 7*R
gr9 = gr1 + 8*R
gr10 = gr1 + 9*R
gr11 = max(numbers)
count1, count2, count3, count4, count5, count6, count7, count8, count9, count10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

print('Хмакс=',max(numbers),'\nХмин=',min(numbers),'\nR=',(max(numbers)-min(numbers)))
print('Середина интервала\n',
      (gr1+gr2)/2,
(gr2+gr3)/2,
(gr3+gr4)/2,
(gr4+gr5)/2,
(gr5+gr6)/2,
(gr6+gr7)/2,
(gr7+gr8)/2,
(gr8+gr9)/2,
(gr9+gr10)/2,
(gr10+gr11)/2)

for number in numbers:
    if number >= gr1 and number <= gr2:
        count1 += 1

print(f"В 1 интервале : {count1}")

for number in numbers:
    if number > gr2 and number <= gr3:
        count2 += 1

print(f"В 2 интервале : {count2}")

for number in numbers:
    if number > gr3 and number <= gr4:
        count3 += 1

print(f"В 3 интервале : {count3}")

for number in numbers:
    if number > gr4 and number <= gr5:
        count4 += 1

print(f"В 4 интервале : {count4}")

for number in numbers:
    if number > gr5 and number <= gr6:
        count5 += 1

print(f"В 5 интервале : {count5}")

for number in numbers:
    if number > gr6 and number <= gr7:
        count6 += 1

print(f"В 6 интервале : {count6}")

for number in numbers:
    if number > gr7 and number <= gr8:
        count7 += 1

print(f"В 7 интервале : {count7}")

for number in numbers:
    if number > gr8 and number <= gr9:
        count8 += 1

print(f"В 8 интервале : {count8}")

for number in numbers:
    if number > gr9 and number <= gr10:
        count9 += 1

print(f"В 9 интервале : {count9}")

for number in numbers:
    if number > gr10 and number <= gr11:
        count10 += 1

print(f"В 10 интервале : {count10}")

count = [count1,count2,count3,count4,count5,count6,count7,count8,count9,count10]

print('Проверка',sum([count1,count2,count3,count4,count5,count6,count7,count8,count9,count10]))
def p(x):
    return x/100
#print("p1={}\np2={}\np3={}\np4={}\np5={}\np6={}\np7={}\np8={}\np9={}\np10={}\n".format(p(count1), p(count2), p(count3), p(count4), p(count5), p(count6), p(count7), p(count8), p(count9), p(count10)))
#Альтернатива нижней строки
for i, count in enumerate(count, start=1):
    print(f"p{i}={p(count)}")

print('\nh1=',round(count1/100/(gr2-gr1),4),
'\nh2=',round(count2/100/(gr3-gr2),4),
'\nh3=',round(count3/100/(gr4-gr3),4),
'\nh4=',round(count4/100/(gr5-gr4),4),
'\nh5=',round(count5/100/(gr6-gr5),4),
'\nh6=',round(count6/100/(gr7-gr6),4),
'\nh7=',round(count7/100/(gr8-gr7),4),
'\nh8=',round(count8/100/(gr9-gr8),4),
'\nh9=',round(count9/100/(gr10-gr9),4),
'\nh10=',round(count10/100/(gr11-gr10),4),'\n')

MO=((gr1+gr2)*count1+(gr2+gr3)*count2+(gr3+gr4)*count3+(gr4+gr5)*count4+(gr5+gr6)*count5+(gr6+gr7)*count6+(gr7+gr8)*count7+(gr8+gr9)*count8+(gr9+gr10)*count9+(gr11+gr10)*count10)/200
print('MO=',MO)

Dispersia = (((gr1+gr2)/2-MO)**2*count1+((gr2+gr3)/2-MO)**2*count2+((gr3+gr4)/2-MO)**2*count3+((gr4+gr5)/2-MO)**2*count4+((gr5+gr6)/2-MO)**2*count5+((gr6+gr7)/2-MO)**2*count6+((gr7+gr8)/2-MO)**2*count7+((gr8+gr9)/2-MO)**2*count8+((gr9+gr10)/2-MO)**2*count9+((gr10+gr11)/2-MO)**2*count10)/100

print('Таблица 3')
print('xi*pi=',
'\n1',(gr1+gr2)*count1/200,
'\n2',(gr2+gr3)*count2/200,
'\n3',(gr3+gr4)*count3/200,
'\n4',(gr4+gr5)*count4/200,
'\n5',(gr5+gr6)*count5/200,
'\n6',(gr6+gr7)*count6/200,
'\n7',(gr7+gr8)*count7/200,
'\n8',(gr8+gr9)*count8/200,
'\n9',(gr9+gr10)*count9/200,
'\n10',(gr10+gr11)*count10/200)

print('\n(xi-MO)^2=',
'\n1',((gr1+gr2)/2-MO)**2,
'\n2',((gr2+gr3)/2-MO)**2,
'\n3',((gr3+gr4)/2-MO)**2,
'\n4',((gr4+gr5)/2-MO)**2,
'\n5',((gr5+gr6)/2-MO)**2,
'\n6',((gr6+gr7)/2-MO)**2,
'\n7',((gr7+gr8)/2-MO)**2,
'\n8',((gr8+gr9)/2-MO)**2,
'\n9',((gr9+gr10)/2-MO)**2,
'\n10',((gr10+gr11)/2-MO)**2)

print('\n(xi-MO)^2*pi=',
'\n1',((gr1+gr2)/2-MO)**2*count1/100,
'\n2',((gr2+gr3)/2-MO)**2*count2/100,
'\n3',((gr3+gr4)/2-MO)**2*count3/100,
'\n4',((gr4+gr5)/2-MO)**2*count4/100,
'\n5',((gr5+gr6)/2-MO)**2*count5/100,
'\n6',((gr6+gr7)/2-MO)**2*count6/100,
'\n7',((gr7+gr8)/2-MO)**2*count7/100,
'\n8',((gr8+gr9)/2-MO)**2*count8/100,
'\n9',((gr9+gr10)/2-MO)**2*count9/100,
'\n10',((gr10+gr11)/2-MO)**2*count10/100)

print('MO=',MO)
print('\nDispersia=',Dispersia)
import math
SKO = math.sqrt(Dispersia)
print('\nSKO=',SKO)

print('\nt1=', ((gr1+gr2)/2-MO)/SKO,
'\nt2=', ((gr2+gr3)/2-MO)/SKO,
'\nt3=', ((gr3+gr4)/2-MO)/SKO,
'\nt4=', ((gr4+gr5)/2-MO)/SKO,
'\nt5=', ((gr5+gr6)/2-MO)/SKO,
'\nt6=', ((gr6+gr7)/2-MO)/SKO,
'\nt7=', ((gr7+gr8)/2-MO)/SKO,
'\nt8=', ((gr8+gr9)/2-MO)/SKO,
'\nt9=', ((gr9+gr10)/2-MO)/SKO,
'\nt10=', ((gr10+gr11)/2-MO)/SKO)

fx1=(math.e**(-(((gr1+gr2)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx2=(math.e**(-(((gr2+gr3)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx3=(math.e**(-(((gr3+gr4)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx4=(math.e**(-(((gr4+gr5)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx5=(math.e**(-(((gr5+gr6)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx6=(math.e**(-(((gr6+gr7)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx7=(math.e**(-(((gr7+gr8)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx8=(math.e**(-(((gr8+gr9)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx9=(math.e**(-(((gr9+gr10)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)
fx10=(math.e**(-(((gr10+gr11)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi)

print('\nphi 1=',(math.e**(-(((gr1+gr2)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 2=',(math.e**(-(((gr2+gr3)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 3=',(math.e**(-(((gr3+gr4)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 4=',(math.e**(-(((gr4+gr5)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 5=',(math.e**(-(((gr5+gr6)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 6=',(math.e**(-(((gr6+gr7)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 7=',(math.e**(-(((gr7+gr8)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 8=',(math.e**(-(((gr8+gr9)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 9=',(math.e**(-(((gr9+gr10)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\nphi 10=',(math.e**(-(((gr10+gr11)/2-MO)/SKO)**2/2))/math.sqrt(2*math.pi),
'\n','\nfx1=',fx1/SKO,
'\nfx2=',fx2/SKO,
'\nfx3=',fx3/SKO,
'\nfx4=',fx4/SKO,
'\nfx5=',fx5/SKO,
'\nfx6=',fx6/SKO,
'\nfx7=',fx7/SKO,
'\nfx8=',fx8/SKO,
'\nfx9=',fx9/SKO,
'\nfx10=',fx10/SKO)

print('\n1=', (gr1-MO)/SKO,
'\n2=', (gr2-MO)/SKO,
'\n3=', (gr3-MO)/SKO,
'\n4=', (gr4-MO)/SKO,
'\n5=', (gr5-MO)/SKO,
'\n6=', (gr6-MO)/SKO,
'\n7=', (gr7-MO)/SKO,
'\n8=', (gr8-MO)/SKO,
'\n9=', (gr9-MO)/SKO,
'\n10=', (gr10-MO)/SKO,
'\n10=', (gr11-MO)/SKO)