import numpy             as np
import matplotlib.pyplot as plt
import seaborn           as sns
sns.set(rc={'axes.facecolor':'whitesmoke'})
'''
    x_data1    : Pressure measured
    y_data1    : Energy of Pu-239
    y_data2    : Energy of Am-241
    y_data3    : Energy of Cm-244
    distance   : Convert the pressure in x_data1 to equivalent length

'''
x_data1     = [100   ,    210,    410,    510,    555,    605,    665,    705,    725,    745,    755,   765]
y_data1     = [5131.0, 4692.9, 3595.2, 3005.8, 2709.8, 2334.9, 1932.5, 1523.3, 1270.1, 1055.4,  839.7,     0]
y_data2     = [5465.2, 4958.0, 4009.1, 3472.7, 3195.1, 2864.7, 2514.7, 2173.6, 1965.1, 1801.4, 1642.8, 203.1]
y_data3     = [5780.7, 5297.8, 4387.8, 3894.9, 3618.3, 3343.6, 3027.6, 2726.7, 2543.5, 2382.2, 2265.6, 959.0]
distance    = []

for i in range(len(x_data1)):
    distance.append(x_data1[i]*4/765.0)
'''
    poly1         : polynomial fitting for energy of Pu-239
    poly2         : polynomial fitting for energy of Am-241
    poly3         : polynomial fitting for energy of Cm-244
    poly1s        : polynomial fitting for energy of Pu-239 at max uncertainties
    poly2s        : polynomial fitting for energy of Am-241 at max uncertainties
    poly3s        : polynomial fitting for energy of Cm-244 at max uncertainties
    poly1m        : polynomial fitting for energy of Pu-239 at min uncertainties
    poly2m        : polynomial fitting for energy of Am-241 at min uncertainties
    poly3m        : polynomial fitting for energy of Cm-244 at min uncertainties
    y_data1_poly  : plotting poly1
    y_data2_poly  : plotting poly2
    y_data3_poly  : plotting poly3
    y_data1_polys : plotting poly1s
    y_data2_polys : plotting poly2s
    y_data3_polys : plotting poly3s
    y_data1_polym : plotting poly1m
    y_data2_polym : plotting poly2m
    y_data3_polym : plotting poly3m
    distance_new  : new array for more resolution distance-wise

'''
poly1         = np.polyfit(distance[7:-1],y_data1[7:-1]                                       ,deg=2 )
poly2         = np.polyfit(distance[7:-1],y_data2[7:-1]                                       ,deg=2 )
poly3         = np.polyfit(distance[7:-1],y_data3[7:-1]                                       ,deg=2 )
poly1s        = np.polyfit(distance[7:-1],[y_data1[i] + 100 for i in range(7,len(x_data1)-1) ],deg=2 )
poly2s        = np.polyfit(distance[7:-1],[y_data2[i] + 100 for i in range(7,len(x_data1)-1) ],deg=2 )
poly3s        = np.polyfit(distance[7:-1],[y_data3[i] + 100 for i in range(7,len(x_data1)-1) ],deg=2 )
poly1m        = np.polyfit(distance[7:-1],[y_data1[i] - 100 for i in range(7,len(x_data1)-1) ],deg=2 )
poly2m        = np.polyfit(distance[7:-1],[y_data2[i] - 100 for i in range(7,len(x_data1)-1) ],deg=2 )
poly3m        = np.polyfit(distance[7:-1],[y_data3[i] - 100 for i in range(7,len(x_data1)-1) ],deg=2 )
y_data1_poly  = []
y_data2_poly  = []
y_data3_poly  = []
y_data1_polys = []
y_data2_polys = []
y_data3_polys = []
y_data1_polym = []
y_data2_polym = []
y_data3_polym = []
distance_new  = np.linspace(distance[len(distance)-2],5,120)

