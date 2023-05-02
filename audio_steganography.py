import wave

def encode_message():
    audio_file=input("enter the audio file with extension:")
    msg=input("enter the mssg u want to hide:")
    msg=b'msg'
    output_file=input("enter the output file with extension:")
    audio=wave.open(audio_file,'rb')
    output=wave.open(output_file, 'wb')
    output.setparams(audio.getparams())
    frames = audio.readframes(audio.getnframes())
    msg += int.to_bytes(0, 1, 'big') # Add null byte as end-of-message marker
    msg_bits = ''.join(format(byte, '08b') for byte in msg)
    encoded_frames = bytearray(frames)
    for i, bit in enumerate(msg_bits):
        byte_pos = i // 8
        if byte_pos >= len(encoded_frames):
            break
        encoded_byte = encoded_frames[byte_pos]
        if bit == '1':
            encoded_byte |= 1
        else:
            encoded_byte &= 0xFE
        encoded_frames[byte_pos] = encoded_byte
    output.writeframes(bytes(encoded_frames))

def decode_message():
    audio_file=input("enter the file to be decoded with extension:")
    with wave.open(audio_file, 'rb') as audio:
        frames = audio.readframes(audio.getnframes())
        extracted_bits = ''
        for byte in frames:
            extracted_bits += format(byte, '08b')[-1]
            if extracted_bits[-8:] == '00000000':
                break
        bits=int(extracted_bits)
        print(bits)
        print(type(bits))


        #for i in range(0, len(extracted_bits)-8, 8)
        msg_bytes = bytearray(int(extracted_bits[i:i+8], 2) for i in range(0, len(extracted_bits)-8, 8))
        
         # replace 'utf-8' with the appropriate encoding if needed
        return msg_bytes
a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
if (a == 1):
	encode_message()

elif (a == 2):
    x=decode_message()
    print("decoded word:")
    print(x)
    






