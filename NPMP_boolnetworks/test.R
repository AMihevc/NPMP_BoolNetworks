library(BoolNet)
represirator <- loadNetwork("represirator.txt")
zac_stanja <- list(0,0,1)
path <- getPathToAttractor(repre, zac_stanja)
print(path)