for i in range(len(distance_new)):
    y_data1_poly.append( poly1[2] +poly1[1] *distance_new[i]+poly1[0] *distance_new[i]*distance_new[i])
    y_data2_poly.append( poly2[2] +poly2[1] *distance_new[i]+poly2[0] *distance_new[i]*distance_new[i])
    y_data3_poly.append( poly3[2] +poly3[1] *distance_new[i]+poly3[0] *distance_new[i]*distance_new[i])
    y_data1_polys.append(poly1s[2]+poly1s[1]*distance_new[i]+poly1s[0]*distance_new[i]*distance_new[i])
    y_data2_polys.append(poly2s[2]+poly2s[1]*distance_new[i]+poly2s[0]*distance_new[i]*distance_new[i])
    y_data3_polys.append(poly3s[2]+poly3s[1]*distance_new[i]+poly3s[0]*distance_new[i]*distance_new[i])
    y_data1_polym.append(poly1m[2]+poly1m[1]*distance_new[i]+poly1m[0]*distance_new[i]*distance_new[i])
    y_data2_polym.append(poly2m[2]+poly2m[1]*distance_new[i]+poly2m[0]*distance_new[i]*distance_new[i])
    y_data3_polym.append(poly3m[2]+poly3m[1]*distance_new[i]+poly3m[0]*distance_new[i]*distance_new[i])

plt.rcParams["figure.figsize"] = (15,10)
fig, axs = plt.subplots(3, 1,sharex=True, sharey=True)

axs[0].scatter(distance[:-1], y_data1[:-1], marker='x', color='blue'                              )
axs[0].plot(   distance[:-1], y_data1[:-1]            , color='blue'             , label='Pu-239' )
axs[0].plot(   distance_new , y_data1_poly            , color='black' ,alpha=0.5 , label='Fit'    )

axs[0].fill_between(distance[:-1], [y_data1[i] - 100 for i in range(len(x_data1)-1) ], [y_data1[i] + 100 for i in range(len(x_data1)-1) ], color='blue' , alpha=0.1)
axs[0].fill_between(distance_new , y_data1_polym                                     , y_data1_polys                                     , color='black', alpha=0.1)

axs[0].set_ylim(-10,7000)
axs[0].legend()

axs[1].scatter(distance[:-1], y_data2[:-1], marker='x', color='red'             )
axs[1].plot(distance[:-1], y_data2[:-1] ,color='red'            , label='Am-241')
axs[1].plot(distance_new , y_data2_poly ,color='black',alpha=0.5, label='Fit'   )

axs[1].fill_between(distance[:-1], [y_data2[i] - 100 for i in range(len(x_data1)-1) ], [y_data2[i] + 100 for i in range(len(x_data1)-1) ], color='red'  , alpha=0.1)
axs[1].fill_between( distance_new, y_data2_polym                                     , y_data2_polys                                     , color='black', alpha=0.1)

axs[1].set_ylim(-10,7000)
axs[1].legend()

axs[2].scatter(distance[:-1], y_data3[:-1], marker='x', color='green'                         )
axs[2].plot(   distance[:-1], y_data3[:-1]            , color='green'         , label='Cm-244')
axs[2].plot(    distance_new, y_data3_poly            ,color='black',alpha=0.5, label='Fit'   )

axs[2].fill_between(distance[:-1], [y_data3[i] - 100 for i in range(len(x_data1)-1) ], [y_data3[i] + 100 for i in range(len(x_data1)-1) ], color='green', alpha=0.1)
axs[2].fill_between( distance_new, y_data3_polym                                     , y_data3_polys                                     , color='black', alpha=0.1)

axs[2].set_ylim(-10,7000)
axs[2].legend()

plt.suptitle('Energy (keV) in function of the effective length (cm)')
axs[2].set_xlabel('Effective length (cm)')
axs[1].set_ylabel('Energy (keV)'         )
plt.savefig('plot_energy.png',dpi=300)

plt.clf()


n_data1          = [ 300,  290,  285,  268,  259,  305,  295,  281,  325,  251,  233, 0.00]
n_data1error     = [5.77, 5.87, 5.92, 6.11, 6.21, 5.73, 5.82, 5.97, 5.55, 6.31, 6.55, 0.00]
n_data2          = [ 283,  310,  251,  261,  265,  290,  282,  308,  274,  255,  238,  220]
n_data2error     = [5.94, 5.68, 6.31, 6.19, 6.14, 5.87, 5.95, 5.70, 6.04, 6.26, 6.48, 6.74]
n_data3          = [ 237,  207,  213,  257,  226,  241,  222,  215,  249,  208,  188,  149]
n_data3error     = [6.50, 6.95, 6.85, 6.24, 6.65, 6.44, 6.71, 6.82, 6.34, 6.93, 7.29, 8.19]
n_data1errortrue = []
n_data2errortrue = []
n_data3errortrue = []
for i in range(len(n_data2)):
    n_data1errortrue.append(n_data1[i]*n_data1error[i]/100.0)
    n_data2errortrue.append(n_data2[i]*n_data2error[i]/100.0)
    n_data3errortrue.append(n_data3[i]*n_data3error[i]/100.0)


