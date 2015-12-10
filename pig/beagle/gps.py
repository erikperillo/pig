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
along with tgs.  If not, see <http://www.gnu.org/licenses/>. 
"""

import time
import Adafruit_BBIO.UART as UART
import serial
import pig.core

class DeviceOpeningError(Exception):
    pass

class DeviceReadError(Exception):
    pass

class GPS(pig.core.Receiver):
    """
    class for representing the GPS model 'SkyNav SKM53'.
    """

    DEVICE_MODEL = "skynav_skm53"

    PLATFORMS = ["beagle", "beagleboneblack", "beaglebone", "bbb"]

    @classmethod
    def get_model_name(cls):
        return cls.DEVICE_MODEL

    @classmethod
    def supports(cls, platform):
        return platform.lower() in cls.PLATFORMS

    def __init__(self, serial_port, baud_rate=9600):
        try:
            self.device = serial.Serial(port=serial_port, baudrate=baud_rate, 
                                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
                                        bytesize=serial.EIGHTBITS)
            self._lines_buffer = []
        except Exception as e:
            raise DeviceOpeningError("error while opening device: %s" % e.message)

    def read(self, msg_to_stop="GGA", max_num_lines=100):
        if not self.device.isOpen():
            raise DeviceNotOpenException

        self.nmea_lines = self._lines_buffer
    
        while len(self.nmea_lines) <= max_num_lines:
            new_line = self.device.readline().rstrip("\r\n")

            if not new_line:
                continue

            if msg_to_stop in new_line and any(msg_to_stop in line for line in self.nmea_lines):
                self._lines_buffer = [new_line]
                return

            self.nmea_lines.append(new_line)

        raise DeviceReadError("Couldn't find %s ocurrence of '%s', limit number of lines" % \
                              (("second" if any(msg_to_stop in line for line in \
                                                self.nmea_lines) else "any"), msg_to_stop))
