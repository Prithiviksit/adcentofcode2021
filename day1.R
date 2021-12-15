library(data.table)
library(magrittr)
library(zoo)
dt<-fread("input.txt") 
dt<-dt$V1

count=0
previous=FALSE
for (i in 1:length(dt)){
    if(previous){
      if (dt[i]>previous){
        previous=dt[i]
        count=count+1
      }else{
        previous=dt[i]
      }
    }else{
      previous=dt[i]
    }
}

dt2<-rollapply(dt,3,sum)

count=0
previous=FALSE
for (i in 1:length(dt2)){
  if(previous){
    if (dt2[i]>previous){
      previous=dt2[i]
      count=count+1
    }else{
      previous=dt2[i]
    }
  }else{
    previous=dt2[i]
  }
}