meann1  = []
meann2  = []
meann3  = []
meann1s = []
meann2s = []
meann3s = []
meann1p = []
meann2p = []
meann3p = []
Sum1    =  sum(n_data1[0:len(n_data1)-3])                       /(len(n_data1)-3)
Sum2    =  sum(n_data2[0:len(n_data1)-3])                       /(len(n_data1)-3)
Sum3    =  sum(n_data3[0:len(n_data1)-3])                       /(len(n_data1)-3)
Sum1s   = (sum(n_data1[0:len(n_data1)-3])+sum(n_data1errortrue))/(len(n_data1)-3)
Sum2s   = (sum(n_data2[0:len(n_data1)-3])+sum(n_data2errortrue))/(len(n_data1)-3)
Sum3s   = (sum(n_data3[0:len(n_data1)-3])+sum(n_data3errortrue))/(len(n_data1)-3)
Sum1p   = (sum(n_data1[0:len(n_data1)-3])-sum(n_data1errortrue))/(len(n_data1)-3)
Sum2p   = (sum(n_data2[0:len(n_data1)-3])-sum(n_data2errortrue))/(len(n_data1)-3)
Sum3p   = (sum(n_data3[0:len(n_data1)-3])-sum(n_data3errortrue))/(len(n_data1)-3)

for i in range(len(n_data1)):
    if i < len(n_data1)-3:
        meann1.append( Sum1 )
        meann2.append( Sum2 )
        meann3.append( Sum3 )
        meann1s.append(Sum1s)
        meann2s.append(Sum2s)
        meann3s.append(Sum3s)
        meann1p.append(Sum1p)
        meann2p.append(Sum2p)
        meann3p.append(Sum3p)
    else:
        meann1.append( n_data1[i]                    )
        meann2.append( n_data2[i]                    )
        meann3.append( n_data3[i]                    )
        meann1s.append(n_data1[i]+n_data1errortrue[i])
        meann2s.append(n_data2[i]+n_data2errortrue[i])
        meann3s.append(n_data3[i]+n_data3errortrue[i])
        meann1p.append(n_data1[i]-n_data1errortrue[i])
        meann2p.append(n_data2[i]-n_data2errortrue[i])
        meann3p.append(n_data3[i]-n_data3errortrue[i])

poly1         = np.polyfit(distance[7:-1],meann1[7:-1],deg=2  )
poly2         = np.polyfit(distance[8:],meann2[8:],deg=2      )
poly3         = np.polyfit(distance[8:],meann3[8:],deg=2      )
poly1s        = np.polyfit(distance[7:-1],meann1s[7:-1],deg=2 )
poly2s        = np.polyfit(distance[8:],meann2s[8:],deg=2     )
poly3s        = np.polyfit(distance[8:],meann3s[8:],deg=2     )
poly1p        = np.polyfit(distance[7:-1],meann1p[7:-1],deg=2 )
poly2p        = np.polyfit(distance[8:],meann2p[8:],deg=2     )
poly3p        = np.polyfit(distance[8:],meann3p[8:],deg=2     )
n_data1_poly  = []
n_data2_poly  = []
n_data3_poly  = []
n_data1_polys = []
n_data2_polys = []
n_data3_polys = []
n_data1_polyp = []
n_data2_polyp = []
n_data3_polyp = []
distance_new  = np.linspace(3.9477,5,120)

