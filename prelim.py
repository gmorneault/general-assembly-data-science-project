# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 20:30:20 2014

@author: gmorneault
"""

import os
import math
import pandas as pd

os.chdir('C:\Users\gmorneault\Documents\Data\Lending Club')

loanStats = pd.DataFrame()
loanStats = pd.read_csv('LoanStats3a.csv', skiprows=1)

loanStats.head()
loanStats.shape
loanStats.describe()
loanStats['mort_acc'][0] == nan


len([stat for stat in loanStats['num_sats'] if not math.isnan(stat)])
len([stat for stat in loanStats['num_sats'] if not math.isnan(stat)])