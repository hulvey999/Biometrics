try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if not f.verifyPassword():
        raise ValueError("The given fingerprint sensor password is wrong!")

except Exception as e:
    print(f'Error: {e}')
    exit(1)

print('Waiting for finger...')

# Wait for finger to read
while f.readImage() == False:
    pass

# Convert read image to characteristics
f.convertImage(0x01)

# Search for a match
result = f.searchTemplate()

positionNumber = result[0]
accuracyScore = result[1]

if positionNumber == -1:
    print('No match found.')
else:
    print(f'Fingerprint found at position {positionNumber} with accuracy score {accuracyScore}.')