for i in range(len(distance_new)):
    n_data1_poly.append( poly1[2] +poly1[1] *distance_new[i]+poly1[0] *distance_new[i]*distance_new[i])
    n_data2_poly.append( poly2[2] +poly2[1] *distance_new[i]+poly2[0] *distance_new[i]*distance_new[i])
    n_data3_poly.append( poly3[2] +poly3[1] *distance_new[i]+poly3[0] *distance_new[i]*distance_new[i])
    n_data1_polys.append(poly1s[2]+poly1s[1]*distance_new[i]+poly1s[0]*distance_new[i]*distance_new[i])
    n_data2_polys.append(poly2s[2]+poly2s[1]*distance_new[i]+poly2s[0]*distance_new[i]*distance_new[i])
    n_data3_polys.append(poly3s[2]+poly3s[1]*distance_new[i]+poly3s[0]*distance_new[i]*distance_new[i])
    n_data1_polyp.append(poly1p[2]+poly1p[1]*distance_new[i]+poly1p[0]*distance_new[i]*distance_new[i])
    n_data2_polyp.append(poly2p[2]+poly2p[1]*distance_new[i]+poly2p[0]*distance_new[i]*distance_new[i])
    n_data3_polyp.append(poly3p[2]+poly3p[1]*distance_new[i]+poly3p[0]*distance_new[i]*distance_new[i])

fig, axs = plt.subplots(3, 1)

axs[0].scatter(distance[:-1], n_data1[:-1], marker='x', color='blue', label='Pu 239')
axs[0].plot(   distance[:-1], n_data1[:-1]            , color='blue'            )
axs[0].plot(   distance_new, n_data1_poly             , color='black',alpha=0.5,  label='Fit'          )
#axs[0].plot(   distance_new, n_data1_polys   ,'--'         , color='black',alpha=0.5)
#axs[0].plot(   distance_new, n_data1_polyp   ,'--'         , color='black',alpha=0.5)
axs[0].plot(   distance_new , [n_data1_poly[i]+15 for i in range(len(distance_new))] ,'--' , color='black',alpha=0.5)
axs[0].plot(   distance_new , [n_data1_poly[i]-15 for i in range(len(distance_new))] ,'--' , color='black',alpha=0.5)
axs[0].plot(   distance[:-1], meann1[:-1]            , color='black'      , alpha=0.5)
axs[0].plot(   distance[:-1], meann1s[:-1]         ,'--'   , color='black', alpha=0.5)
axs[0].plot(   distance[:-1], meann1p[:-1]         ,'--'   , color='black', alpha=0.5)
axs[0].fill_between(distance[:-1], [n_data1[i] - n_data1[i]*n_data1error[i]/100 for i in range(len(x_data1)-1) ], [n_data1[i] + n_data1[i]*n_data1error[i]/100 for i in range(len(x_data1)-1) ], color='blue', alpha=0.2)
axs[0].fill_between(distance[:-1], meann1p[:-1],meann1s[:-1] , color='black', alpha=0.05)
#axs[0].fill_between(distance_new, n_data1_polyp,n_data1_polys , color='black', alpha=0.05)
axs[0].fill_between(distance_new, [n_data1_poly[i]-15 for i in range(len(distance_new))],[n_data1_poly[i]+15 for i in range(len(distance_new))] , color='black', alpha=0.05)

axs[1].scatter(distance, n_data2, marker='x', color='red', label='Am-241')
axs[1].plot(   distance, n_data2            , color='red'        )
axs[1].plot(   distance_new, n_data2_poly            , color='black',alpha=0.5,  label='Fit'          )
axs[1].plot(   distance_new, n_data2_polys   ,'--'         , color='black',alpha=0.5)
axs[1].plot(   distance_new, n_data2_polyp   ,'--'         , color='black',alpha=0.5)
axs[1].plot(   distance, meann2            , color='black'      , alpha=0.5)
axs[1].plot(   distance, meann2s          ,'--'  , color='black', alpha=0.5)
axs[1].plot(   distance, meann2p          ,'--'  , color='black', alpha=0.5)
axs[1].fill_between(distance, [n_data2[i] - n_data2[i]*n_data2error[i]/100 for i in range(len(x_data1)) ], [n_data2[i] + n_data2[i]*n_data2error[i]/100 for i in range(len(x_data1)) ], color='red', alpha=0.2)
axs[1].fill_between(distance, meann2p,meann2s , color='black', alpha=0.05)
axs[1].fill_between(distance_new, n_data2_polyp,n_data2_polys , color='black', alpha=0.05)

