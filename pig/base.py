class Gadget(object):
    """all gadgets should inherit this."""
    def getModelName() -> str:
        """returns the device's model name."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class InputGadget(Gadget):
    """any gadget that gets some signal from the outside world should inherit this."""
    pass

class OutputGadget(Gadget):
    """any gadget that produces some signal to the outside world should inherit this."""
    pass

class ScalarSensor(InputGadget):
    """any gadget which value of interest is a physical scalar quantity should inherit this."""
    def getIntensity() -> float:
        """returns the intensity of the quantity measured by the device."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class VectorSensor(InputGadget):
    """any gadget which value of interest is a physical vector quantity should inherit this."""
    def getXIntensity() -> float:
        """returns the intensity of the quantity measured by the device on the x axis."""
        raise NotImplementedError("method must be implemented to comply with the interface")
    def getYIntensity() -> float:
        """returns the intensity of the quantity measured by the device on the y axis."""
        raise NotImplementedError("method must be implemented to comply with the interface")
    def getZIntensity() -> float:
        """returns the intensity of the quantity measured by the device on the z axis."""
        raise NotImplementedError("method must be implemented to comply with the interface")

class Receiver(InputGadget):
    """any gadget which value of interest is a signal from another gadget 
       should inherit this.""" 
    pass

class Transmitter(OutputGadget):
    """any gadget which sends a signal to another gadget should inherit this.""" 
    pass
