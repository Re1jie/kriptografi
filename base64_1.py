import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
konversi_byte = bytes.fromhex(hex_string)

print(konversi_byte)

encode_base64 = base64.b64encode(konversi_byte)

print(encode_base64)

