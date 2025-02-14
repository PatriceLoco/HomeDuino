#include "esphome/core/log.h"
#include "firebase_sensor.h"

namespace esphome {
namespace firebase_sensor {

static const char *TAG = "firebase_sensor.text_sensor";

void FirebaseSensor::setup() {
  
}

void FirebaseSensor::dump_config() { 
    ESP_LOGCONFIG(TAG, "Firebase sensor");
}

}  // namespace firebase_sensor
}  // namespace esphome