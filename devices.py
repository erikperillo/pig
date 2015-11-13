from base import *

class Motor(OutputGadget):
    """interface that represents motors."""    
    def move(intensity: float) -> None:
        """moves the motor with the speed defined by intensity.
           intensity is a value between [-1,1], whereas -1 is the maximum speed
           in reverse direction and 1 is the maximum speed in normal direction."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class LightSource(OutputGadget):
    """interface that represents some light source."""    
    def lighten(intensity: float) -> None:
        """produces light via the sensor with luminosity defined by intensity.
           intensity is a value between [0,1], whereas 0 is the mininum possible 
           luminosity and 1 is the maximum possible luminosity."""

class Button(InputGadget):
    """interface that represents a simple button."""    
    def pressed() -> bool:
        """returns True if the button is/was held down and False otherwise."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class FlameThrower(OutputGadget):
    """interface that represents flamethrower devices."""
    def fire(intensity: float) -> None:
        """sends flaming death to the world.
           intensity is a value between [0,1], whereas 0 is the mininum possible
           fire intensity and 1 is the maximum."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class DistanceSensor(ScalarSensor):
    """interface that represents distance sensors. it may be an ultrassonic or infrared one,
       for example."""    
    def getDistance() -> float:
        """returns the distance from the sensor in meters. the return value must be 
           greater or equal to zero."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class LuminositySensor(ScalarSensor):
    """interface that represents a light sensor."""
    def getLuminosity() -> float:
        """gets the luminosity read by the sensor. the return value must be between [0,1], 
           whereas 0 is the mininum luminosity possibly readable by the sensor 
           and 1 is the maximum."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class GPS(Receiver):
    """interface that represents a GPS receiver device."""
    def getNMEAMessage() -> str:
        """gets a standard NMEA message from device.""" 
        raise NotImplementedError("method must be implemented to comply with the interface")
