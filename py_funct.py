# =============================================================================================================================================
#
# AUTHOR: TMM
# DATE: June 2024
# PROJECT: Mine Seline Level 8 and 9 study 
# PURPOSE: This scrip is to define the histories and set up pyhton call backs 
# 
# =============================================================================================================================================
#                                                    IMPORTED MODULES
# =============================================================================================================================================
import itasca as it
import sys
import time
import numpy as np
import pandas as pd
# =============================================================================================================================================
#                                                    fUNCTIONS 
# =============================================================================================================================================

def ModelSize():
    zc = it.zone.count()/1e6
    gpc = it.gridpoint.count()/1e6
    it.command('''
    ;Number of zones: {} million 
    ;Number of Gridpoints: {} million
    '''.format(zc,gpc))
i = 0
def ModelMonitoring():
    global i 
    i+=1
 # creating the first plot and frame
    with open('Monitoring\\Modelmonitoring.txt','a') as f:
        x1 = str(i)
        y1 = str(it.zone.count()/1e6)
        x1_y1 = x1+','+y1+'\n'
        f.write(x1_y1)
        f.close()

def MechMonitoring():
     with open('Monitoring\\MechMonitoring.txt','a') as f:
            x1 = str(it.cycle())
            y1 = str(it.zone.unbal())
            y2 = str(it.zone.creep_timestep())
            y3 = str(it.zone.mech_ratio())
            y4 = str(it.zone.creep_time_total())
            line = x1+','+y1+','+y2+','+y3+','+y4+'\n'
            f.write(line)
            f.close()
            
ModelMonitoring()
MechMonitoring()
# =============================================================================================================================================
#                                                    SET CALLBACKS
# =============================================================================================================================================
## Cycle number for callback timing 

# -10	 Validate the data structures
# 0	     Determine a stable timestep
# 10	 Equations of motion (or thermal bodies update)
# 15	 Body coupling between processes
# 20	 Increment time
# 30	 Update the cell space
# 35	 Create/delete contacts
# 40	 Force-Displacement law (or thermal contact update)
# 42	 Accumulate deterministic quantities
# 45	 Contact coupling between processes
# 60	 Second pass of equations of motion
# 70	 Thermal calculations
# 80	 Fluid calculations
# =============================================================================================================================================
it.remove_callback('MechMonitoring',-11)
it.set_callback('MechMonitoring',-11)






    

