d=30
n=10000
a=np.random.rand(d)
b=np.random.rand(n,d)
fa=np.fft.rfft(a[::-1],d*n*2)
fb=np.fft.rfft(b.flatten(),d*n*2)
xcorr = np.fft.irfft(fa*fb)
conv = []
for i in range(n):
    conv.append( xcorr[d*i+d-1] )
conv = np.array(conv)
print conv
print b.dot(a)
