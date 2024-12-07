#just a copy 

K3=0
I3=0
while I3<100:
  K2=0
  I2=0
  while I2 < 1000:
    K=0
    I1=0
    while I1 != 1:  
      Y=random.randrange(1,21,1)
      if Y == 1:
        I1=I1+1
      K = K+1
    I2=I2+1
    K2=K2+K
  #print(K)
  I3 = I3+1
  print("I3 =" , I3 ,"K2 =",K2/1000)
  K3 = K3 + K2

print("K3 =", K3/100000)