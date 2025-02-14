import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor

firebase_sensor_ns = cg.esphome_ns.namespace("firebase_sensor")
FirebaseSensor = firebase_sensor_ns.class_("FirebaseSensor", text_sensor.TextSensor, cg.Component)

CONFIG_SCHEMA = text_sensor.text_sensor_schema(FirebaseSensor).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = await text_sensor.new_text_sensor(config)
    await cg.register_component(var, config)
    cg.add_library("mobizt/FirebaseClient", "1.3.5")
