def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Vodafone-6C8C', 'XyZ7fArxtTP6m7YK')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    print('Setting clock to NTP')
    from machine import RTC

    rtc = RTC()

    import ntptime
    ntptime.settime() # set the rtc datetime from the remote server
    print(rtc.datetime())

do_connect()