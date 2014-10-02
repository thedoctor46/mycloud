p=6008551475143
i=2

while i*i<p;
	while p%i==0:
		p=p/i
		i=i+i

print(p)
