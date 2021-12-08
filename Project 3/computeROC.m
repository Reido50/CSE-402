genuine = table2array(readtable("genuine.csv"));
imposter = table2array(readtable("imposter.csv"));
drawROC(genuine, imposter, 'd')
