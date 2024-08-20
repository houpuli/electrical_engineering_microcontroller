# Pi Pico PWM fan control based on build-in temperature sensor

![Raspberry Pi Pico Pinout, Features, Programming Options and Peripherals](https://microcontrollerslab.com/wp-content/uploads/2021/01/Raspberry-Pi-Pico-pinout-diagram.svg)

5v input on Vbus  (40)

ground on ground   (38)

- **VBUS** – This is the power from the microUSB bus, 5-volts. If the Pico is not being powered by the microUSB connector then there will be no output here.
- **VSYS** – This is the input voltage, which can range from 2 to 5-volts. The on-board voltage converter will change it to 3.3-volts for the Pico.
- **3V3** – This is a 3.3-volt output, from the Pico’s internal regulator. It can be used to power additional components, providing you keep the load under 300ma.
- [Raspberry Pi Pico - Interface (almost) Everything! (dronebotworkshop.com)](https://dronebotworkshop.com/pi-pico/)

![Pico Power Pins](https://i0.wp.com/dronebotworkshop.com/wp-content/uploads/2021/02/pico-pins-power.jpeg?resize=750%2C422&ssl=1)

or usb 

temp input on 

PMW output 1 (front fan)  GP0   25 hz  pwm 10 to 100

PMW output 2  (cpu tach)  GP2   3500 rpm,   

8 pwm blocks : 

![](https://how2electronics.com/wp-content/uploads/2022/09/PWM-Pins-Pi-Pico-640x152.jpg)

The temperature sensor does not have a physical pin in the board but is accessed as **ADC4**.

[Read Temperature Sensor Value from Raspberry Pi Pico (how2electronics.com)](https://how2electronics.com/read-temperature-sensor-value-from-raspberry-pi-pico/)

run micropython 

[Raspberry Pi Pico and MicroPython on Windows — PiCockpit | Monitor and Control your Raspberry Pi: free for up to 5 Pis!](https://picockpit.com/raspberry-pi/raspberry-pi-pico-and-micropython-on-windows/#MicroPython)

download 

rp2-pico-20220618-v1.19.1.uf2

use thonny

select interpreter as pi pico 
