import time
from turtle import *
import time
from name import q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,heart,nn
from secrets import choice
def si():

     nu=(input("enter name: "))
     ls=[str(x) for x in nu]
     df=0
     for ij in range(0,len(ls)):

          if ls[ij]=='q':
               q()
          elif ls[ij]=='w':
               w()
          elif ls[ij]=='e':
               e()
               
          elif ls[ij]=='r':
               r()
               
          elif ls[ij]=='t':
               t()
               
          elif ls[ij]=='y':
               y()
               
          elif ls[ij]=='u':
               u()
               
          elif ls[ij]=='i':
               i()
               
          elif ls[ij]=='o':
               o()
               
          elif ls[ij]=='p':
               p()
               
          elif ls[ij]=='a':
               a()
               
          elif ls[ij]=='s':
               s()
               
          elif ls[ij]=='d':
               d()
               
          elif ls[ij]=='f':
               f()
               
          elif ls[ij]=='g':
               g()
               
          elif ls[ij]=='h':
               h()
               
          elif ls[ij]=='j':
               j()
               
          elif ls[ij]=='k':
               k()
               
          elif ls[ij]=='l':
               l()
               
          elif ls[ij]=='z':
               z()
               
          elif ls[ij]=='c':
               c()
               
          elif ls[ij]=='x':
               x()
               
          elif ls[ij]=='v':
               v()
               
          elif ls[ij]=='b':
               b()
               
          elif ls[ij]=='n':
               n()
               
          elif ls[ij]=='m':
               m()
               
          else:
               break
def ff():         
     penup()
     fd(330)
     pendown()
nk=1
while(nk==1):
     nn()
     si()
     heart()
     time.sleep(5)
     reset()
     pensize(6)
     print("if you want to cancel press 0 : ")
     nk=int (input("if you want to continue press 1 :  "))