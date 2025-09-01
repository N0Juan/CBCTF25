# 3rd Time Charm - Cryptography Challenge

## Challenge Information
- **Category:** Cryptography
- **Points:** TBD
- **Difficulty:** Medium

## Challenge Description
A multi-stage cryptographic puzzle involving pattern analysis and cipher decryption. The challenge hint suggests: "The first one is simple. Then its shifted further. But after that its uniform."

## Solution Overview
This challenge involves a custom cipher with varying shift patterns:
1. The first few characters use simple shifts
2. Some characters are "shifted further" 
3. The remaining characters use a uniform shift pattern

## Solution Files
- `decode_charm.py` - Main solution script
- `decode_charm2.py` - Alternative/additional solution approach

## Solution Process
1. **Pattern Analysis**: The cipher uses different shift values for different positions
2. **Shift Pattern Discovery**: 
   - First few characters: simple shifts (2, 2, 2)
   - Middle characters: increased shifts (3, 4)
   - Remaining characters: uniform shift pattern
3. **Brute Force**: Try different uniform shift values for the remaining positions
4. **Validation**: Look for results starting with "CBCTF" to identify the correct solution

## Key Insights
- The cipher text is provided as a list of ASCII values
- Different positions use different shift values following a described pattern
- The solution requires both pattern recognition and brute force techniques

## Flag Format
`CBCTF{...}`

## Tools Used
- Python 3
- Custom decryption script
- Pattern analysis