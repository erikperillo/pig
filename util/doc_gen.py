#!/usr/bin/python3

"""
This tool describes interfaces present in base and devices modules.
Although the idea is to make the interfaces as language-independent
as possible, a 'loose' implementation in a simple language is good
to see how things can be structured. 
Python doesn't have a interface type (like java or go), but it
can be simulated via classes.
"""

from os import linesep
import pig

INFO_MSG = "This doc describes interfaces present in base and devices modules."

BASE_CLASSES_MSG = linesep.join(("BASE CLASSES (INTERFACES)", 
                        "These interfaces are intended to be the low-level basis of the rest",
                        "of the whole system."))

DEV_CLASSES_MSG = linesep.join(("SOME DEVICES CLASSES (INTERFACES)", 
                        "These interfaces define the devices, their services and behavior."))

BASE_CLASSES = ["Gadget",
                "InputGadget",
                "OutputGadget",
                "ScalarSensor",
                "VectorSensor",
                "Receiver",
                "Transmitter"]

DEV_CLASSES = ["Motor",
               "LightSource",
               "Button",
               "FlameThrower",
               "DistanceSensor",
               "LuminositySensor",
               "GPS"] 

def main():
    print(INFO_MSG + linesep)

    for msg, keys in zip((BASE_CLASSES_MSG, DEV_CLASSES_MSG), (BASE_CLASSES, DEV_CLASSES)):
        print(msg + linesep)

        classes = dict([(name, cls) for name, cls in pig.__dict__.items() if isinstance(cls, type)])

        for key in keys:
            print(("class '%s'" % key) + ((" [inherits from %s]" % \
                                           ", ".join(str(k) for k in classes[key].__bases__)) \
                                           if classes[key].__bases__ else "") + ":")
            print("\t" + classes[key].__doc__)

            for k, m in classes[key].__dict__.items():
                if k.startswith("__"):
                    continue

                print("\tmethod '%s':" % k)
                inputs = ",".join(_k + ("(%s)" % str(c)) for _k, c in m.__annotations__.items() \
                                  if _k != "return")
                if inputs:
                    print("\t\tinputs:", inputs)
                print("\t\treturns:", m.__annotations__["return"])
                print("\t\tdescription: %s" % m.__doc__)

            print()

if __name__ == "__main__":
    main()
