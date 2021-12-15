library(rio)
library(data.table)
library(magrittr)
library(zoo)

dt<-fread("input2.txt")
dt[,sum(V2),by="V1"]
1965*(2140-958)

depth=0
aim=0
horizontal=0
for (i in 1:nrow(dt)){
  if(dt[i,V1]=="down"){
    aim=aim+dt[i,V2]
  }
  if(dt[i,V1]=="up"){
    aim=aim-dt[i,V2]
  }
  if(dt[i,V1]=="forward"){
    horizontal=horizontal+dt[i,V2]
    depth=depth+dt[i,V2]*aim
  }
}

horizontal*depth
