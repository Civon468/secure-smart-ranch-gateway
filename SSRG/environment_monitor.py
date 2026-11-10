import math

from datetime import datetime
import logging

logging.basicConfig(
    filename= "ranch_monitor.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)


temperature_threshold = 30
Humidity_threshold = 75

sensor_reading = [
    {"sensor_id": "TEMP-04", "temperature": "unknown"},
    {"sensor_id": "TEMP-05", "temperature": None},
    {"sensor_id": "TEMP-06", "temperature": 150.0},
    {"sensor_id": "TEMP-07", "temperature": float("nan")}
]

def validate_temperature(temperature):
    if not isinstance(temperature, (int, float)):
        return False
    if isinstance(temperature, bool):
        return False
    if not math.isfinite(temperature):
            return False
    if temperature < -50 or temperature > 100:
        return False
   
    return True


def check_Temerature(temperature,threshold):
    if temperature > threshold:
        return "Warning"
    else:
        return "Normal"





def main():
    for reading in sensor_reading:
        temperature = reading["temperature"]
        sensor_id = reading["sensor_id"]


        if not validate_temperature(temperature):
            print(sensor_id, "INVALID READING")
            logging.error(
                f"Sensor {sensor_id}: invalid temperature reading" 
            )
            continue

        timestamp = datetime.now().isoformat(timespec="seconds")

        status = check_Temerature(temperature, temperature_threshold)
        print(timestamp,sensor_id, temperature, status)

        if status == "Warning":
            logging.warning(
                f"Sensor {sensor_id}: temperature={temperature}"
            )
        else:
            logging.info(
                f"Sensor {sensor_id}: temperature={temperature}"
            )
 
if __name__ == "__main__":
    main()