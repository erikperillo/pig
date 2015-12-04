"""  
Copyright 2015 Erik Perillo <erik.perillo@gmail.com>

This file is part of pig.

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this.  If not, see <http://www.gnu.org/licenses/>. 
"""

import base

class Motor(base.OutputGadget):
    """interface that represents motors."""    
    def move(self, intensity):
        """moves the motor with the speed defined by intensity.
           intensity is a value between [-1,1], whereas -1 is the maximum speed
           in reverse direction and 1 is the maximum speed in normal direction.
           intensity: float"""
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)

class LightSource(base.OutputGadget):
    """interface that represents some light source."""    
    def lighten(self, intensity):
        """produces light via the sensor with luminosity defined by intensity.
           intensity is a value between [0,1], whereas 0 is the mininum possible 
           luminosity and 1 is the maximum possible luminosity.
           intensity: float"""
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)

class Button(base.InputGadget):
    """interface that represents a simple button."""    
    def pressed(self):
        """returns True if the button is/was held down and False otherwise.
           return: bool"""
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)

class Camera(base.InputGadget):
    """interface that represents a camera."""    
    def get_frame(self):
        """returns an image representation.
           return: <matrix>"""
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)

class FlameThrower(base.OutputGadget):
    """interface that represents flamethrower devices."""
    def fire(self, intensity):
        """sends flaming death to the world.
           intensity is a value between [0,1], whereas 0 is the mininum possible
           fire intensity and 1 is the maximum.
           intensity: float"""
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)

class DistanceSensor(base.ScalarSensor):
    """interface that represents distance sensors. it may be an ultrassonic or infrared one,
       for example."""    
    def value(self):
        """returns the distance from the sensor in meters. the return value must be 
           greater or equal to zero.
           return: float"""
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)

class LuminositySensor(base.ScalarSensor):
    """interface that represents a light sensor."""
    def value(self):
        """gets the luminosity read by the sensor. the return value must be between [0,1], 
           whereas 0 is the mininum luminosity possibly readable by the sensor 
           and 1 is the maximum.
           return: float"""
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)

class GPS(base.Receiver):
    """interface that represents a GPS receiver device."""
    def get_NMEA_message(self):
        """gets a standard NMEA message from device.
           return: str""" 
        raise NotImplementedError(base.NOT_IMPLEMENTED_MSG)
