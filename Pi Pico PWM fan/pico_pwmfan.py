import machine
from machine import Pin, PWM
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
frontfan = PWM(Pin(0))
cputach = PWM(Pin(2))

cputach.freq(int(10000/60))
cputach.duty_u16(int(50 * 65535 / 100))

frontfan.freq(25000)
#

def duty_cycle(temperature):
    return 20 + (temperature - 10) * 80 / 50

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    #voltage = reading
    #print('V',voltage)
    temperature = 27 - (reading - 0.706)/0.001721 +10
    print('TempC',temperature)
    
    frontfan.duty_u16(int(duty_cycle(temperature) * 65535 / 100))
    utime.sleep(2)
    
    # blink on-board LED to indicate the pwm value, led blink faster when the pwm value is higher
    machine.Pin(25, machine.Pin.OUT).value(1)
    utime.sleep_ms(int(duty_cycle(temperature))*100)
    machine.Pin(25, machine.Pin.OUT).value(0)
    #utime.sleep_ms(int(duty_cycle(temperature)))
    