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

from Adafruit_I2C import Adafruit_I2C
import time
import sys
import math
import pig.core

class Compass(pig.core.VectorSensor):
    #definitions 
    DEVICE_MODEL = "HMC5883L"

    PLATFORMS = ["beagle", "beagleboneblack", "bbb", "beaglebone"]

    #device registers
    REGISTERS = {"a": 0x00, "b": 0x01, "mode": 0x02,
                 "x_msb": 0x03, "x_lsb": 0x04,
                 "z_msb": 0x05, "z_lsb": 0x06,
                 "y_msb": 0x07, "y_lsb": 0x08,
                 "status": 0x09, "id_a": 0x0a, "id_b": 0x0b, "id_c": 0x0c}

    #available (measurement) modes
    MODES = {"default": 0x00, "continuous": 0x00, "single": 0x01}

    #gains (LBb/Gauss)
    GAINS = {"default": 0x01, "low": 0x07, "mean": 0x03, "high": 0x00}

    #measuring rates (Hz)
    RATES = {"default": 0x04, "low": 0x00, "mean": 0x05, "high": 0x06}

    #number of samples to get per measurement
    SAMPLING = {"default": 0x00, "low": 0x00, "mean": 0x02, "high": 0x03}

    #bias to apply to device
    BIAS = {"default": 0x00, "positive": 0x01, "negative": 0x02}

    #status to status registers
    STATUS = {"ready": 0x01}

    @classmethod
    def get_model_name(cls):
        return Compass.DEVICE_MODEL

    @classmethod
    def supports(cls, platform):
        return platform.lower() in Compass.PLATFORMS

    def __init__(self, port, cfg_file="", gain="default", rate="default", 
                 mode="default", samples="default", bias="default"):
        #initialization of device
        self.device = Adafruit_I2C(port)

        #setting mode via registers
        self.set_reg_a(Compass.SAMPLING[samples], Compass.RATES[rate], Compass.BIAS[bias])
        self.set_reg_b(Compass.GAINS[gain])
        self.set_reg_mode(Compass.MODES[mode])

        #opening configuration file; must be .csv 
        if cfg_file:
            with open(cfg_file, "r") as fd:
                self.errors = tuple(int(val) for val in fd.read().split(",")) 
        else:
            self.errors = 2*(1, 0)
    
    def write(self, register, mode):
        self.device.write8(register,mode)  

    def read(self, register):
        return self.device.readS8(register)

    def set_reg_a(self, samples="default", rate="default", bias="default"):
        mode = (Compass.SAMPLING[samples] << 5) | (Compass.RATES[rate] << 2) | Compass.BIAS[bias]
        self.write(REGISTERS["a"], mode) 

    def set_reg_b(self, gain=GAINS["default"]):
        mode = gain << 5
        self.write(REGISTERS["b"], mode)

    def set_reg_mode(self, mode=MODES["continuous"]):
        mode = mode
        self.write(REGISTERS["mode"], mode)

    def refresh(self):
        #defining registers from which to read
        registers = [Compass.REGISTERS[key] for key in ("x_msb", "x_lsb", "y_msb",
                                                        "y_lsb", "z_msb", "z_lsb")]

        #reading data from sensor's registers
        raw_data = [self.read(reg) for reg in registers]

        #making the right shifts to get the value
        self._x, self._y, self._z = tuple(raw_data[i] << 8 | raw_data[i+1] \
                                          for i in range(0, len(raw_data), 2)) 

    def value_x(self):
        return self._x    

    def value_y(self):
        return self._y    

    def value_z(self):
        return self._z    

    def angle(self, ):
        self.refresh()
        x, y = self.value_x(), self.value_y()

        #compensating errors
        xmax, xmin, ymax, ymin = self.errors
        x = 2*(x-xmin)/float(xmax-xmin) - 1
        y = 2*(y-ymin)/float(ymax-ymin) - 1

        return math.atan2(y, x)
