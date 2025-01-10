from gpiozero import LED
from time import sleep

led = LED(21)

def main():
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)


if __name__ == "__main__":
    main()
