'''Custom'''

import time, os

from MAVProxy.modules.lib import mp_module
from pymavlink import mavutil
import sys, traceback
from datetime import datetime

class SwoopModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(SwoopModule, self).__init__(mpstate, "Swoop", "Swoop module")
        '''initialisation code'''

    def mavlink_packet(self, m):
        'handle a mavlink packet'''

        if m.get_type() == 'SWOOP_INFLIGHT_FLAGS_INSTANT':
            if(m.inflightFlags>0):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)
                print( 'Inflight flags  ' + str(m.inflightFlags))
            if(m.maximumIntensity>0):
                print('Max Intensity  ' + str(m.maximumIntensity))
            if(m.hoverAssistIntensity>0):
                print('Hover Asssit Intensity ' + str(m.hoverAssistIntensity))
            if(m.emergencyLandIntensity>0):
                print('Emergency Land Intensity ' + str(m.emergencyLandIntensity))
            if(m.gpsIntensity>0):
                print('GPS Intensity ' + str(m.gpsIntensity))
            if(m.vibrationIntensity>0):
                print('Vibration Intensity ' + str(m.vibrationIntensity))
            if(m.hoverMotorIntensity>0):
                print('Hover Motor Intensity ' + str(m.hoverMotorIntensity))
            if(m.forwardMotorIntensity>0):
                print('Forward Motor Intensity ' + str(m.forwardMotorIntensity))
            if(m.lidarIntensity>0):
                print('Lidar Intensity ' + str(m.lidarIntensity))
            if(m.hoverBatteryIntensity>0):
                print('Hover Battery Intensity ' + str(m.hoverBatteryIntensity))
            if(m.forwardBatteryIntensity>0):
                print('Hover Battery Intensity ' + str(m.forwardBatteryIntensity))
            if(m.altitudeIntensity >0 ):
                print('Altitude Intensity ' + str(m.altitudeIntensity))
            if(m.windIntensity >0 ):
                print('Wind Intensity ' + str(m.windIntensity))
            if(m.hoverAttitudeIntensity >0 ):
                print('Hover Attitude Intensity ' + str(m.hoverAttitudeIntensity))
            if(m.landingIntensity >0 ):
                print('Landing Intensity ' + str(m.landingIntensity))
            if(m.aerodynamicIntensity >0 ):
                print('Aerodynamic Intensity ' + str(m.aerodynamicIntensity))
            if(m.airspeedIntensity >0 ):
                print('Airspeed Intensity ' + str(m.airspeedIntensity))
            if(m.servoIntensity >0 ):
                print('Servo Intensity ' + str(m.servoIntensity))
            if(m.servoIntensity >0 ):
                print('Target Search Intensity ' + str(m.targetSearchFailedIntensity))
            if(m.servoIntensity >0 ):
                print('ADSB Intensity ' + str(m.adsbFlagsIntensity))
            if(m.hoverAssistDetail>0):
                print('Hover Asssit Detail ' + str(m.hoverAssistDetail))
            if(m.emergencyLandDetail>0):
                print('Emergency Land Detail' + str(m.emergencyLandDetail))
            if(m.gpsDetail>0):
                print('GPS Detail ' + str(m.gpsDetail))
            if(m.vibrationDetail>0):
                print('Vibration Detail ' + str(m.vibrationDetail))
            if(m.hoverMotorDetail>0):
                print('Hover Motor Detail ' + str(m.hoverMotorDetail))
            if(m.forwardMotorDetail>0):
                print('Forward Motor Detail ' + str(m.forwardMotorDetail))
            if(m.lidarDetail>0):
                print('Lidar Detail ' + str(m.lidarDetail))
            if(m.hoverBatteryDetail>0):
                print('Hover Battery Detail ' + str(m.hoverBatteryDetail))
            if(m.forwardBatteryDetail>0):
                print('Hover Battery Detail ' + str(m.forwardBatteryDetail))
            if(m.altitudeDetail >0 ):
                print('Altitude Detail ' + str(m.altitudeDetail))
            if(m.windDetail >0 ):
                print('Wind Detail ' + str(m.windDetail))
            if(m.hoverAttitudeDetail >0 ):
                print('Hover Attitude Detail ' + str(m.hoverAttitudeDetail))
            if(m.landingDetail >0 ):
                print('Landing Detail ' + str(m.landingDetail))
            if(m.aerodynamicDetail >0 ):
                print('Aerodynamic Detail ' + str(m.aerodynamicDetail))
            if(m.airspeedDetail >0 ):
                print('Airspeed Detail ' + str(m.airspeedDetail))
            if(m.servoDetail >0 ):
                print('Servo Detail ' + str(m.servoDetail))
            if(m.servoDetail >0 ):
                print('Target Search Detail ' + str(m.targetSearchFailedDetail))
            if(m.servoDetail >0 ):
                print('ADSB Detail ' + str(m.adsbFlagsDetail))

        # if m.get_type() == 'SWOOP_STATUS':
        #     print('Got Flight Status')
        #     print('Flight Status: ' + str(m.flightStatus))
        #     print('Waypoint Type: ' + str(m.waypointType))
        #     print('Next Waypoint Type: ' + str(m.nextWaypointType)) 
        #     print('DO Jump COunter: ' + str(m.waypointJumper)) 
        # #if m.get_type() == 'SWOOP_ENERGY':
        #  #   print('Got energy') 
        #   #  print('F Endurance: ' + str(m.ForwardEndurance))
        #    # print('F Health: ' + str(m.ForwardHealth))	
        #     #print('F %: ' + str(m.ForwardWHrPortionRemaining))
        #     #print('ETR: ' + str(m.ForwardTimeToNextLanding))
        # if m.get_type() == 'SWOOP_ARMING_FLAGS':
        #     print('Arming Check')
        #     print('Passed Check: ' + str(m.armingCheckStatus))
        #     print('Byte 1: ' + str(m.armingCheckFlags1))
        #     print('Byte 2: ' + str(m.armingCheckFlags2)) 
        #     print('Byte 3: ' + str(m.armingCheckFlags3)) 

            

def init(mpstate):
    '''initialise module'''
    return SwoopModule(mpstate)
