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
  #return(list(value,pos))
  return(pos)
}


most_common(c("0","1","1","1","0","0"))

shrink<-function(l){
  if(nrow(l$df)<=1){
    return(l)
  }else{
    l$df[,l$i]%>% most_common -> keep
    df<-l$df[keep,]
    i=(l$i)%%12+1
    print(c(length(keep),i))
    return(shrink(list(df=df,i=i)))
  }
}

l<-shrink(list(df=dt3,i=1))
l$df%>% as.numeric() %>% paste0(.,collapse = "") %>% strtoi(.,base=2)
#825

######### find CO2

least_common<-function(v){
  value<-ifelse(Add_char(v)<length(v)/2,1,0)
  pos<-which(v==value)
  #return(list(value,pos))
  return(pos)
}


least_common(c("1","0","1","0","1","0"))

shrink2<-function(l){
  if(nrow(l$df)<=1){
    return(l)
  }else{
    l$df[,l$i]%>% least_common -> keep
    print(c(length(keep),l$i))
    df<-l$df[keep,]
    i=(l$i)%%12+1
    print(c(length(keep),i))
    return(shrink2(list(df=df,i=i)))
  }
}

l<-shrink2(list(df=dt3,i=1))
l$df%>% as.numeric() %>% paste0(.,collapse = "") %>% strtoi(.,base=2)
#3375
3375*825
