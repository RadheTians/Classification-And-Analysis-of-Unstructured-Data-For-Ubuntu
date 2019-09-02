import subprocess
import os
import pymongo

def abcd(y,w,d):

	#print("press 1 to sort according to file type")
	#print("press 2 to sort according to age of file")
	#print("press 3 to sort according to last modified")
        #print("press 4 to sort according to last access")
	#q=raw_input("enter the choice")
	if int(w)==1:
	  x="ls -alXp "
	elif int(w)==2:
	  x="ls -alprt "
	elif int(w)==3:
	  x="ls -alprtc "
        elif int(w)==4:
	  x="ls -alprtu "
	x=x+y
	x=x+"| awk '{print $9}'"
	s=subprocess.check_output(x,shell=True)
	l=s.split()
        list=[]
	for i in l:
	   
	  if '.' in i:
	     
	    n=i.split(".")
	    
	 
	    if all(char.isdigit() for char in n[-1])==False and '/' not in i:   
	       
	      z="exiftool "+y+"/"+i+"| head -n 6| tail -n 1| awk '{print $(NF-1),$NF}'"
	      x="exiftool "+y+"/"+i+"| head -n 7| tail -n 1| awk '{print $(NF-1),$NF}'"
	      o="exiftool "+y+"/"+i+"| head -n 9| tail -n 1| awk '{print $NF}'" 
	      k="exiftool "+y+"/"+i+"| head -n 5| tail -n 1| awk '{print $(NF-1),$NF}'"
	      b="exiftool "+y+"/"+i+"| head -n 2| tail -n 1| awk '{print $NF}'" 

	      try:
		  
		  t=subprocess.check_output(z,shell=True)
		  q=subprocess.check_output(x,shell=True)
		  u=subprocess.check_output(o,shell=True)
		  if u.find('Error')!=-1:
		    u= n[-1].upper() 
		  v=subprocess.check_output(k,shell=True)
		  f=subprocess.check_output(b,shell=True)
		  #list.append(f)
		  #list.append(u)
		  #list.append(v)
		  #list.append(q)
		  #list.append(t)
		  list.extend((f,u,v,q,t))
                  list[:] = [l.rstrip('\n') for l in list]
                  #return list
		  #print f+u+v+q+t
	   
	      except subprocess.CalledProcessError as e:
		  
		  pass
        ll=list
        if int(w)==1:
           ll=sort(list)
        val=SetDataSet(ll,d)
        return val		    

def sort(list):
        l=list
        for i in range(1,len(l),5):
              for j in range(i+5,len(l),5):
                 if l[i].lower()>l[j].lower():
                    tp=l[i-1]
                    l[i-1]=l[j-1]
                    l[j-1]=tp
                    tp=l[i]
                    l[i]=l[j]
                    l[j]=tp
                    tp=l[i+1]
                    l[i+1]=l[j+1]
                    l[j+1]=tp
                    tp=l[i+2]
                    l[i+2]=l[j+2]
                    l[j+2]=tp
                    tp=l[i+3]
                    l[i+3]=l[j+3]
                    l[j+3]=tp
        return l 

def MongoConnect(mongolist,type):
	myclient=pymongo.MongoClient("mongodb+srv://aviral:monkey123@sandbox-0vx53.mongodb.net")
        mydb=myclient["filecollection"]
        mycol=mydb[type+'FILES']
        list=[]
        list.append(mongolist)
        result=mycol.insert_many(list)

def SetDataSet(Listvalue,d):
	JSON={}
	keys=['filename','filetype','fileage','lastmodified','lastaccess']  
	#values=[]
        listt=[]
	ListSet=Listvalue       
        for j in range(0,len(ListSet)-4,5): 
                list=[]
                for k in range(j,j+5,1):
                    list.append(ListSet[k])
                    #if k%5==1:
                       #values.append(ListSet[k])
                       #MongoConnect(JSON,ListSet[k])
                JSON=dict(zip(keys,list))
                if d==1: 
                    MongoConnect(JSON,list[1]) 
                listt.append(list) 

        return listt

