import esphome.codegen as cg
from esphome.components import sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_POWER,
    CONF_TEMPERATURE,
    DEVICE_CLASS_POWER ,
    ENTITY_CATEGORY_DIAGNOSTIC,
    DEVICE_CLASS_TEMPERATURE,
    ICON_POWER,
    ICON_THERMOMETER,
    ICON_AIR_FILTER,
    UNIT_WATT,
    UNIT_CELSIUS,
    UNIT_SECOND,
)

CONF_FILTER_LIFE = "filter_life"

from . import CONF_BROAN_ID, BroanComponent

DEPENDENCIES = ["broan"]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_BROAN_ID): cv.use_id(BroanComponent),
        cv.Optional(CONF_POWER): sensor.sensor_schema(
            device_class=DEVICE_CLASS_POWER,
            icon=ICON_POWER,
            unit_of_measurement=UNIT_WATT,
        ),
        cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon=ICON_THERMOMETER,
            unit_of_measurement=UNIT_CELSIUS,
        ),
        cv.Optional(CONF_FILTER_LIFE): sensor.sensor_schema(
            icon=ICON_AIR_FILTER,
            unit_of_measurement=UNIT_SECOND,
        ),
    }
)

async def to_code(config):
    broan_component = await cg.get_variable(config[CONF_BROAN_ID])
    if power_config := config.get(CONF_POWER):
        sens = await sensor.new_sensor(power_config)
        cg.add(broan_component.set_power_sensor(sens))

    if temperature_config := config.get(CONF_TEMPERATURE):
        sens = await sensor.new_sensor(temperature_config)
        cg.add(broan_component.set_temperature_sensor(sens))


    if filter_life_config := config.get(CONF_FILTER_LIFE):
        sens = await sensor.new_sensor(filter_life_config)
        cg.add(broan_component.set_filter_life_sensor(sens))
