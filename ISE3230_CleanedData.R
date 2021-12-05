library(readr)

#Using Data From Fantasy Pros
points <- read_csv("C:/Users/chris/Downloads/FantasyPros_Fantasy_Football_Points_Allowed.csv")
points <- points[1:32,]

#Creating a table with each teams positional factor against QB, RB, WR, TE, and DST
points$std_QBpts <- (points$QB / mean_qb) 
qbpoints <- points[c(1,16)]

mean_rb <- mean(points$RB)
points$std_RBpts <- points$RB / mean_rb

mean_te <- mean(points$TE)
points$std_TEpts <- points$TE / mean_te

mean_wr <- mean(points$WR)
points$std_WRpts <- points$WR / (mean_wr)

mean_dst <- mean(points$DST)
points$std_DSTpts <- points$DST / mean_dst

stdpoints <- points[c(1,16,17,18,19,20)]

#qb projected weekly points

qbProj <- read_csv("C:/Users/chris/Downloads/FantasyPros_Fantasy_Football_Projections_QB.csv")
qbProj <- qbProj[2:11, c(1,2,12) ]
qbProj$FPTS <- qbProj$FPTS / 16


#rb projected weekly points
rbProj <- read_csv("C:/Users/chris/Downloads/FantasyPros_Fantasy_Football_Projections_RB.csv")
rbProj <- rbProj[2:11, c(1,2,10) ]
rbProj$FPTS <- rbProj$FPTS / 16

#wr projected weekly points
wrProj <- read_csv("C:/Users/chris/Downloads/FantasyPros_Fantasy_Football_Projections_WR.csv")
wrProj <- wrProj[2:11, c(1,2,10) ]
wrProj$FPTS <- wrProj$FPTS / 16

#te projected weekly points
teProj <- read_csv("C:/Users/chris/Downloads/FantasyPros_Fantasy_Football_Projections_TE.csv")
teProj <- teProj[2:11, c(1,2,7) ]
teProj$FPTS <- teProj$FPTS / 16

#dst projected weekly points
dstProj <- read_csv("C:/Users/chris/Downloads/FantasyPros_Fantasy_Football_Projections_DST.csv")
dstProj$FPTS <- dstProj$FPTS / 16
