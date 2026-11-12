from math import isqrt
N=100000
s=[0]*(N+1)
for d in range(1,N+1):
    for k in range(d,N+1,d):
        s[k]+=d

def prime(x):
    return x>=2 and all(x%d for d in range(2,isqrt(x)+1))

seen={}
for n in range(1,N+1):
    if prime(s[n]):
        seen.setdefault(s[n],[]).append(n)
print('arguments checked:', N)
print('prime divisor-sum arguments:', sum(map(len,seen.values())))
print('collisions within range:', [(p,v) for p,v in seen.items() if len(v)>1])
print('8191 repunits:', sum(2**i for i in range(13)), sum(90**i for i in range(3)))

reps = [(b, length) for b in range(2,91) for length in range(3,14) if sum(b**i for i in range(length)) == 8191]
assert reps == [(2, 13), (90, 3)]
print('all nontrivial repunit representations of 8191:', reps)
reps31 = [(b, length) for b in range(2,6) for length in range(3,6) if sum(b**i for i in range(length)) == 31]
assert reps31 == [(2, 5), (5, 3)]
print('all nontrivial repunit representations of 31:', reps31)
