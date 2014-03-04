file = open('signal.txt')
#it took me a while to figure out how to get the file signal to read into the script
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

# the problem is in the above bit of code where I encountered a problem
#I then googled it and found an alternative piece of script which is above
#This fixed my problem but then I encountered another. By chaning all int to float I thought it would be fixed. 
#I then came back to the original problem again.. 

result.append(float(buffertotal)/buffersize)

for v in range(position, len(data)): 

   buffertotal=buffertotal-buffer[v%buffersize] 
   buffer[v%buffersize]=data[v] 
   buffertotal=buffertotal+buffer[v%buffersize] 
   result.append(float(buffertotal)/buffersize)

print result
