import segno
from segno import helpers

def hello() -> None:
    # testing purpose
    tag = segno.make('Hello World!')
    tag.save('Hello-World.png', scale = 4, border = 2)

def v_card(last_name:str, 
           first_name:str, 
           display_name:str, 
           emails:list, 
           urls:list) -> None:
    '''This function generates contact information '''
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
    # qrcode.save('blue_vcard.png', dark = '#0000ffcc', scale = 4)
    # to get multi colors on QR code
    # qrcode.save('new_vcard.png', dark = 'darkblue', data_dark = 'steelblue', scale = 4)

def wifi_code(wifi_name:str, 
              password:str,
              security:str) -> None:
    '''This function takes wifi-name, password and security authentication type to generate qr-code.
        The most common security authentication types are: WEP, WPA, WPA2, WPA3, etc.'''
    qrcode = helpers.make_wifi(ssid = wifi_name,
                               password = password,
                               security = security)
    
    qrcode.save(f'{wifi_name}.png', scale = 20)
    # to save in QR code in different format
    # qrcode.save('wifi.svg', dark = 'yellow', light = '#323524', scale = 4)
    # qrcode.save('wifi.eps', scale = 4)
