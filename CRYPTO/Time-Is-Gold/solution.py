#!/usr/bin/env python3
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from datetime import datetime
import pytz

def try_decrypt(timestamp, ciphertext_b64):
    try:
        key = timestamp.to_bytes(16, byteorder='big')
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = base64.b64decode(ciphertext_b64)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()
    except:
        return None

def decrypt_message(timestamp_str, ciphertext_b64):
    # Parse timestamp in multiple ways
    try:
        parts = timestamp_str.split()
        date_part, time_part = parts[0], parts[1]
        
        # Try different date formats
        date_formats = [
            "%Y/%m/%d",  # normal
            "%Y/%d/%m"   # swapped day/month
        ]
        
        for date_format in date_formats:
            try:
                # Parse without timezone first (naive)
                dt_str = f"{date_part} {time_part}"
                dt_naive = datetime.strptime(dt_str, f"{date_format} %H:%M")
                
                # Try different timezone assumptions
                timezones = [
                    None,  # UTC/naive
                    pytz.timezone('US/Pacific'),  # Portland
                    pytz.timezone('UTC'),
                    pytz.timezone('US/Eastern'),
                ]
                
                for tz in timezones:
                    if tz is None:
                        # Use naive datetime
                        timestamp = int(dt_naive.timestamp())
                    else:
                        # Localize to timezone
                        dt_tz = tz.localize(dt_naive)
                        timestamp = int(dt_tz.timestamp())
                    
                    result = try_decrypt(timestamp, ciphertext_b64)
                    if result:
                        tz_name = "naive" if tz is None else str(tz)
                        return f"[{date_format}, {tz_name}] {result}"
                        
            except ValueError:
                continue
                
    except Exception as e:
        pass
        
    return None

# Process messages looking for the flag
with open('fixed_messages.txt', 'r') as f:
    for line_num, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
            
        parts = line.split(' ', 2)
        if len(parts) != 3:
            continue
            
        date_part, time_part, ciphertext = parts
        timestamp_str = f"{date_part} {time_part}"
        
        decrypted = decrypt_message(timestamp_str, ciphertext)
        if decrypted and "CBCTF{" in decrypted:
            print(f"*** FLAG FOUND on line {line_num} ***")
            print(f"Timestamp: {timestamp_str}")
            print(f"Flag: {decrypted}")
            break
        elif decrypted:
            print(f"Line {line_num}: {decrypted}")
            
        # Continue searching for flag
            
print("Finished processing")