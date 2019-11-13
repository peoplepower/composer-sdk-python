'''
Created on January 27, 2017

This file is subject to the terms and conditions defined in the
file 'LICENSE.txt', which is part of this source code package.

@author: David Moss
'''

from devices.device import Device


class ButtonDevice(Device):
    """Button Device"""

    # List of Device Types this class is compatible with
    DEVICE_TYPES = [9014]

    # Measurement name for the button status
    MEASUREMENT_NAME_BUTTON_STATUS = 'buttonStatus'

    MEASUREMENT_PARAMETERS_LIST = [
        MEASUREMENT_NAME_BUTTON_STATUS
    ]

    # Goals
    GOAL_BUTTON_ARM_DISARM = 110
    GOAL_BUTTON_CALL_FOR_HELP_MEDICAL = 111
    GOAL_BUTTON_CALL_FOR_HELP_SECURITY = 112
    GOAL_BUTTON_CALL_FOR_HELP_PANIC = 113
    GOAL_BUTTON_DOORBELL = 115

    # Low battery tag
    LOW_BATTERY_TAG = "lowbattery_cr2032"

    # Type of battery
    BATTERY_TYPE = "CR2032"

    def __init__(self, botengine, device_id, device_type, device_description, precache_measurements=True):
        """
        Constructor
        :param botengine:
        :param device_id:
        :param device_type:
        :param device_description:
        :param precache_measurements:
        """
        Device.__init__(self, botengine, device_id, device_type, device_description, precache_measurements=precache_measurements)

        # Default behavior
        self.goal_id = ButtonDevice.GOAL_BUTTON_ARM_DISARM

    def initialize(self, botengine):
        """
        Initialization
        :param botengine: BotEngine environment
        """
        return

    def destroy(self, botengine):
        """
        Destroy this device
        :param botengine: BotEngine environment
        """
        return

    def get_device_type_name(self):
        """
        :return: the name of this device type in the given language, for example, "Entry Sensor"
        """
        # NOTE: Abstract device type name, doesn't show up in end user documentation
        return _("Button")
    
    def get_image_name(self):
        """
        :return: the font icon name of this device type
        """
        return "button"

    def is_currently_pressed(self, botengine=None):
        """
        :param botengine:
        :return: True if the button is currently being pressed (from the perspective of the server)
        """
        if self.MEASUREMENT_NAME_BUTTON_STATUS in self.measurements:
            return self.measurements[self.MEASUREMENT_NAME_BUTTON_STATUS][0][0]

        return False


    def is_single_button_pressed(self, botengine=None):
        """
        Find out if a single button is pressed on this device
        :param botengine:
        :param button_index: Button index if there are multiple buttons on this device.
        :return: True if the button is currently pressed
        """
        return self.MEASUREMENT_NAME_BUTTON_STATUS in self.last_updated_params and self.measurements[self.MEASUREMENT_NAME_BUTTON_STATUS][0][0]

    def is_single_button_released(self, botengine=None):
        """
        Find out if a single button is pressed on this device
        :param botengine:
        :param button_index: Button index if there are multiple buttons on this device.
        :return: True if the button is currently pressed
        """
        return self.MEASUREMENT_NAME_BUTTON_STATUS in self.last_updated_params and not self.measurements[self.MEASUREMENT_NAME_BUTTON_STATUS][0][0]

    def get_timestamp(self):
        """
        Get the timestamp of the last buttonStatus measurement received
        :param botengine:
        :return: Timestamp of the last buttonStatus measurement in ms; None if it doesn't exist
        """
        if self.MEASUREMENT_NAME_BUTTON_STATUS in self.measurements:
            return self.measurements[self.MEASUREMENT_NAME_BUTTON_STATUS][0][1]

        return None