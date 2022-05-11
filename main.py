from stem import Signal
from stem.control import Controller

password = input('Entter your tor password')

#### to setup up tor password do;

# tor --hash-password <YOUR_PASSWORD_HERE>


def change_ip_address(password):


    print("Changing ip address...")
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)
        
