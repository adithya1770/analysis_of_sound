from machine import Pin, time_pulse_us
import time

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
main_Arr = list()

def get_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()

    duration = time_pulse_us(echo, 1, 30000)

    distance_cm = (duration * 0.0343) / 2
    distance_m = distance_cm / 100
    return distance_m, duration

while True:
    new_Arr = list()
    dist, duration = get_distance()
    duration=duration/1000000
    reading = sensor_temp.read_u16() * conversion_factor
    temp = 27 - (reading - 0.706)/0.001721
    new_Arr.append([dist, duration, temp])
    main_Arr.append(new_Arr)
    print(main_Arr)
    time.sleep(1)

