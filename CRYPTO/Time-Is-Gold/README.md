# Time Is Gold - Cryptography Challenge

## Challenge Information
- **Category:** Cryptography
- **Points:** TBD  
- **Difficulty:** Hard

## Challenge Description
A time-based cryptographic challenge involving AES decryption with timestamps as encryption keys. The challenge requires analyzing encrypted messages with various timestamp formats and timezone considerations.

## Challenge Files
- `fixed_messages.txt` - Collection of timestamped encrypted messages
- `time-snipet.py` - Helper/analysis script

## Solution Overview
This challenge involves:
1. **Timestamp-based AES keys**: Unix timestamps converted to 16-byte AES keys
2. **Multiple date/time formats**: Different parsing approaches needed
3. **Timezone complexity**: Various timezone assumptions must be tested
4. **Message scanning**: Search through multiple encrypted messages for the flag

## Solution Process

### Key Discovery
- AES encryption in ECB mode
- 16-byte keys derived from Unix timestamps (`timestamp.to_bytes(16, byteorder='big')`)
- Base64 encoded ciphertext

### Timestamp Parsing Strategy
1. **Date Format Variations**:
   - `%Y/%m/%d` (normal format)
   - `%Y/%d/%m` (swapped day/month)

2. **Timezone Considerations**:
   - Naive/UTC timestamps
   - US/Pacific (Portland timezone)  
   - US/Eastern
   - Explicit UTC

3. **Brute Force Approach**: Try all combinations of date formats and timezones

### Implementation Details
- Process each line in `fixed_messages.txt`
- Extract timestamp and ciphertext
- Try all format/timezone combinations
- Decrypt with AES-ECB using timestamp-derived key
- Search for "CBCTF{" in decrypted content

## Solution Files
- `solution.py` - Complete automated solution script

## Key Insights
- Time-based cryptography requires handling multiple timestamp interpretations
- Timezone ambiguity adds significant complexity
- Automated scanning is essential due to multiple encrypted messages
- AES-ECB with timestamp keys creates a brute-forceable keyspace

## Technical Details
```python
# Key derivation
key = timestamp.to_bytes(16, byteorder='big')
cipher = AES.new(key, AES.MODE_ECB)

# Decryption  
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
```

## Tools Used
- Python 3 with pycryptodome
- pytz for timezone handling
- datetime parsing libraries

## Flag Format
`CBCTF{...}`