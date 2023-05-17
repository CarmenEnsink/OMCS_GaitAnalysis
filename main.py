# -*- coding: utf-8 -*-
"""
Main script to read and analyse optical motion capture data (VICON based)
Possibility to include analog (forceplate) data

Version - Author:
    17-05-2023: C.J. Ensink - c.ensink@maartenskliniek.nl
"""

# Import dependencies
from readmarkerdata import readmarkerdata
from eventdetection import eventdetection
from gaitcharacteristics import gaitcharacteristicsGRAIL, gaitcharacteristicsOverground, propulsion

# Example GRAIL (treadmill) trial
# Set datapath
datapath = 'data/exampleGRAIL.c3d'
markerdata, fs_markerdata, analogdata = readmarkerdata(datapath, analogdata=True)
gait_events = eventdetection(markerdata, fs_markerdata, algorithmtype='velocity', trialtype='treadmill', debugplot=True)
spatiotemporals = gaitcharacteristicsGRAIL(markerdata, gait_events, fs_markerdata)
# In case propulsion is of interest; bodyweight is needed
bodyweight = 67 # In kg
trial = datapath # For title above debugplot
gait_events, spatiotemporals, analogdata = propulsion(gait_events, spatiotemporals, analogdata, bodyweight, debugplot=True, trial=trial)



# Example overground trial
datapath = 'data/exampleOverground.c3d'
markerdata, fs_markerdata, analogdata = readmarkerdata(datapath, analogdata=True)
gait_events = eventdetection(markerdata, fs_markerdata, algorithmtype='velocity', trialtype='overground', debugplot=True)
spatiotemporals = gaitcharacteristicsOverground(markerdata, gait_events, fs_markerdata)
