import sys
from gpiozero import LED
from time import sleep

delay = 1
fnc = "ledCCW"

leds = {
	"r": LED(17),
	"g": LED(27),
	"b": LED(22)
}

if len(sys.argv) > 1:
	delay = float(sys.argv[1])

if len(sys.argv) > 2:
	fnc = sys.argv[2]

def ledReset():
	for key, value in leds.items():
		value.off()

def ledAllOn():
	for key, value in leds.items():
		value.on()

def ledOn(led):
	leds[led].on()

def ledOff(led):
	leds[led].off()

def ledCCW():
	ledOff("b")
	ledOn("r")
	sleep(delay)
	ledOff("r")
	ledOn("g")
	sleep(delay)
	ledOff("g")
	ledOn("b")
	sleep(delay)

def ledCW():
	ledOff("r")
	ledOn("b")
	sleep(delay)
	ledOff("b")
	ledOn("g")
	sleep(delay)
	ledOff("g")
	ledOn("r")
	sleep(delay)

ledReset()

i = 0
j = 5
while True:
	if i < j:
		ledCCW()
	elif (i >= j) and (i < j*2):
		ledCW()	
	elif (i >= j*2) and (i < j*3):
		ledReset()
		sleep(delay)
	elif (i >= j*3) and (i < j*4):
		ledReset()
		sleep(delay)
		ledAllOn()
		sleep(delay)
	else:
		i = -1
	i += 1
