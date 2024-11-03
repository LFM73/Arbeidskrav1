#!/usr/bin/env python
# coding: utf-8

# <h2> Utgifter uansett bil <h2/>

# In[216]:


KM = 10000  # Kilometer pr år
TFA = 8.38  # Trafikkforsikringsavgift pr dag
TFA_aa = TFA * 365  #Trafikkforsikringsavgift pr år


# <h2> Utgifter El-bil <h2/>
# 
# 

# In[218]:


F_EL = 5000  # Forsikring El-bil pr år
FORBRUK_EL_KM = 0.2  # Forbruk Drivstoff El-bil kWh/km
KR_KWH = 2  # Strømpris Kr/kWh
KR_KWH_KM = FORBRUK_EL_KM * KR_KWH  # Strømpris pr km
BAVG_EL = 0.1 * KM  # Bomavgift pr år
KOST_EL = F_EL + BAVG_EL + (KR_KWH_KM * KM) + TFA_aa  # Sammenlagt utgifter for EL-bil pr år


# <h2> Utgifter Bensin-bil <h2/>

# In[220]:


F_BB = 7500  # Forsikring Bensinbil pr år
DS_BB = 1  # Drivstoff Bensinbil kr/km
DS_BB_Total = DS_BB * KM  # Totalt driftstoffutgifter for bensinbil pr år
BAVG_BB = 0.3 * KM  # Bomavgift bensinbil pr år
KOST_BB = F_BB + DS_BB_Total + BAVG_BB + TFA_aa  # Sammenlagt utgifter for bensinbil pr år


# <h2> Årlige utgifter EL- og bensinbil og differanse<h2/>

# In[222]:


DIFF = KOST_BB - KOST_EL  # Differanse årlig utgift bensinbil vs. EL-bil

print ('Årlig utgifter EL-bil =', KOST_EL) 
print ('Årlig utgifter bensinbil =', KOST_BB)
print ('Differanse EL-bil vs. Bensinbil =', DIFF)

