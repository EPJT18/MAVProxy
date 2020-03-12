'''Custom'''

import time, os

from MAVProxy.modules.lib import mp_module
from pymavlink import mavutil
import sys, traceback

class SwoopModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(SwoopModule, self).__init__(mpstate, "Swoop", "Swoop module")
        '''initialisation code'''

    def mavlink_packet(self, m):
        'handle a mavlink packet'''

        if m.get_type() == 'SWOOP_FLAGS':
           
	        print ('armingFlags: %f' %  m.armingFlags)

            

def init(mpstate):
    '''initialise module'''
    return SwoopModule(mpstate)
