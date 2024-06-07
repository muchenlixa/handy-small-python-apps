import segno
from segno import helpers

def hello() -> None:
    tag = segno.make('Hello World!')
    tag.save('Hello-World.png', scale = 4, border = 2)

def v_card() -> None:
    qrcode = helpers.make_vcard(name='last_name;first_name', 
                                displayname='display_name',
                                email=('me@example.org', 
                                       'another@example.org'),
                                url=['http://www.example.org', 
                                     'https://example.org/'])
    # note that you can also use 
    # helpers.make_geo -> lat, long for location
    # helper.make_email -> send message with topic and body, might be used for subscribing, registering for arrival
    # helper.make_epc_qr -> initiate an electronic payment

    qrcode.save('my-vcard.png', scale = 4)
    # to change colors of the QR code
    qrcode.save('blue_vcard.png', dark = '#0000ffcc', scale = 4)
    # to get multi colors on QR code
    qrcode.save('new_vcard.png', dark = 'darkblue', data_dark = 'steelblue', scale = 4)

def wifi_code(wifi_name, password, security) -> None:
    qrcode = helpers.make_wifi(ssid = wifi_name,
                               password = password,
                               security = security)
    qrcode.save('wifi.png', scale = 4)
    # to save in QR code in different format
    qrcode.save('wifi.svg', dark = 'yellow', light = '#323524', scale = 4)
    qrcode.save('wifi.eps', scale = 4)

hello()