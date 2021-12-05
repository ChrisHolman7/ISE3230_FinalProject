# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:10:45 2021

@author: chris
"""

import cvxpy as cp

#objective function (maximize the minimum week)
z = cp.Variable(1, nonneg = True)

#quarterbacks
x = cp.Variable(10, boolean = True )

#top 10 qb weekly projected points
qbProj = [24.33125, 24.12500, 23.71250, 23.07500, 22.46250, 21.99375, 21.42500, 21.40000, 21.18750, 20.14375]

#qb factor for each team
qbDef = {
    "ARI": 0.7836082, "ATL": 0.9701816, "BAL": 0.9915042, "BUF": 0.7409629, "CAR": 0.8582375, "CHI": 1.0341496, "CIN": 0.9062136, "CLE": 1.0021656, "DAL": 1.0661336, "DEN": 0.8582375, 
    "DET": 1.0501416,  "GB": 0.8209229, "HOU": 1.0714643, "IND": 1.0661336,"JAC": 0.9381976, "KC": 1.1034483, "LV": 1.1514243, "LAC": 0.9275362,"LAR": 0.9755122,
    "MIA": 1.1354323,"MIN": 1.0394803,"NE": 0.7196402, "NO": 1.3273363, "NYG": 0.9968349, "NYJ": 1.0021656,
    "PHI": 1.0288189,"PIT": 0.9595202, "SF": 0.9648509, "SEA": 1.0181576, "TB": 1.0074963,"TEN": 1.0767949,
    "WFT": 1.4072964, "BYE" : 0 }

#running backs
r = cp.Variable(10, boolean = True)

#top 10 rb weekly proj points
rbProj = [18.45625, 17.41250, 17.26250, 15.70000, 14.34375, 14.15625, 13.97500, 13.86875, 13.71250, 13.23125]

#rb factor for each team
rbDef = {
    "ARI": 0.8313751, "ATL": 1.0378951, "BAL": 0.9319874, "BUF": 0.9743505, "CAR": 0.8896244, "CHI": 1.0378951, "CIN": 1.0061228, "CLE": 0.9584643, "DAL": 1.0802581, "DEN": 0.9796459, 
    "DET": 1.2761873,  "GB": 0.8896244, "HOU": 1.0961443, "IND": 0.7466490,"JAC": 0.9055105, "KC": 0.8949197,  "LV": 1.1755750, "LAC": 1.2603012,"LAR": 0.9213967,
    "MIA": 0.9955320,"MIN": 1.0114182,"NE": 0.8472613, "NO": 0.8419659, "NYG": 1.1490981, "NYJ": 1.5462519,
    "PHI": 0.9743505,"PIT": 1.0167136, "SF": 0.7837167, "SEA": 1.2603012, "TB": 0.8631474,"TEN": 0.8525567,
    "WFT": 0.9637597, "BYE" : 0 
    }

#wide receivers
w = cp.Variable(10, boolean = True)

#top 10 wr weekly proj points
wrProj = [14.41250, 14.02500, 12.89375, 12.48125, 11.95625, 11.93750, 11.77500, 11.65000, 10.32500, 10.17500]

#wr factor for each team
wrDef = {
    "ARI": 0.8969100, "ATL": 1.0281652, "BAL": 1.0150396, "BUF": 0.6650260, "CAR": 0.8006563, "CHI": 1.1681706, "CIN": 0.8881597, "CLE": 0.9712879, "DAL": 1.1419196, "DEN": 1.0544162, 
    "DET": 0.9931638,  "GB": 0.8444080, "HOU": 1.1112934, "IND": 1.1331693,"JAC": 1.0106645, "KC": 0.9406617,  "LV": 1.0019141, "LAC": 0.8706590,"LAR": 0.9712879,
    "MIA": 1.1856713,"MIN": 1.1287941,"NE": 0.8575335, "NO": 1.2687996, "NYG": 1.0325403, "NYJ": 1.0762920,
    "PHI": 0.8706590,"PIT": 1.0150396, "SF": 0.9362866, "SEA": 0.9537873, "TB": 0.8225321,"TEN": 1.1287941,
    "WFT": 1.2162975, "BYE" : 0 
    }

#tight ends
t = cp.Variable(10, boolean = True)

#top 10 wr weekly proj points
teProj = [12.60625, 10.44375,  9.50000,  8.42500,  7.15625,  6.58125,  6.30000,  6.28125,  6.26250,  6.03750]

#te factor for each team
teDef = {
    "ARI": 0.5783133, "ATL": 0.7710843, "BAL": 1.1566265, "BUF": 0.7582329, "CAR": 0.7710843, "CHI": 0.7582329, "CIN": 1.0024096, "CLE": 0.9895582, "DAL": 1.0409639, "DEN": 0.5911647, 
    "DET": 0.9381526,  "GB": 0.8481928, "HOU": 1.2594378, "IND": 1.3108434,"JAC": 1.0666667, "KC": 1.2337349,  "LV": 1.7220884, "LAC": 1.3622490,"LAR": 1.2208835,
    "MIA": 1.1823293,"MIN": 0.7068273,"NE": 0.6297189, "NO": 1.0795181, "NYG": 0.9253012, "NYJ": 1.1566265,
    "PHI": 1.4779116,"PIT": 0.8738956, "SF": 0.4883534, "SEA": 1.2979920, "TB": 1.1309237,"TEN": 0.7839357,
    "WFT": 0.8867470, "BYE" : 0 
    }

#defenses
d = cp.Variable(10, boolean = True)

#top 10 defense weekly proj points
dsProj = [7.21250, 7.11875, 6.95625, 6.91250, 6.75625, 6.74375, 6.72500, 6.70625, 6.67500, 6.66875]

#dst factor for each team
dsDef = {
    "ARI": 0.8089451, "ATL": 1.5401070, "BAL": 1.2445309, "BUF": 0.6067088, "CAR": 1.2289742, "CHI": 1.3534273, "CIN": 0.9645114, "CLE": 0.8556150, "DAL": 0.7622752, "DEN": 1.2445309, 
    "DET": 1.3223140,  "GB": 0.4978123, "HOU": 1.5245503, "IND": 0.4200292,"JAC": 1.5245503, "KC": 1.0267380,  "LV": 1.1200778, "LAC": 0.6844920,"LAR": 0.9022849,
    "MIA": 1.2134176,"MIN": 0.4822557,"NE": 1.0578512, "NO": 0.9800681, "NYG": 1.1356344, "NYJ": 1.3845406,
    "PHI": 0.6533787,"PIT": 0.9022849, "SF": 0.7778318, "SEA": 1.0111813, "TB": 0.6222654,"TEN": 0.8867282,
    "WFT": 1.2600875, "BYE" : 0 
    }

obj_func = z[0]

constraints = []
#only one quarter back is chosen
constraints.append(x[0] + x[1] + x[2] + x[3]+ x[4]+ x[5]+ x[6]+ x[7]+ x[8]+ x[9] == 1)
#only one running back is chosen
constraints.append(r[0] + r[1] + r[2] + r[3]+ r[4]+ r[5]+ r[6]+ r[7]+ r[8]+ r[9] <= 2)
#only 2 wide receiver is chosen
constraints.append(w[0] + w[1] + w[2] + w[3]+ w[4]+ w[5]+ w[6]+ w[7]+ w[8]+ w[9] <= 3)
#only one tight end is chosen
constraints.append(t[0] + t[1] + t[2] + t[3]+ t[4]+ t[5]+ t[6]+ t[7]+ t[8]+ t[9] == 1)
#only one defense is chosen
constraints.append(d[0] + d[1] + d[2] + d[3]+ d[4]+ d[5]+ d[6]+ d[7]+ d[8]+ d[9] == 1)
#only 7 players total
constraints.append(x[0] + x[1] + x[2] + x[3]+ x[4]+ x[5]+ x[6]+ x[7]+ x[8]+ x[9] + r[0] + r[1] + r[2] + r[3]+ r[4]+ r[5]+ r[6]+ r[7]+ r[8]+ r[9] + w[0] + w[1] + w[2] + w[3]+ w[4]+ w[5]+ w[6]+ w[7]+ w[8]+ w[9] + t[0] + t[1] + t[2] + t[3]+ t[4]+ t[5]+ t[6]+ t[7]+ t[8]+ t[9] +d[0] + d[1] + d[2] + d[3]+ d[4]+ d[5]+ d[6]+ d[7]+ d[8]+ d[9] == 7 )

#week 1
constraints.append(z[0] <= (qbProj[0]*qbDef["PIT"]*x[0]) + (qbProj[1]*qbDef["CLE"]*x[1]) + (qbProj[2]*qbDef["TEN"]*x[2]) + (qbProj[3]*qbDef["LV"]*x[3]) + (qbProj[4]*qbDef["TB"]*x[4])+ (qbProj[5]*qbDef["IND"]*x[5]) + (qbProj[6]*qbDef["WFT"]*x[6]) + (qbProj[7]*qbDef["NO"]*x[7]) + (qbProj[8]*qbDef["DAL"]*x[8]) + (qbProj[9]*qbDef["ATL"]*x[9]) 
                         + (rbProj[0]*rbDef["NYJ"] *r[0]) +(rbProj[1]*rbDef["CIN"]*r[1]) + (rbProj[2]*rbDef["ARI"]*r[2]) + (rbProj[3]*rbDef["GB"]*r[3]) + (rbProj[4]*rbDef["NO"]*r[4]) + (rbProj[5]*rbDef["KC"]*r[5]) + (rbProj[6]*rbDef["DEN"]*r[6]) + (rbProj[7]*rbDef["SEA"]*r[7]) + (rbProj[8]*rbDef["TB"]*r[8]) + (rbProj[9]*rbDef["MIN"]*r[9]) 
                         + (wrProj[0]*wrDef["CLE"] *w[0]) +(wrProj[1]*wrDef["NO"]*w[1]) + (wrProj[2]*wrDef["PIT"]*w[2]) + (wrProj[3]*wrDef["PHI"]*w[3]) + (wrProj[4]*wrDef["CIN"]*w[4]) + (wrProj[5]*wrDef["TEN"]*w[5]) + (wrProj[6]*wrDef["IND"]*w[6]) + (wrProj[7]*wrDef["ARI"]*w[7]) + (wrProj[8]*wrDef["TB"]*w[8]) + (wrProj[9]*wrDef["TB"]*w[9])
 + (teProj[0]*teDef["CLE"] *t[0]) +(teProj[1]*teDef["BAL"]*t[1]) + (teProj[2]*teDef["DET"]*t[2]) + (teProj[3]*teDef["LV"]*t[3]) + (teProj[4]*teDef["SF"]*t[4]) + (teProj[5]*teDef["PHI"]*t[5]) + (teProj[6]*teDef["NYG"]*t[6]) + (teProj[7]*teDef["NE"]*t[7]) + (teProj[8]*teDef["NO"]*t[8]) + (teProj[9]*teDef["LAC"]*t[9])

+ (dsProj[0]*dsDef["BUF"] *d[0]) +(dsProj[1]*dsDef["CHI"]*d[1]) + (dsProj[2]*dsDef["LAC"]*d[2]) + (dsProj[3]*dsDef["SEA"]*d[3]) + (dsProj[4]*dsDef["GB"]*d[4]) + (dsProj[5]*dsDef["NO"]*d[5]) + (dsProj[6]*dsDef["TEN"]*d[6]) + (dsProj[7]*dsDef["ATL"]*d[7]) + (dsProj[8]*dsDef["LV"]*d[8]) + (dsProj[9]*dsDef["IND"]*d[9])
)
                        
                        
#week 2
constraints.append(z[0] <= (qbProj[0]*qbDef["MIA"]*x[0]) + (qbProj[1]*qbDef["BAL"]*x[1]) + (qbProj[2]*qbDef["MIN"]*x[2]) + (qbProj[3]*qbDef["KC"]*x[3]) + (qbProj[4]*qbDef["LAC"]*x[4])+ (qbProj[5]*qbDef["TEN"]*x[5]) + (qbProj[6]*qbDef["DAL"]*x[6]) + (qbProj[7]*qbDef["DET"]*x[7]) + (qbProj[8]*qbDef["ATL"]*x[8]) + (qbProj[9]*qbDef["SF"]*x[9])  
                         + (rbProj[0]*rbDef["NO"] *r[0]) +(rbProj[1]*rbDef["ARI"]*r[1]) + (rbProj[2]*rbDef["SEA"]*r[2]) + (rbProj[3]*rbDef["CAR"]*r[3]) + (rbProj[4]*rbDef["DET"]*r[4]) + (rbProj[5]*rbDef["HOU"]*r[5]) + (rbProj[6]*rbDef["WFT"]*r[6]) + (rbProj[7]*rbDef["LAR"]*r[7]) + (rbProj[8]*rbDef["LAC"]*r[8]) + (rbProj[9]*rbDef["CHI"]*r[9])
                        + (wrProj[0]*wrDef["BAL"] *w[0]) +(wrProj[1]*wrDef["DET"]*w[1]) + (wrProj[2]*wrDef["MIA"]*w[2]) + (wrProj[3]*wrDef["TB"]*w[3]) + (wrProj[4]*wrDef["ARI"]*w[4]) + (wrProj[5]*wrDef["MIN"]*w[5]) + (wrProj[6]*wrDef["TEN"]*w[6]) + (wrProj[7]*wrDef["SEA"]*w[7]) + (wrProj[8]*wrDef["LAC"]*w[8]) + (wrProj[9]*wrDef["LAC"]*w[9])
+ (teProj[0]*teDef["BAL"] *t[0]) +(teProj[1]*teDef["PIT"]*t[1]) + (teProj[2]*teDef["PHI"]*t[2]) + (teProj[3]*teDef["KC"]*t[3]) + (teProj[4]*teDef["GB"]*t[4]) + (teProj[5]*teDef["TB"]*t[5]) + (teProj[6]*teDef["JAC"]*t[6]) + (teProj[7]*teDef["BUF"]*t[7]) + (teProj[8]*teDef["DET"]*t[8]) + (teProj[9]*teDef["NYG"]*t[9])
+ (dsProj[0]*dsDef["LV"] *d[0]) +(dsProj[1]*dsDef["IND"]*d[1]) + (dsProj[2]*dsDef["NYG"]*d[2]) + (dsProj[3]*dsDef["LAR"]*d[3]) + (dsProj[4]*dsDef["CAR"]*d[4]) + (dsProj[5]*dsDef["DET"]*d[5]) + (dsProj[6]*dsDef["MIN"]*d[6]) + (dsProj[7]*dsDef["SF"]*d[7]) + (dsProj[8]*dsDef["KC"]*d[8]) + (dsProj[9]*dsDef["TEN"]*d[9]))

                     
                        
                         
#week 3
constraints.append(z[0] <= (qbProj[0]*qbDef["WFT"]*x[0]) + (qbProj[1]*qbDef["LAC"]*x[1]) + (qbProj[2]*qbDef["JAC"]*x[2]) + (qbProj[3]*qbDef["DET"]*x[3]) + (qbProj[4]*qbDef["PHI"]*x[4])+ (qbProj[5]*qbDef["MIN"]*x[5]) + (qbProj[6]*qbDef["KC"]*x[6]) + (qbProj[7]*qbDef["SF"]*x[7]) + (qbProj[8]*qbDef["LAR"]*x[8]) + (qbProj[9]*qbDef["DAL"]*x[9]) 
                         + (rbProj[0]*rbDef["HOU"] *r[0]) +(rbProj[1]*rbDef["SEA"]*r[1]) + (rbProj[2]*rbDef["IND"]*r[2]) + (rbProj[3]*rbDef["NE"]*r[3]) + (rbProj[4]*rbDef["SF"]*r[4]) + (rbProj[5]*rbDef["CHI"]*r[5]) + (rbProj[6]*rbDef["ATL"]*r[6]) + (rbProj[7]*rbDef["TEN"]*r[7]) + (rbProj[8]*rbDef["PHI"]*r[8]) + (rbProj[9]*rbDef["PIT"]*r[9])
                        + (wrProj[0]*wrDef["LAC"] *w[0]) +(wrProj[1]*wrDef["SF"]*w[1]) + (wrProj[2]*wrDef["WFT"]*w[2]) + (wrProj[3]*wrDef["NYG"]*w[3]) + (wrProj[4]*wrDef["SEA"]*w[4]) + (wrProj[5]*wrDef["JAC"]*w[5]) + (wrProj[6]*wrDef["MIN"]*w[6]) + (wrProj[7]*wrDef["IND"]*w[7]) + (wrProj[8]*wrDef["PHI"]*w[8]) + (wrProj[9]*wrDef["PHI"]*w[9])
+ (teProj[0]*teDef["LAC"] *t[0]) +(teProj[1]*teDef["MIA"]*t[1]) + (teProj[2]*teDef["GB"]*t[2]) + (teProj[3]*teDef["DET"]*t[3]) + (teProj[4]*teDef["BAL"]*t[4]) + (teProj[5]*teDef["NYG"]*t[5]) + (teProj[6]*teDef["NYJ"]*t[6]) + (teProj[7]*teDef["LV"]*t[7]) + (teProj[8]*teDef["SF"]*t[8]) + (teProj[9]*teDef["BUF"]*t[9])
+ (dsProj[0]*dsDef["CIN"] *d[0]) +(dsProj[1]*dsDef["TB"]*d[1]) + (dsProj[2]*dsDef["BUF"]*d[2]) + (dsProj[3]*dsDef["TEN"]*d[3]) + (dsProj[4]*dsDef["NE"]*d[4]) + (dsProj[5]*dsDef["SF"]*d[5]) + (dsProj[6]*dsDef["JAC"]*d[6]) + (dsProj[7]*dsDef["DAL"]*d[7]) + (dsProj[8]*dsDef["DET"]*d[8]) + (dsProj[9]*dsDef["MIN"]*d[9]))

                       
                        
                         
#week 4
constraints.append(z[0] <= (qbProj[0]*qbDef["HOU"]*x[0]) + (qbProj[1]*qbDef["PHI"]*x[1]) + (qbProj[2]*qbDef["LAR"]*x[2]) + (qbProj[3]*qbDef["DEN"]*x[3]) + (qbProj[4]*qbDef["CAR"]*x[4])+ (qbProj[5]*qbDef["SF"]*x[5]) + (qbProj[6]*qbDef["LV"]*x[6]) + (qbProj[7]*qbDef["PIT"]*x[7]) + (qbProj[8]*qbDef["NE"]*x[8]) + (qbProj[9]*qbDef["KC"]*x[9])  
                         + (rbProj[0]*rbDef["DAL"] *r[0]) +(rbProj[1]*rbDef["CLE"]*r[1]) + (rbProj[2]*rbDef["NYJ"]*r[2]) + (rbProj[3]*rbDef["NYG"]*r[3]) + (rbProj[4]*rbDef["PIT"]*r[4]) + (rbProj[5]*rbDef["MIN"]*r[5]) + (rbProj[6]*rbDef["NO"]*r[6]) + (rbProj[7]*rbDef["MIA"]*r[7]) + (rbProj[8]*rbDef["CAR"]*r[8]) + (rbProj[9]*rbDef["JAC"]*r[9]) 
                         + (wrProj[0]*wrDef["PHI"] *w[0]) +(wrProj[1]*wrDef["PIT"]*w[1]) + (wrProj[2]*wrDef["HOU"]*w[2]) + (wrProj[3]*wrDef["WFT"]*w[3]) + (wrProj[4]*wrDef["CLE"]*w[4]) + (wrProj[5]*wrDef["LAR"]*w[5]) + (wrProj[6]*wrDef["SF"]*w[6]) + (wrProj[7]*wrDef["NYJ"]*w[7]) + (wrProj[8]*wrDef["CAR"]*w[8]) + (wrProj[9]*wrDef["CAR"]*w[9])
+ (teProj[0]*teDef["PHI"] *t[0]) +(teProj[1]*teDef["LAC"]*t[1]) + (teProj[2]*teDef["SEA"]*t[2]) + (teProj[3]*teDef["DEN"]*t[3]) + (teProj[4]*teDef["CHI"]*t[4]) + (teProj[5]*teDef["WFT"]*t[5]) + (teProj[6]*teDef["BAL"]*t[6]) + (teProj[7]*teDef["IND"]*t[7]) + (teProj[8]*teDef["PIT"]*t[8]) + (teProj[9]*teDef["ATL"]*t[9])
+ (dsProj[0]*dsDef["GB"] *d[0]) +(dsProj[1]*dsDef["ARI"]*d[1]) + (dsProj[2]*dsDef["ATL"]*d[2]) + (dsProj[3]*dsDef["MIA"]*d[3]) + (dsProj[4]*dsDef["NYG"]*d[4]) + (dsProj[5]*dsDef["PIT"]*d[5]) + (dsProj[6]*dsDef["LAR"]*d[6]) + (dsProj[7]*dsDef["KC"]*d[7]) + (dsProj[8]*dsDef["DEN"]*d[8]) + (dsProj[9]*dsDef["SF"]*d[9]))

                        
                        
                        

#week 5
constraints.append(z[0] <= (qbProj[0]*qbDef["KC"]*x[0]) + (qbProj[1]*qbDef["BUF"]*x[1]) + (qbProj[2]*qbDef["SF"]*x[2]) + (qbProj[3]*qbDef["IND"]*x[3]) + (qbProj[4]*qbDef["NYG"]*x[4])+ (qbProj[5]*qbDef["LAR"]*x[5]) + (qbProj[6]*qbDef["CLE"]*x[6]) + (qbProj[7]*qbDef["CIN"]*x[7]) + (qbProj[8]*qbDef["MIA"]*x[8]) + (qbProj[9]*qbDef["CAR"]*x[9])  
                         + (rbProj[0]*rbDef["PHI"] *r[0]) +(rbProj[1]*rbDef["DET"]*r[1]) + (rbProj[2]*rbDef["JAC"]*r[2]) + (rbProj[3]*rbDef["WFT"]*r[3]) + (rbProj[4]*rbDef["CIN"]*r[4]) + (rbProj[5]*rbDef["LAC"]*r[5]) + (rbProj[6]*rbDef["DAL"]*r[6]) + (rbProj[7]*rbDef["BAL"]*r[7]) + (rbProj[8]*rbDef["NYG"]*r[8]) + (rbProj[9]*rbDef["GB"]*r[9]) 
                            + (wrProj[0]*wrDef["BUF"] *w[0]) +(wrProj[1]*wrDef["CIN"]*w[1]) + (wrProj[2]*wrDef["KC"]*w[2]) + (wrProj[3]*wrDef["NYJ"]*w[3]) + (wrProj[4]*wrDef["DET"]*w[4]) + (wrProj[5]*wrDef["SF"]*w[5]) + (wrProj[6]*wrDef["LAR"]*w[6]) + (wrProj[7]*wrDef["JAC"]*w[7]) + (wrProj[8]*wrDef["NYG"]*w[8]) + (wrProj[9]*wrDef["NYG"]*w[9])
+ (teProj[0]*teDef["BUF"] *t[0]) +(teProj[1]*teDef["CHI"]*t[1]) + (teProj[2]*teDef["ARI"]*t[2]) + (teProj[3]*teDef["IND"]*t[3]) + (teProj[4]*teDef["MIN"]*t[4]) + (teProj[5]*teDef["NYJ"]*t[5]) + (teProj[6]*teDef["PIT"]*t[6]) + (teProj[7]*teDef["TB"]*t[7]) + (teProj[8]*teDef["CIN"]*t[8]) + (teProj[9]*teDef["NO"]*t[9])
+ (dsProj[0]*dsDef["DEN"] *d[0]) +(dsProj[1]*dsDef["SEA"]*d[1]) + (dsProj[2]*dsDef["NO"]*d[2]) + (dsProj[3]*dsDef["BAL"]*d[3]) + (dsProj[4]*dsDef["WFT"]*d[4]) + (dsProj[5]*dsDef["CIN"]*d[5]) + (dsProj[6]*dsDef["SF"]*d[6]) + (dsProj[7]*dsDef["CAR"]*d[7]) + (dsProj[8]*dsDef["IND"]*d[8]) + (dsProj[9]*dsDef["LAR"]*d[9]))

                        
                         
                        
#week 6
constraints.append(z[0] <= (qbProj[0]*qbDef["TEN"]*x[0]) + (qbProj[1]*qbDef["WFT"]*x[1]) + (qbProj[2]*qbDef["CLE"]*x[2]) + (qbProj[3]*qbDef["LAC"]*x[3]) + (qbProj[4]*qbDef["NE"]*x[4])+ (qbProj[5]*qbDef["PIT"]*x[5]) + (qbProj[6]*qbDef["BAL"]*x[6]) + (qbProj[7]*qbDef["CHI"]*x[7]) + (qbProj[8]*qbDef["PHI"]*x[8]) + (qbProj[9]*qbDef["TB"]*x[9])   
                         + (rbProj[0]*rbDef["MIN"] *r[0]) +(rbProj[1]*rbDef["CAR"]*r[1]) + (rbProj[2]*rbDef["BUF"]*r[2]) + (rbProj[3]*rbDef["BYE"]*r[3]) + (rbProj[4]*rbDef["CHI"]*r[4]) + (rbProj[5]*rbDef["ARI"]*r[5]) + (rbProj[6]*rbDef["LAR"]*r[6]) + (rbProj[7]*rbDef["HOU"]*r[7]) + (rbProj[8]*rbDef["NE"]*r[8]) + (rbProj[9]*rbDef["DET"]*r[9]) 
                        + (wrProj[0]*wrDef["WFT"] *w[0]) +(wrProj[1]*wrDef["CHI"]*w[1]) + (wrProj[2]*wrDef["TEN"]*w[2]) + (wrProj[3]*wrDef["BYE"]*w[3]) + (wrProj[4]*wrDef["CAR"]*w[4]) + (wrProj[5]*wrDef["CLE"]*w[5]) + (wrProj[6]*wrDef["PIT"]*w[6]) + (wrProj[7]*wrDef["BUF"]*w[7]) + (wrProj[8]*wrDef["NE"]*w[8]) + (wrProj[9]*wrDef["NE"]*w[9])

+ (teProj[0]*teDef["WFT"] *t[0]) +(teProj[1]*teDef["DEN"]*t[1]) + (teProj[2]*teDef["BYE"]*t[2]) + (teProj[3]*teDef["LAC"]*t[3]) + (teProj[4]*teDef["CIN"]*t[4]) + (teProj[5]*teDef["BYE"]*t[5]) + (teProj[6]*teDef["LV"]*t[6]) + (teProj[7]*teDef["JAC"]*t[7]) + (teProj[8]*teDef["CHI"]*t[8]) + (teProj[9]*teDef["KC"]*t[9])
+ (dsProj[0]*dsDef["SEA"] *d[0]) +(dsProj[1]*dsDef["NYG"]*d[1]) + (dsProj[2]*dsDef["KC"]*d[2]) + (dsProj[3]*dsDef["HOU"]*d[3]) + (dsProj[4]*dsDef["BYE"]*d[4]) + (dsProj[5]*dsDef["CHI"]*d[5]) + (dsProj[6]*dsDef["CLE"]*d[6]) + (dsProj[7]*dsDef["TB"]*d[7]) + (dsProj[8]*dsDef["LAC"]*d[8]) + (dsProj[9]*dsDef["PIT"]*d[9]))
                      
                         
#week 7
constraints.append(z[0] <= (qbProj[0]*qbDef["BYE"]*x[0]) + (qbProj[1]*qbDef["TEN"]*x[1]) + (qbProj[2]*qbDef["HOU"]*x[2]) + (qbProj[3]*qbDef["CIN"]*x[3]) + (qbProj[4]*qbDef["BYE"]*x[4])+ (qbProj[5]*qbDef["NO"]*x[5]) + (qbProj[6]*qbDef["BYE"]*x[6]) + (qbProj[7]*qbDef["WFT"]*x[7]) + (qbProj[8]*qbDef["CHI"]*x[8]) + (qbProj[9]*qbDef["LV"]*x[9])   
                         + (rbProj[0]*rbDef["NYG"] *r[0]) +(rbProj[1]*rbDef["BYE"]*r[1]) + (rbProj[2]*rbDef["KC"]*r[2]) + (rbProj[3]*rbDef["SEA"]*r[3]) + (rbProj[4]*rbDef["WFT"]*r[4]) + (rbProj[5]*rbDef["DEN"]*r[5]) + (rbProj[6]*rbDef["CAR"]*r[6]) + (rbProj[7]*rbDef["SF"]*r[7]) + (rbProj[8]*rbDef["BYE"]*r[8]) + (rbProj[9]*rbDef["BAL"]*r[9]) 
                         + (wrProj[0]*wrDef["TEN"] *w[0]) +(wrProj[1]*wrDef["WFT"]*w[1]) + (wrProj[2]*wrDef["BYE"]*w[2]) + (wrProj[3]*wrDef["MIA"]*w[3]) + (wrProj[4]*wrDef["BYE"]*w[4]) + (wrProj[5]*wrDef["HOU"]*w[5]) + (wrProj[6]*wrDef["NO"]*w[6]) + (wrProj[7]*wrDef["KC"]*w[7]) + (wrProj[8]*wrDef["BYE"]*w[8]) + (wrProj[9]*wrDef["BYE"]*w[9])
+ (teProj[0]*teDef["TEN"] *t[0]) +(teProj[1]*teDef["PHI"]*t[1]) + (teProj[2]*teDef["IND"]*t[2]) + (teProj[3]*teDef["CIN"]*t[3]) + (teProj[4]*teDef["LAR"]*t[4]) + (teProj[5]*teDef["MIA"]*t[5]) + (teProj[6]*teDef["CLE"]*t[6]) + (teProj[7]*teDef["ATL"]*t[7]) + (teProj[8]*teDef["WFT"]*t[8]) + (teProj[9]*teDef["GB"]*t[9])
+ (dsProj[0]*dsDef["BYE"] *d[0]) +(dsProj[1]*dsDef["DET"]*d[1]) + (dsProj[2]*dsDef["GB"]*d[2]) + (dsProj[3]*dsDef["SF"]*d[3]) + (dsProj[4]*dsDef["SEA"]*d[4]) + (dsProj[5]*dsDef["WFT"]*d[5]) + (dsProj[6]*dsDef["HOU"]*d[6]) + (dsProj[7]*dsDef["LV"]*d[7]) + (dsProj[8]*dsDef["CIN"]*d[8]) + (dsProj[9]*dsDef["NO"]*d[9]))

                                    
  
#week 8
constraints.append(z[0] <= (qbProj[0]*qbDef["MIA"]*x[0]) + (qbProj[1]*qbDef["NYG"]*x[1]) + (qbProj[2]*qbDef["GB"]*x[2]) + (qbProj[3]*qbDef["BYE"]*x[3]) + (qbProj[4]*qbDef["MIN"]*x[4])+ (qbProj[5]*qbDef["JAC"]*x[5]) + (qbProj[6]*qbDef["NE"]*x[6]) + (qbProj[7]*qbDef["ARI"]*x[7]) + (qbProj[8]*qbDef["NO"]*x[8]) + (qbProj[9]*qbDef["DET"]*x[9])   
                         + (rbProj[0]*rbDef["ATL"] *r[0]) +(rbProj[1]*rbDef["DAL"]*r[1]) + (rbProj[2]*rbDef["IND"]*r[2]) + (rbProj[3]*rbDef["TB"]*r[3]) + (rbProj[4]*rbDef["ARI"]*r[4]) + (rbProj[5]*rbDef["PIT"]*r[5]) + (rbProj[6]*rbDef["KC"]*r[6]) + (rbProj[7]*rbDef["TEN"]*r[7]) + (rbProj[8]*rbDef["MIN"]*r[8]) + (rbProj[9]*rbDef["NYJ"]*r[9]) 
                         + (wrProj[0]*wrDef["NYG"] *w[0]) +(wrProj[1]*wrDef["ARI"]*w[1]) + (wrProj[2]*wrDef["MIA"]*w[2]) + (wrProj[3]*wrDef["CAR"]*w[3]) + (wrProj[4]*wrDef["DAL"]*w[4]) + (wrProj[5]*wrDef["GB"]*w[5]) + (wrProj[6]*wrDef["JAC"]*w[6]) + (wrProj[7]*wrDef["IND"]*w[7]) + (wrProj[8]*wrDef["MIN"]*w[8]) + (wrProj[9]*wrDef["MIN"]*w[9])
+ (teProj[0]*teDef["NYG"] *t[0]) +(teProj[1]*teDef["BYE"]*t[1]) + (teProj[2]*teDef["CHI"]*t[2]) + (teProj[3]*teDef["BYE"]*t[3]) + (teProj[4]*teDef["PHI"]*t[4]) + (teProj[5]*teDef["CAR"]*t[5]) + (teProj[6]*teDef["WFT"]*t[6]) + (teProj[7]*teDef["BUF"]*t[7]) + (teProj[8]*teDef["ARI"]*t[8]) + (teProj[9]*teDef["DEN"]*t[9])
+ (dsProj[0]*dsDef["CLE"] *d[0]) +(dsProj[1]*dsDef["HOU"]*d[1]) + (dsProj[2]*dsDef["DEN"]*d[2]) + (dsProj[3]*dsDef["TEN"]*d[3]) + (dsProj[4]*dsDef["TB"]*d[4]) + (dsProj[5]*dsDef["ARI"]*d[5]) + (dsProj[6]*dsDef["GB"]*d[6]) + (dsProj[7]*dsDef["DET"]*d[7]) + (dsProj[8]*dsDef["BYE"]*d[8]) + (dsProj[9]*dsDef["JAC"]*d[9]))

                        
                        
#week 9
constraints.append(z[0] <= (qbProj[0]*qbDef["JAC"]*x[0]) + (qbProj[1]*qbDef["GB"]*x[1]) + (qbProj[2]*qbDef["SF"]*x[2]) + (qbProj[3]*qbDef["MIN"]*x[3]) + (qbProj[4]*qbDef["DEN"]*x[4])+ (qbProj[5]*qbDef["BYE"]*x[5]) + (qbProj[6]*qbDef["PHI"]*x[6]) + (qbProj[7]*qbDef["KC"]*x[7]) + (qbProj[8]*qbDef["BYE"]*x[8]) + (qbProj[9]*qbDef["LAC"]*x[9])   
                         + (rbProj[0]*rbDef["NE"] *r[0]) +(rbProj[1]*rbDef["BAL"]*r[1]) + (rbProj[2]*rbDef["LAR"]*r[2]) + (rbProj[3]*rbDef["ATL"]*r[3]) + (rbProj[4]*rbDef["KC"]*r[4]) + (rbProj[5]*rbDef["CIN"]*r[5]) + (rbProj[6]*rbDef["LV"]*r[6]) + (rbProj[7]*rbDef["NYJ"]*r[7]) + (rbProj[8]*rbDef["DEN"]*r[8]) + (rbProj[9]*rbDef["CLE"]*r[9]) 
                         + (wrProj[0]*wrDef["GB"] *w[0]) +(wrProj[1]*wrDef["KC"]*w[1]) + (wrProj[2]*wrDef["JAC"]*w[2]) + (wrProj[3]*wrDef["NO"]*w[3]) + (wrProj[4]*wrDef["BAL"]*w[4]) + (wrProj[5]*wrDef["SF"]*w[5]) + (wrProj[6]*wrDef["BYE"]*w[6]) + (wrProj[7]*wrDef["LAR"]*w[7]) + (wrProj[8]*wrDef["DEN"]*w[8]) + (wrProj[9]*wrDef["DEN"]*w[9])
+ (teProj[0]*teDef["GB"] *t[0]) +(teProj[1]*teDef["NYG"]*t[1]) + (teProj[2]*teDef["ARI"]*t[2]) + (teProj[3]*teDef["MIN"]*t[3]) + (teProj[4]*teDef["BYE"]*t[4]) + (teProj[5]*teDef["NO"]*t[5]) + (teProj[6]*teDef["DAL"]*t[6]) + (teProj[7]*teDef["HOU"]*t[7]) + (teProj[8]*teDef["KC"]*t[8]) + (teProj[9]*teDef["BYE"]*t[9])
+ (dsProj[0]*dsDef["CHI"] *d[0]) +(dsProj[1]*dsDef["TEN"]*d[1]) + (dsProj[2]*dsDef["BYE"]*d[2]) + (dsProj[3]*dsDef["NYJ"]*d[3]) + (dsProj[4]*dsDef["ATL"]*d[4]) + (dsProj[5]*dsDef["KC"]*d[5]) + (dsProj[6]*dsDef["SF"]*d[6]) + (dsProj[7]*dsDef["LAC"]*d[7]) + (dsProj[8]*dsDef["MIN"]*d[8]) + (dsProj[9]*dsDef["BYE"]*d[9]))

                        

#week 10
constraints.append(z[0] <= (qbProj[0]*qbDef["NYJ"]*x[0]) + (qbProj[1]*qbDef["LV"]*x[1]) + (qbProj[2]*qbDef["CAR"]*x[2]) + (qbProj[3]*qbDef["MIA"]*x[3]) + (qbProj[4]*qbDef["ATL"]*x[4])+ (qbProj[5]*qbDef["GB"]*x[5]) + (qbProj[6]*qbDef["MIN"]*x[6]) + (qbProj[7]*qbDef["SEA"]*x[7]) + (qbProj[8]*qbDef["WFT"]*x[8]) + (qbProj[9]*qbDef["DEN"]*x[9])  
                         + (rbProj[0]*rbDef["ARI"] *r[0]) +(rbProj[1]*rbDef["LAC"]*r[1]) + (rbProj[2]*rbDef["NO"]*r[2]) + (rbProj[3]*rbDef["TEN"]*r[3]) + (rbProj[4]*rbDef["SEA"]*r[4]) + (rbProj[5]*rbDef["NE"]*r[5]) + (rbProj[6]*rbDef["BYE"]*r[6]) + (rbProj[7]*rbDef["JAC"]*r[7]) + (rbProj[8]*rbDef["ATL"]*r[8]) + (rbProj[9]*rbDef["BYE"]*r[9])   
                         + (wrProj[0]*wrDef["LV"] *w[0]) +(wrProj[1]*wrDef["SEA"]*w[1]) + (wrProj[2]*wrDef["NYJ"]*w[2]) + (wrProj[3]*wrDef["DAL"]*w[3]) + (wrProj[4]*wrDef["LAC"]*w[4]) + (wrProj[5]*wrDef["CAR"]*w[5]) + (wrProj[6]*wrDef["GB"]*w[6]) + (wrProj[7]*wrDef["NO"]*w[7]) + (wrProj[8]*wrDef["ATL"]*w[8]) + (wrProj[9]*wrDef["ATL"]*w[9])
+ (teProj[0]*teDef["LV"] *t[0]) +(teProj[1]*teDef["KC"]*t[1]) + (teProj[2]*teDef["LAR"]*t[2]) + (teProj[3]*teDef["MIA"]*t[3]) + (teProj[4]*teDef["PIT"]*t[4]) + (teProj[5]*teDef["DAL"]*t[5]) + (teProj[6]*teDef["PHI"]*t[6]) + (teProj[7]*teDef["BAL"]*t[7]) + (teProj[8]*teDef["SEA"]*t[8]) + (teProj[9]*teDef["TB"]*t[9])
+ (dsProj[0]*dsDef["DET"] *d[0]) +(dsProj[1]*dsDef["SF"]*d[1]) + (dsProj[2]*dsDef["TB"]*d[2]) + (dsProj[3]*dsDef["JAC"]*d[3]) + (dsProj[4]*dsDef["TEN"]*d[4]) + (dsProj[5]*dsDef["SEA"]*d[5]) + (dsProj[6]*dsDef["CAR"]*d[6]) + (dsProj[7]*dsDef["DEN"]*d[7]) + (dsProj[8]*dsDef["MIA"]*d[8]) + (dsProj[9]*dsDef["GB"]*d[9]))

                        

#week 11
constraints.append(z[0] <= (qbProj[0]*qbDef["IND"]*x[0]) + (qbProj[1]*qbDef["DAL"]*x[1]) + (qbProj[2]*qbDef["SEA"]*x[2]) + (qbProj[3]*qbDef["CHI"]*x[3]) + (qbProj[4]*qbDef["KC"]*x[4])+ (qbProj[5]*qbDef["ARI"]*x[5]) + (qbProj[6]*qbDef["PIT"]*x[6]) + (qbProj[7]*qbDef["MIN"]*x[7]) + (qbProj[8]*qbDef["NYG"]*x[8]) + (qbProj[9]*qbDef["NO"]*x[9])  
                         + (rbProj[0]*rbDef["WFT"] *r[0]) +(rbProj[1]*rbDef["GB"]*r[1]) + (rbProj[2]*rbDef["HOU"]*r[2]) + (rbProj[3]*rbDef["PHI"]*r[3]) + (rbProj[4]*rbDef["MIN"]*r[4]) + (rbProj[5]*rbDef["DET"]*r[5]) + (rbProj[6]*rbDef["TB"]*r[6]) + (rbProj[7]*rbDef["BUF"]*r[7]) + (rbProj[8]*rbDef["KC"]*r[8]) + (rbProj[9]*rbDef["LV"]*r[9])    
                         + (wrProj[0]*wrDef["DAL"] *w[0]) +(wrProj[1]*wrDef["MIN"]*w[1]) + (wrProj[2]*wrDef["IND"]*w[2]) + (wrProj[3]*wrDef["NE"]*w[3]) + (wrProj[4]*wrDef["GB"]*w[4]) + (wrProj[5]*wrDef["SEA"]*w[5]) + (wrProj[6]*wrDef["ARI"]*w[6]) + (wrProj[7]*wrDef["HOU"]*w[7]) + (wrProj[8]*wrDef["KC"]*w[8]) + (wrProj[9]*wrDef["KC"]*w[9])
+ (teProj[0]*teDef["DAL"] *t[0]) +(teProj[1]*teDef["CIN"]*t[1]) + (teProj[2]*teDef["JAC"]*t[2]) + (teProj[3]*teDef["CHI"]*t[3]) + (teProj[4]*teDef["CLE"]*t[4]) + (teProj[5]*teDef["NE"]*t[5]) + (teProj[6]*teDef["BYE"]*t[6]) + (teProj[7]*teDef["NYJ"]*t[7]) + (teProj[8]*teDef["MIN"]*t[8]) + (teProj[9]*teDef["CAR"]*t[9])
+ (dsProj[0]*dsDef["LAC"] *d[0]) +(dsProj[1]*dsDef["BYE"]*d[1]) + (dsProj[2]*dsDef["CAR"]*d[2]) + (dsProj[3]*dsDef["BUF"]*d[3]) + (dsProj[4]*dsDef["PHI"]*d[4]) + (dsProj[5]*dsDef["MIN"]*d[5]) + (dsProj[6]*dsDef["SEA"]*d[6]) + (dsProj[7]*dsDef["NO"]*d[7]) + (dsProj[8]*dsDef["CHI"]*d[8]) + (dsProj[9]*dsDef["ARI"]*d[9]))

                         

#week 12
constraints.append(z[0] <= (qbProj[0]*qbDef["NO"]*x[0]) + (qbProj[1]*qbDef["BYE"]*x[1]) + (qbProj[2]*qbDef["BYE"]*x[2]) + (qbProj[3]*qbDef["CLE"]*x[3]) + (qbProj[4]*qbDef["LV"]*x[4])+ (qbProj[5]*qbDef["WFT"]*x[5]) + (qbProj[6]*qbDef["DEN"]*x[6]) + (qbProj[7]*qbDef["LAR"]*x[7]) + (qbProj[8]*qbDef["IND"]*x[8]) + (qbProj[9]*qbDef["NYG"]*x[9])  
                         + (rbProj[0]*rbDef["MIA"] *r[0]) +(rbProj[1]*rbDef["SF"]*r[1]) + (rbProj[2]*rbDef["NE"]*r[2]) + (rbProj[3]*rbDef["BUF"]*r[3]) + (rbProj[4]*rbDef["LAR"]*r[4]) + (rbProj[5]*rbDef["BAL"]*r[5]) + (rbProj[6]*rbDef["PHI"]*r[6]) + (rbProj[7]*rbDef["TB"]*r[7]) + (rbProj[8]*rbDef["LV"]*r[8]) + (rbProj[9]*rbDef["PIT"]*r[9])   
                         + (wrProj[0]*wrDef["BYE"] *w[0]) +(wrProj[1]*wrDef["LAR"]*w[1]) + (wrProj[2]*wrDef["NO"]*w[2]) + (wrProj[3]*wrDef["JAC"]*w[3]) + (wrProj[4]*wrDef["SF"]*w[4]) + (wrProj[5]*wrDef["BYE"]*w[5]) + (wrProj[6]*wrDef["WFT"]*w[6]) + (wrProj[7]*wrDef["NE"]*w[7]) + (wrProj[8]*wrDef["LV"]*w[8]) + (wrProj[9]*wrDef["LV"]*w[9])
+ (teProj[0]*teDef["BYE"] *t[0]) +(teProj[1]*teDef["DAL"]*t[1]) + (teProj[2]*teDef["MIN"]*t[2]) + (teProj[3]*teDef["CLE"]*t[3]) + (teProj[4]*teDef["CHI"]*t[4]) + (teProj[5]*teDef["JAC"]*t[5]) + (teProj[6]*teDef["LAC"]*t[6]) + (teProj[7]*teDef["CAR"]*t[7]) + (teProj[8]*teDef["LAR"]*t[8]) + (teProj[9]*teDef["SEA"]*t[9])
 + (dsProj[0]*dsDef["CIN"] *d[0]) +(dsProj[1]*dsDef["GB"]*d[1]) + (dsProj[2]*dsDef["SEA"]*d[2]) + (dsProj[3]*dsDef["TB"]*d[3]) + (dsProj[4]*dsDef["BUF"]*d[4]) + (dsProj[5]*dsDef["LAR"]*d[5]) + (dsProj[6]*dsDef["BYE"]*d[6]) + (dsProj[7]*dsDef["NYG"]*d[7]) + (dsProj[8]*dsDef["CLE"]*d[8]) + (dsProj[9]*dsDef["WFT"]*d[9]))

                        

#week 13
constraints.append(z[0] <= (qbProj[0]*qbDef["NE"]*x[0]) + (qbProj[1]*qbDef["DEN"]*x[1]) + (qbProj[2]*qbDef["CHI"]*x[2]) + (qbProj[3]*qbDef["PIT"]*x[3]) + (qbProj[4]*qbDef["NO"]*x[4])+ (qbProj[5]*qbDef["SF"]*x[5]) + (qbProj[6]*qbDef["CIN"]*x[6]) + (qbProj[7]*qbDef["BYE"]*x[7]) + (qbProj[8]*qbDef["ATL"]*x[8]) + (qbProj[9]*qbDef["NYJ"]*x[9])   
                   + (rbProj[0]*rbDef["BYE"] *r[0]) +(rbProj[1]*rbDef["DET"]*r[1]) + (rbProj[2]*rbDef["BYE"]*r[2]) + (rbProj[3]*rbDef["DAL"]*r[3]) + (rbProj[4]*rbDef["BYE"]*r[4]) + (rbProj[5]*rbDef["BYE"]*r[5]) + (rbProj[6]*rbDef["MIA"]*r[6]) + (rbProj[7]*rbDef["HOU"]*r[7]) + (rbProj[8]*rbDef["NO"]*r[8]) + (rbProj[9]*rbDef["LAC"]*r[9])    
                   + (wrProj[0]*wrDef["DEN"] *w[0]) +(wrProj[1]*wrDef["BYE"]*w[1]) + (wrProj[2]*wrDef["NE"]*w[2]) + (wrProj[3]*wrDef["TB"]*w[3]) + (wrProj[4]*wrDef["DET"]*w[4]) + (wrProj[5]*wrDef["CHI"]*w[5]) + (wrProj[6]*wrDef["SF"]*w[6]) + (wrProj[7]*wrDef["BYE"]*w[7]) + (wrProj[8]*wrDef["NO"]*w[8]) + (wrProj[9]*wrDef["NO"]*w[9])
+ (teProj[0]*teDef["DEN"] *t[0]) +(teProj[1]*teDef["WFT"]*t[1]) + (teProj[2]*teDef["SEA"]*t[2]) + (teProj[3]*teDef["PIT"]*t[3]) + (teProj[4]*teDef["MIN"]*t[4]) + (teProj[5]*teDef["TB"]*t[5]) + (teProj[6]*teDef["KC"]*t[6]) + (teProj[7]*teDef["NYG"]*t[7]) + (teProj[8]*teDef["BYE"]*t[8]) + (teProj[9]*teDef["LV"]*t[9])
+ (dsProj[0]*dsDef["BAL"] *d[0]) +(dsProj[1]*dsDef["JAC"]*d[1]) + (dsProj[2]*dsDef["LV"]*d[2]) + (dsProj[3]*dsDef["HOU"]*d[3]) + (dsProj[4]*dsDef["DAL"]*d[4]) + (dsProj[5]*dsDef["BYE"]*d[5]) + (dsProj[6]*dsDef["CHI"]*d[6]) + (dsProj[7]*dsDef["NYJ"]*d[7]) + (dsProj[8]*dsDef["PIT"]*d[8]) + (dsProj[9]*dsDef["SF"]*d[9]))

                         

#week 14
constraints.append(z[0] <= (qbProj[0]*qbDef["TB"]*x[0]) + (qbProj[1]*qbDef["LV"]*x[1]) + (qbProj[2]*qbDef["LAR"]*x[2]) + (qbProj[3]*qbDef["CLE"]*x[3]) + (qbProj[4]*qbDef["WFT"]*x[4])+ (qbProj[5]*qbDef["HOU"]*x[5]) + (qbProj[6]*qbDef["NYG"]*x[6]) + (qbProj[7]*qbDef["CHI"]*x[7]) + (qbProj[8]*qbDef["BUF"]*x[8]) + (qbProj[9]*qbDef["BYE"]*x[9])   
                   + (rbProj[0]*rbDef["ATL"] *r[0]) +(rbProj[1]*rbDef["PIT"]*r[1]) + (rbProj[2]*rbDef["JAC"]*r[2]) + (rbProj[3]*rbDef["NYJ"]*r[3]) + (rbProj[4]*rbDef["CHI"]*r[4]) + (rbProj[5]*rbDef["BAL"]*r[5]) + (rbProj[6]*rbDef["LAC"]*r[6]) + (rbProj[7]*rbDef["BYE"]*r[7]) + (rbProj[8]*rbDef["WFT"]*r[8]) + (rbProj[9]*rbDef["SF"]*r[9])  
                   + (wrProj[0]*wrDef["LV"] *w[0]) +(wrProj[1]*wrDef["CHI"]*w[1]) + (wrProj[2]*wrDef["TB"]*w[2]) + (wrProj[3]*wrDef["CAR"]*w[3]) + (wrProj[4]*wrDef["PIT"]*w[4]) + (wrProj[5]*wrDef["LAR"]*w[5]) + (wrProj[6]*wrDef["HOU"]*w[6]) + (wrProj[7]*wrDef["JAC"]*w[7]) + (wrProj[8]*wrDef["WFT"]*w[8]) + (wrProj[9]*wrDef["WFT"]*w[9])
+ (teProj[0]*teDef["LV"] *t[0]) +(teProj[1]*teDef["KC"]*t[1]) + (teProj[2]*teDef["CIN"]*t[2]) + (teProj[3]*teDef["CLE"]*t[3]) + (teProj[4]*teDef["DEN"]*t[4]) + (teProj[5]*teDef["CAR"]*t[5]) + (teProj[6]*teDef["DET"]*t[6]) + (teProj[7]*teDef["BYE"]*t[7]) + (teProj[8]*teDef["CHI"]*t[8]) + (teProj[9]*teDef["DAL"]*t[9])
+ (dsProj[0]*dsDef["MIN"] *d[0]) +(dsProj[1]*dsDef["ARI"]*d[1]) + (dsProj[2]*dsDef["DAL"]*d[2]) + (dsProj[3]*dsDef["BYE"]*d[3]) + (dsProj[4]*dsDef["NYJ"]*d[4]) + (dsProj[5]*dsDef["CHI"]*d[5]) + (dsProj[6]*dsDef["LAR"]*d[6]) + (dsProj[7]*dsDef["BYE"]*d[7]) + (dsProj[8]*dsDef["CLE"]*d[8]) + (dsProj[9]*dsDef["HOU"]*d[9]))

                        

#week 15
constraints.append(z[0] <= (qbProj[0]*qbDef["CAR"]*x[0]) + (qbProj[1]*qbDef["LAC"]*x[1]) + (qbProj[2]*qbDef["DET"]*x[2]) + (qbProj[3]*qbDef["GB"]*x[3]) + (qbProj[4]*qbDef["NYG"]*x[4])+ (qbProj[5]*qbDef["LAR"]*x[5]) + (qbProj[6]*qbDef["KC"]*x[6]) + (qbProj[7]*qbDef["BAL"]*x[7]) + (qbProj[8]*qbDef["NO"]*x[8]) + (qbProj[9]*qbDef["WFT"]*x[9])  
                   + (rbProj[0]*rbDef["BUF"] *r[0]) +(rbProj[1]*rbDef["CHI"]*r[1]) + (rbProj[2]*rbDef["PIT"]*r[2]) + (rbProj[3]*rbDef["TB"]*r[3]) + (rbProj[4]*rbDef["BAL"]*r[4]) + (rbProj[5]*rbDef["LV"]*r[5]) + (rbProj[6]*rbDef["DAL"]*r[6]) + (rbProj[7]*rbDef["NE"]*r[7]) + (rbProj[8]*rbDef["NYG"]*r[8]) + (rbProj[9]*rbDef["DEN"]*r[9])  
                   + (wrProj[0]*wrDef["LAC"] *w[0]) +(wrProj[1]*wrDef["BAL"]*w[1]) + (wrProj[2]*wrDef["CAR"]*w[2]) + (wrProj[3]*wrDef["SF"]*w[3]) + (wrProj[4]*wrDef["CHI"]*w[4]) + (wrProj[5]*wrDef["DET"]*w[5]) + (wrProj[6]*wrDef["LAR"]*w[6]) + (wrProj[7]*wrDef["PIT"]*w[7]) + (wrProj[8]*wrDef["NYG"]*w[8]) + (wrProj[9]*wrDef["NYG"]*w[9])
+ (teProj[0]*teDef["LAC"] *t[0]) +(teProj[1]*teDef["CLE"]*t[1]) + (teProj[2]*teDef["ATL"]*t[2]) + (teProj[3]*teDef["GB"]*t[3]) + (teProj[4]*teDef["ARI"]*t[4]) + (teProj[5]*teDef["SF"]*t[5]) + (teProj[6]*teDef["CIN"]*t[6]) + (teProj[7]*teDef["NYJ"]*t[7]) + (teProj[8]*teDef["BAL"]*t[8]) + (teProj[9]*teDef["PHI"]*t[9])
+ (dsProj[0]*dsDef["TEN"] *d[0]) +(dsProj[1]*dsDef["SEA"]*d[1]) + (dsProj[2]*dsDef["PHI"]*d[2]) + (dsProj[3]*dsDef["NE"]*d[3]) + (dsProj[4]*dsDef["TB"]*d[4]) + (dsProj[5]*dsDef["BAL"]*d[5]) + (dsProj[6]*dsDef["DET"]*d[6]) + (dsProj[7]*dsDef["WFT"]*d[7]) + (dsProj[8]*dsDef["GB"]*d[8]) + (dsProj[9]*dsDef["LAR"]*d[9]))

                        

#week 16
constraints.append(z[0] <= (qbProj[0]*qbDef["NE"]*x[0]) + (qbProj[1]*qbDef["PIT"]*x[1]) + (qbProj[2]*qbDef["IND"]*x[2]) + (qbProj[3]*qbDef["CIN"]*x[3]) + (qbProj[4]*qbDef["WFT"]*x[4])+ (qbProj[5]*qbDef["CHI"]*x[5]) + (qbProj[6]*qbDef["HOU"]*x[6]) + (qbProj[7]*qbDef["CLE"]*x[7]) + (qbProj[8]*qbDef["CAR"]*x[8]) + (qbProj[9]*qbDef["NYG"]*x[9])  
                   + (rbProj[0]*rbDef["TB"] *r[0]) +(rbProj[1]*rbDef["LAR"]*r[1]) + (rbProj[2]*rbDef["SF"]*r[2]) + (rbProj[3]*rbDef["MIA"]*r[3]) + (rbProj[4]*rbDef["CLE"]*r[4]) + (rbProj[5]*rbDef["GB"]*r[5]) + (rbProj[6]*rbDef["PHI"]*r[6]) + (rbProj[7]*rbDef["ARI"]*r[7]) + (rbProj[8]*rbDef["WFT"]*r[8]) + (rbProj[9]*rbDef["BAL"]*r[9])    
                   + (wrProj[0]*wrDef["PIT"] *w[0]) +(wrProj[1]*wrDef["CLE"]*w[1]) + (wrProj[2]*wrDef["NE"]*w[2]) + (wrProj[3]*wrDef["DET"]*w[3]) + (wrProj[4]*wrDef["LAR"]*w[4]) + (wrProj[5]*wrDef["IND"]*w[5]) + (wrProj[6]*wrDef["CHI"]*w[6]) + (wrProj[7]*wrDef["SF"]*w[7]) + (wrProj[8]*wrDef["WFT"]*w[8]) + (wrProj[9]*wrDef["WFT"]*w[9])
+ (teProj[0]*teDef["PIT"] *t[0]) +(teProj[1]*teDef["DEN"]*t[1]) + (teProj[2]*teDef["TEN"]*t[2]) + (teProj[3]*teDef["CIN"]*t[3]) + (teProj[4]*teDef["ATL"]*t[4]) + (teProj[5]*teDef["DET"]*t[5]) + (teProj[6]*teDef["LV"]*t[6]) + (teProj[7]*teDef["NO"]*t[7]) + (teProj[8]*teDef["CLE"]*t[8]) + (teProj[9]*teDef["DAL"]*t[9])
+ (dsProj[0]*dsDef["KC"] *d[0]) +(dsProj[1]*dsDef["MIN"]*d[1]) + (dsProj[2]*dsDef["DAL"]*d[2]) + (dsProj[3]*dsDef["ARI"]*d[3]) + (dsProj[4]*dsDef["MIA"]*d[4]) + (dsProj[5]*dsDef["CLE"]*d[5]) + (dsProj[6]*dsDef["IND"]*d[6]) + (dsProj[7]*dsDef["NYG"]*d[7]) + (dsProj[8]*dsDef["CIN"]*d[8]) + (dsProj[9]*dsDef["CHI"]*d[9]))

                         
                     
                       

problem = cp.Problem(cp.Maximize(obj_func),constraints)
#maximize
problem.solve(solver=cp.GUROBI, verbose=True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print("r =")
print(r.value)
print("w =")
print(w.value)
print("t =")
print(t.value)
print("d =")
print(d.value)

#qb Russell Wilson SEA 5
#rb1 Dalvin Cook MIN 1
#rb2 Jonathon Taylor IND 7
#wr1 Davante Adams GB 1
#wr2 Calvin Ridley ATL 3
#te Travis Kelce KC 0
#d Colts IND 3

#week 14 with selected team
            #SEA                      MIN                       IND                  GB                          ATL                        KC                   IND
print(qbProj[5]*qbDef["HOU"] + rbProj[1]*rbDef["PIT"] + rbProj[7]*rbDef["BYE"] + wrProj[1]*wrDef["CHI"] + wrProj[3]*wrDef["CAR"] + teProj[0]*teDef["LV"] + dsProj[3]*dsDef["BYE"])

#wk 13 (LOWEST WEEK)
print(qbProj[5]*qbDef["SF"] + rbProj[1]*rbDef["DET"] + rbProj[7]*rbDef["HOU"] + wrProj[1]*wrDef["BYE"] + wrProj[3]*wrDef["TB"] + teProj[0]*teDef["DEN"] + dsProj[3]*dsDef["HOU"])























