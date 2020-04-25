import time
tic = time.clock()
for i in range(5):
    u = i**2
toc = time.clock()

print(f'TIME ELAPSED {toc-tic}')