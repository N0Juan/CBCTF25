# Encoded Message - Network Security Challenge

## Challenge Information
- **Category:** Network Security
- **Points:** TBD
- **Difficulty:** TBD

## Challenge Description
A network forensics challenge involving the analysis of encoded messages within network traffic.

## Challenge Files
- `Enc0ded_M3ssag3.pcap` - Network packet capture containing encoded communications

## Solution Overview
This challenge requires analyzing network traffic to discover and decode hidden messages. The solution likely involves:
- Packet analysis and filtering
- Message extraction from network streams
- Decoding/decryption of discovered messages
- Protocol-level message reconstruction

## Analysis Approach
1. **Traffic Analysis**: Examine the packet capture for suspicious or encoded data
2. **Stream Following**: Reconstruct communication streams
3. **Encoding Detection**: Identify encoding schemes used (Base64, hex, custom, etc.)
4. **Message Decoding**: Apply appropriate decoding techniques
5. **Flag Extraction**: Retrieve the final decoded flag

## Potential Encoding Schemes
- Base64 encoding
- Hexadecimal encoding
- ASCII manipulation
- Custom encoding algorithms
- Steganographic techniques

## Tools Used
- Wireshark for PCAP analysis
- Network stream analyzers
- Encoding/decoding utilities
- Protocol analyzers

## Skills Required
- Network traffic analysis
- Encoding/decoding techniques
- Pattern recognition
- Protocol understanding

## Flag Format
`CBCTF{...}`

## Notes
*Detailed solution pending - PCAP analysis and message decoding required*