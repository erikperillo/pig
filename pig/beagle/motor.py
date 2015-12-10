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

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time
import pig.core

class BrushedMotor(pig.core.Motor):
    """
    represents a motor and sends proper signals to make it spin
    """

    DEVICE_MODEL = "generic_motor"

    PLATFORMS = ["beagle", "beagleboneblack", "beaglebone", "bbb"]

    @classmethod
    def get_model_name(cls):
        return cls.DEVICE_MODEL

    @classmethod
    def supports(cls, platform):
        return platform.lower in cls.PLATFORMS

    def __init__(self, pwm_port, sign_port, enable_port, disable_port, 
                 max_speed=75.0, dead_zone_speed=0, inverted=False):
        self.pwm_port = pwm_port
        self.sign_port = sign_port 
        self.enable_port = enable_port 
        self.disable_port = disable_port 
        self.inverted = inverted
        self.max_speed = max_speed
        self.dead_zone_speed = dead_zone_speed

        #starting up ports
        GPIO.setup(self.enable_port, GPIO.OUT)
        GPIO.setup(self.disable_port, GPIO.OUT)
        GPIO.setup(self.sign_port, GPIO.OUT)
        PWM.start(self.pwm_port, 0)

    def safeSpeed(self, speed):
        #protecting the motor: 
        #if the signal if less than dead_zone, motor won't even move. 
        #also, avoids a too big speed
        if abs(speed) <= self.dead_zone_speed:
            return 0.0
        return min(abs(speed), self.max_speed)

    def move(self, value):
        """
        moves the motor. 
        accepts any integer value, but it will be converted to motor's maximum value if needed.
        if negative, it automatically transforms the values to send it correctly to GPIO/PWM
        """
        #setting motor corrected direction
        #safe value (absolute value)
        pwm_val = 100.0 * self.safeSpeed(value)
        #sign
        _sign = (-1 if value < 0.0 else 1) * (-1 if self.inverted else 1)
        sign = GPIO.HIGH if _sign >= 0 else GPIO.LOW

        #sending PWM signal
        PWM.set_duty_cycle(self.pwm_port, pwm_val)

        #driver enable/disable
        GPIO.output(self.enable_port, GPIO.HIGH)
        GPIO.output(self.disable_port, GPIO.LOW)

        GPIO.output(self.sign_port, sign)

    def __del__(self):
        PWM.stop(self.pwm_port) 
        PWM.cleanup(self.pwm_port)
