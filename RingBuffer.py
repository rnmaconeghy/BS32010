file = open('signal.txt')

data=[]

for line in file:
   data.append(line.strip())

buffersize=10
 
buffer=[] 

buffertotal=0 

position =0 

result=[]

while len(buffer) < buffersize:

   buffer.append(float(data[position]))

   buffertotal=float(buffertotal)
   buffertotal += float(data[position]) 

   position=float(position)
   position += 1

