library(rio)
library(data.table)
library(magrittr)
library(zoo)

dt<-fread("input3.txt")%>%as.data.table()


dt<-read.table("input3.txt")
