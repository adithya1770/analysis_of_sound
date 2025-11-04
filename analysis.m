data = readtable("data3.csv")
clc
med_val = median(data.Distance_m_);
mod_val = mode(data.Distance_m_);
avg = mean(data.Distance_m_)
