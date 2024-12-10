## QR Code Generator

This python project contains functions to generate QR codes for different purpose using the `segno` library and `helpers`. The supported types of QR codes includes:
- A vCard QR code containing contact information.
- A Wi-Fi QR code that contains network credentials.

---
### Requirements
Before using the code, ensure that you have the required dependencies installed. You can install them using `pip`.
```python
pip install segno
```
---
### Functions

1. `v_card(last_name: str, first_name: str, display_name: str, emails: list, urls: list)`

    **Description**

    Generates a vCard QR code containing contact information, including the person's name, display name, email addresses, and URLs. A vCard QR code can be scanned to save contact details directly to a phone's contact list.
    
    **Parameters**

    - last_name (str): The last name of the contact.
    - first_name (str): The first name of the contact.
    - display_name (str): The display name (or full name) to be shown.
    - emails (list): A list of email addresses associated with the contact.
    - urls (list): A list of URLs associated with the contact.

   **Example**
    ```python
   v_card(
       last_name="Doe", 
       first_name="John", 
       display_name="John Doe", 
       emails=["john.doe@example.com"], 
       urls=["http://www.johndoe.com"]
   )
    ```
   This will generate a vCard QR code and save it as `my-vcard.png` in the current directory. You can also change the QR code's colors or create multi-colored QR codes by modifying the `save` function's parameters.

2. `wifi_code(wifi_name: str, password: str, security: str)`
    
    **Description**

   Generates a QR code for Wi-Fi network credentials (SSID, password, and security type). This QR code allows devices to scan and automatically connect to the network.
   
   **Parameters**

    - wifi_name (str): The name (SSID) of the Wi-Fi network.
    - password (str): The password for the Wi-Fi network.
    - security (str): The security authentication type used for the network. Common values include:
        - WEP
        - WPA
        - WPA2
        - WPA3

   **Example**

   ```python
   wifi_code("MyNetwork", "supersecretpassword", "WPA2")
   ```

   This will generate a Wi-Fi QR code and save it as `MyNetwork.png` in the current directory.

   **Notes**

     The generated QR codes can be saved in different formats (e.g., PNG, SVG, EPS) by modifying the `save` method.
     To customize the appearance of the QR code (e.g., changing colors or scale), you can adjust the `save` function parameters as demonstrated in the comments.

   Example with custom colors:

   qrcode.save('wifi_custom.svg', dark='yellow', light='#323524', scale=4)

---
### Future updates

You can use other helper functions from the helpers module such as:
   - `helpers.make_geo()` for creating a QR code with geographic coordinates (latitude and longitude).
   - `helpers.make_email()` for creating a QR code that initiates an email with a subject and body.
   - `helpers.make_epc_qr()` for initiating an electronic payment QR code.

These functions are not used in the current code but are available for further enhancements.