axs[2].scatter(distance, n_data3, marker='x', color='green', label='Cm-244')
axs[2].plot(   distance, n_data3            , color='green'            )
axs[2].plot(   distance_new, n_data3_poly            , color='black'  ,alpha=0.5,  label='Fit'          )
axs[2].plot(   distance_new, n_data3_polys   ,'--'         , color='black',alpha=0.5)
axs[2].plot(   distance_new, n_data3_polyp   ,'--'         , color='black',alpha=0.5)
axs[2].plot(   distance, meann3           , color='black'       , alpha=0.5)
axs[2].plot(   distance, meann3s          ,'--'  , color='black', alpha=0.5)
axs[2].plot(   distance, meann3p          ,'--'  , color='black', alpha=0.5)
axs[2].fill_between(distance, [n_data3[i] - n_data3[i]*n_data3error[i]/100 for i in range(len(x_data1)) ], [n_data3[i] + n_data3[i]*n_data3error[i]/100 for i in range(len(x_data1)) ], color='green', alpha=0.2)
axs[2].fill_between(distance, meann3p,meann3s , color='black', alpha=0.05)
axs[2].fill_between(distance_new, n_data3_polyp,n_data3_polys , color='black', alpha=0.05)

axs[2].set_xlabel('')

axs[0].set_ylim(-1,350)
axs[1].set_ylim(-1,350)
axs[2].set_ylim(-1,350)
plt.suptitle('Number of counts in function of the effective length (cm)')
axs[2].set_xlabel('Effective length (cm)')
axs[1].set_ylabel('Number of counts')

axs[0].legend()
axs[1].legend()
axs[2].legend()


plt.savefig('plot_n.png',dpi=300)
plt.clf()
#plt.show()

