from pyfingerprint.pyfingerprint import PyFingerprint

try:
    # Initialize the fingerprint sensor
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if not f.verifyPassword():
        raise ValueError("The given fingerprint sensor password is wrong!")

except Exception as e:
    print(f'Error: {e}')
    exit(1)

print('Waiting for finger...')

# Wait that finger is read
while f.readImage() == False:
    pass

# Convert read image to characteristics and store in charbuffer 1
f.convertImage(0x01)

# Save template to file
positionNumber = f.storeTemplate()
print(f'Fingerprint captured and stored at position {positionNumber}.')
