library(rio)
library(data.table)
library(magrittr)
library(zoo)
library(tidyverse)

dt<-fread("input3.txt",colClasses = "char",stringsAsFactors = FALSE)



dt2<-sapply(dt$V1,.%>% strsplit(.,""))


dt3<-do.call(rbind.data.frame,dt2)
colnames(dt3)<-NULL
dt3%>% as.matrix() 


add_char<-function(a,b){as.numeric(a)+as.numeric(b)}
Add_char<-function(x){Reduce(add_char,x)}

apply(dt3,2,Add_char) %>% `>`(500) %>% as.numeric() %>% paste0(.,collapse = "") %>% strtoi(.,base=2)

apply(dt3,2,Add_char) %>% `<`(500) %>% as.numeric() %>% paste0(.,collapse = "") %>% strtoi(.,base=2)


########### find O2
most_common<-function(v){
  value<-ifelse(Add_char(v)>=length(v)/2,1,0)
  pos<-which(v==value)
  return(list(value,pos))
}


most_common(c("1","0","1","0","1","0"))



######### find CO2

least_common<-function(v){
  value<-ifelse(Add_char(v)<length(v)/2,1,0)
  pos<-which(v==value)
  return(list(value,pos))
}


least_common(c("1","0","1","0","1","0"))