distance_new = np.linspace(3.9477,5,120)
print('—————————————————————————————————————')
for i in range(len(distance_new)):
    if n_data1_poly[i] +15< 0 :
        print('RN for Pu-239 sup: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if n_data1_poly[i] < 0 :
        print('RN for Pu-239 mid: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if n_data1_poly[i]-15 < 0 :
        print('RN for Pu-239 inf: ',distance_new[i])
        break
    else: pass
print(' ')

for i in range(len(distance_new)):
    if n_data2_polys[i] < 0 :
        print('RN for Am-241 sup: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if n_data2_poly[i] < 0 :
        print('RN for Am-241 mid: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if n_data2_polyp[i] < 0 :
        print('RN for Am-241 inf: ',distance_new[i])
        break
    else: pass

print(' ')

for i in range(len(distance_new)):
    if n_data3_polys[i] < 0 :
        print('RN for Cm-244 sup: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if n_data3_poly[i] < 0 :
        print('RN for Cm-244 mid: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if n_data3_polyp[i] < 0 :
        print('RN for Cm-244 inf: ',distance_new[i])
        break
    else: pass


print(' ')
print('—————————————————————————————————————')
#print('RE for Pu-239 sup:  4.204142857142857')
print(' ')
distance_new = np.linspace(3.9477,5,120)
for i in range(len(distance_new)):
    if y_data1_polys[i] < 0 :
        print('RE for Pu-239 sup: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if y_data1_poly[i] < 0 :
        print('RE for Pu-239 mid: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if y_data1_polym[i] < 0 :
        print('RE for Pu-239 inf: ',distance_new[i])
        break
    else: pass

print(' ')
for i in range(len(distance_new)):
    if y_data2_polys[i] < 0 :
        print('RE for Am-241 sup: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if y_data2_poly[i] < 0 :
        print('RE for Am-241 mid: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if y_data2_polym[i] < 0 :
        print('RE for Am-241 inf: ',distance_new[i])
        break
    else: pass

print(' ')
for i in range(len(distance_new)):
    if y_data3_polys[i] < 0 :
        print('RE for Cm-244 sup: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if y_data3_poly[i] < 0 :
        print('RE for Cm-244 mid: ',distance_new[i])
        break
    else: pass
for i in range(len(distance_new)):
    if y_data3_polym[i] < 0 :
        print('RE for Cm-244 inf: ',distance_new[i])
        break
    else: pass
print('—————————————————————————————————————')


derivae1 =[]
derivae2 =[]
derivae3 =[]
derivae1.append((y_data1[1]-y_data1[0])/(distance[1]-distance[0]))
derivae2.append((y_data2[1]-y_data2[0])/(distance[1]-distance[0]))
derivae3.append((y_data3[1]-y_data3[0])/(distance[1]-distance[0]))
for i in range(1,len(y_data1)):
    if i==len(y_data1)-1:
        derivae1.append(abs((y_data1[i]-y_data1[i-1])/(distance[i]-distance[i-1])))
        derivae2.append(abs((y_data2[i]-y_data2[i-1])/(distance[i]-distance[i-1])))
        derivae3.append(abs((y_data3[i]-y_data3[i-1])/(distance[i]-distance[i-1])))

    else:
        derivae1.append(abs((y_data1[i+1]-y_data1[i-1])/(distance[i+1]-distance[i-1])))
        derivae2.append(abs((y_data2[i+1]-y_data2[i-1])/(distance[i+1]-distance[i-1])))
        derivae3.append(abs((y_data3[i+1]-y_data3[i-1])/(distance[i+1]-distance[i-1])))

poly1 = np.polyfit(np.log(y_data1[1:-2]),np.log(derivae1[1:-2]),deg=1 )
poly2 = np.polyfit(np.log(y_data2[1:-2]),np.log(derivae2[1:-2]),deg=1 )
poly3 = np.polyfit(np.log(y_data3[1:-2]),np.log(derivae3[1:-2]),deg=1 )
poly1_plot = []
poly2_plot = []
poly3_plot = []
for i in range(len(y_data1)):
    poly1_plot.append(poly1[1]+poly1[0]*np.log(y_data1[i]))
    poly2_plot.append(poly2[1]+poly2[0]*np.log(y_data2[i]))
    poly3_plot.append(poly3[1]+poly3[0]*np.log(y_data3[i]))
#poly2 = np.polyfit(distance[7:-1],y_data1[7:-1],deg=2 )
#poly3 = np.polyfit(distance[7:-1],y_data1[7:-1],deg=2 )




plt.xscale("log")
plt.yscale("log")
plt.xlabel('log(equivalent length)')
plt.ylabel('log(stopping power)')
plt.plot(   distance, derivae1            , color='blue',label='Pu-239')
plt.plot(   distance, derivae2            , color='red',label='Am-241')
plt.plot(   distance, derivae3            , color='green',label='Cm-244')
#plt.scatter(distance, derivae1, marker='x', color='red'                   )
plt.legend()
plt.savefig('plot_stop_x.png',dpi=300)
#plt.show()

plt.clf()
fig, axs = plt.subplots(3, 1)
axs[0].set_xscale("log")
axs[1].set_xscale("log")
axs[2].set_xscale("log")
axs[0].set_yscale("log")
axs[1].set_yscale("log")
axs[2].set_yscale("log")

axs[0].plot(   [y_data1[i]*(10**(-3)) for i in range(1,len(y_data1)-2)] , np.exp(poly1_plot[1:-2])          , color='black',label='fit',alpha=0.5)
axs[1].plot(   [y_data2[i]*(10**(-3)) for i in range(1,len(y_data1)-2)] , np.exp(poly2_plot[1:-2])          , color='black',label='fit',alpha=0.5)
axs[2].plot(   [y_data3[i]*(10**(-3)) for i in range(1,len(y_data1)-2)] , np.exp(poly3_plot[1:-2])          , color='black',label='fit',alpha=0.5)

axs[0].plot(   [y_data1[i]*(10**(-3)) for i in range(1,len(y_data1)-2)] , (derivae1[1:-2])           , color='blue',label='Pu-239')
axs[1].plot(   [y_data2[i]*(10**(-3)) for i in range(1,len(y_data1)-2)] , (derivae2[1:-2])           , color='red',label='Am-241')
axs[2].plot(   [y_data3[i]*(10**(-3)) for i in range(1,len(y_data1)-2)] , (derivae3[1:-2])           , color='green',label='Cm-244')
#plt.scatter(y_data1[1:-2] , derivae1[1:-2],marker='x', color='blue'                   )
'''
axs[0].set_ylim(5*(10**2),3*(10**3))
axs[1].set_ylim(5*(10**2),3*(10**3))
axs[2].set_ylim(5*(10**2),3*(10**3))
'''
'''
axs[0].set_ylim(9*(10**2),2*(10**3))
axs[1].set_ylim(1*(10**2),2*(10**3))
axs[2].set_ylim(1*(10**2),2*(10**3))
'''
plt.suptitle('Stopping power (MeV cm$^2$/g) in function of energy (MeV)')
axs[2].set_xlabel('log(Energy) MeV')
axs[1].set_ylabel('log(stopping power)')
axs[0].legend()
axs[1].legend()
axs[2].legend()
plt.savefig('plot_stop_E.png',dpi=300)
