import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor
from esphome.const import CONF_ID, CONF_RESOLUTION, UNIT_LUX, ICON_BRIGHTNESS_5

DEPENDENCIES = ['i2c']

bh1750_ns = cg.esphome_ns.namespace('bh1750')
BH1750Resolution = bh1750_ns.enum('BH1750Resolution')
BH1750_RESOLUTIONS = {
    4.0: BH1750Resolution.BH1750_RESOLUTION_4P0_LX,
    1.0: BH1750Resolution.BH1750_RESOLUTION_1P0_LX,
    0.5: BH1750Resolution.BH1750_RESOLUTION_0P5_LX,
}

BH1750Sensor = bh1750_ns.class_('BH1750Sensor', sensor.PollingSensorComponent, i2c.I2CDevice)

CONFIG_SCHEMA = sensor.sensor_schema(UNIT_LUX, ICON_BRIGHTNESS_5, 1).extend({
    cv.GenerateID(): cv.declare_id(BH1750Sensor),
    cv.Optional(CONF_RESOLUTION, default=0.5): cv.enum(BH1750_RESOLUTIONS, float=True),
}).extend(cv.polling_component_schema('60s')).extend(i2c.i2c_device_schema(0x23))


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)
    yield i2c.register_i2c_device(var, config)

    cg.add(var.set_resolution(config[CONF_RESOLUTION]))
