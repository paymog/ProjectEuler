import CommonFunctions as cf

sieve = cf.sieve_of_Erastothenes(10000)
best_num = 0
best_ratio = 0
for i in range(1,1000000):
    phi = cf.eulers_totient(i, sieve=sieve)

    if i / phi > best_ratio:
        best_ratio = i / phi
        best_num = i

print best_num