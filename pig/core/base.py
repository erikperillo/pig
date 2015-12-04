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

NOT_IMPLEMENTED_MSG = "method must be implemented to comply with the interface"

class Gadget(object):
    """all gadgets should inherit this."""
    def model_name(self):
        """returns the device's model name.
           return: str"""
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)
    def supports(self, platform):
        """returns whether the gadget is designed for some platform
           platform: str
           return: bool"""
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

class InputGadget(Gadget):
    """any gadget that gets some signal from the outside world should inherit this."""
    pass

class OutputGadget(Gadget):
    """any gadget that produces some signal to the outside world should inherit this."""
    pass

class ScalarSensor(InputGadget):
    """any gadget which value of interest is a physical scalar quantity should inherit this."""
    def value(self):
        """returns the intensity of the quantity measured by the device.
           return: float"""
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

class VectorSensor(InputGadget):
    """any gadget which value of interest is a physical vector quantity should inherit this."""
    def value_x(self):
        """returns the intensity of the quantity measured by the device on the x axis.
           return: float"""
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)
    def value_y(self):
        """returns the intensity of the quantity measured by the device on the y axis.
           return: float"""
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)
    def value_z(self):
        """returns the intensity of the quantity measured by the device on the z axis.
           return: float"""
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

class Receiver(InputGadget):
    """any gadget which value of interest is a signal from another gadget 
       should inherit this.""" 
    pass

class Transmitter(OutputGadget):
    """any gadget which sends a signal to another gadget should inherit this.""" 
    pass
