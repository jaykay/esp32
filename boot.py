# boot.py
import senko
import machine
import network
import gc
import micropython

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Vodafone-6C8C', 'XyZ7fArxtTP6m7YK')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    print('Setting clock to NTP')

    rtc = machine.RTC()

    import ntptime
    ntptime.settime() # set the rtc datetime from the remote server
    print(rtc.datetime())

# print('free:', str(gc.mem_free()))
# # print('info:', str(machine.info()))
# print('info:', str(gc.mem_alloc()))
# print('info:', str(micropython.mem_info()))
# gc.collect()


# OTA = senko.Senko(
#   user="jaykay", repo="esp32", files = ["boot.py", "main.py"]
# )

# Connect to Wi-Fi network.
# do_connect()

# if OTA.update():
#     print("Updated to the latest version! Rebooting...")
#     machine.reset()