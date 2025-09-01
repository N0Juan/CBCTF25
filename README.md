# Cyber Battle CTF 2025 - Qualifying Round Writeups

## Overview
Collection of writeups documenting my solutions for the Cyber Battle Capture The Flag 2025 Qualifying Round.

## Author
**N0Juan**

## Competition Details
- **Event:** Cyber Battle CTF 2025
- **Round:** Qualifying
- **Date:** 31st August 2025
- **Team:** 3MVIPI

## Challenge Status Table

| Category | Challenge Name | Points | Difficulty | Status | Solution Type |
|----------|----------------|--------|------------|--------|---------------|
| **CRYPTO** | [3rd Time Charm](CRYPTO/3rd-Time-Charm/) | 75 | Medium | ✅ **SOLVED** | Progressive shift cipher |
| **CRYPTO** | [Journey Home](CRYPTO/Journey-Home/) | TBD | Medium | ✅ **SOLVED** | Image cryptography |
| **CRYPTO** | [Time Is Gold](CRYPTO/Time-Is-Gold/) | TBD | Hard | ✅ **SOLVED** | Timestamp-based AES decryption |
| **EXPLOIT** | [Gandalf](EXPLOIT/Gandalf/) | TBD | TBD | ❌ **UNSOLVED** | Binary crackme analysis required |
| **EXPLOIT** | [Operation Echo](EXPLOIT/Operation-Echo/) | 50 | Medium | ✅ **SOLVED** | Format string vulnerability |
| **EXPLOIT** | [The Last Spark](EXPLOIT/The-Last-Spark/) | TBD | Hard | ✅ **SOLVED** | Memory dump XOR decryption |
| **FORENSIC** | [Operation LC](FORENSIC/Operation-LC/) | TBD | Medium | ✅ **SOLVED** | USB forensics + steganography |
| **FORENSIC** | [Photogrammetry](FORENSIC/Photogrammetry/) | TBD | TBD | ❌ **UNSOLVED** | Archive analysis required |
| **MISC** | [Gatecrash](MISC/Gatecrash/) | TBD | TBD | ❌ **UNSOLVED** | Image analysis required |
| **NETWORK** | [Command-n-Control](NETWORK/Command-n-Control/) | TBD | TBD | ❌ **UNSOLVED** | PCAP analysis required |
| **NETWORK** | [Encoded Message](NETWORK/Encoded-Message/) | TBD | TBD | ❌ **UNSOLVED** | Network message decoding required |
| **NETWORK** | [MITRE](NETWORK/MITRE/) | TBD | TBD | ❌ **UNSOLVED** | ATT&CK framework analysis required |
| **WEB** | [Secure Archive](WEB/Secure-Archive/) | TBD | Medium | ✅ **SOLVED** | LFI with double URL encoding |
| **WEB** | [Warming Up](WEB/Warming-Up/) | TBD | Easy/Medium | ✅ **SOLVED** | SQLi + IDOR combination |

## Progress Summary

- **Total Challenges:** 14
- **Solved:** 8 (57%)
- **Unsolved:** 6 (43%)

### By Category:
- **CRYPTO:** 3/3 solved (100%) 🏆
- **EXPLOIT:** 2/3 solved (67%)
- **FORENSIC:** 1/2 solved (50%)
- **MISC:** 0/1 solved (0%)
- **NETWORK:** 0/3 solved (0%)
- **WEB:** 2/2 solved (100%) 🏆

## Notable Solutions

### 🏆 Complete Writeups Available:
- **3rd Time Charm** - Progressive shift cipher: `CBCTF{you_captured_me_finally}`
- **Operation Echo** - Format string exploitation: `flag{f0rm4t_str1ng_3xpl01t_succ3ss}`
- **Time Is Gold** - Advanced AES timestamp key cracking
- **Operation LC** - Multi-stage forensics with steganography
- **Secure Archive** - Double URL encoding bypass technique
- **Warming Up** - Classic SQLi + IDOR combination

### 🔧 Solutions with Scripts:
- **3rd Time Charm** - Python decryption scripts (`decode_charm.py`, `decode_charm2.py`)
- **Time Is Gold** - Automated timestamp bruteforce (`solution.py`)
- **The Last Spark** - Memory analysis script (`solution.py`)

### 📋 Pending Analysis:
- **Gandalf** - Binary available via [Google Drive link](https://drive.google.com/file/d/1yKMOItr2g8YQmrP2aUfcf5xC_HLY1swT/view?usp=sharing)
- **Photogrammetry** - Photo archive (`PHOTOS.zip`) needs extraction
- **Network challenges** - PCAP files require analysis
- **Gatecrash** - Classified image needs investigation

## Repository Structure

```
├── CRYPTO/                     # 3/3 solved ✅
│   ├── 3rd-Time-Charm/         # Progressive shift cipher [SOLVED]
│   ├── Journey-Home/           # Image cryptography [SOLVED] 
│   └── Time-Is-Gold/           # Timestamp AES decryption [SOLVED]
├── EXPLOIT/                    # 2/3 solved
│   ├── Gandalf/                # Binary crackme [NEEDS ANALYSIS]
│   ├── Operation-Echo/         # Format string vuln [SOLVED] ✅
│   └── The-Last-Spark/         # Memory dump analysis [SOLVED] ✅
├── FORENSIC/                   # 1/2 solved
│   ├── Operation-LC/           # USB + steganography [SOLVED] ✅
│   └── Photogrammetry/         # Photo analysis [NEEDS ANALYSIS]
├── MISC/                       # 0/1 solved
│   └── Gatecrash/              # Image investigation [NEEDS ANALYSIS]
├── NETWORK/                    # 0/3 solved
│   ├── Command-n-Control/      # C2 traffic analysis [NEEDS ANALYSIS]
│   ├── Encoded-Message/        # Network decoding [NEEDS ANALYSIS]
│   └── MITRE/                  # ATT&CK framework [NEEDS ANALYSIS]
└── WEB/                        # 2/2 solved ✅
    ├── Secure-Archive/         # LFI double encoding [SOLVED] ✅
    └── Warming-Up/             # SQLi + IDOR [SOLVED] ✅
```

## Tools Used Across Challenges

### Cryptography:
- Python 3 with pycryptodome
- Custom cipher analysis scripts
- Timestamp manipulation libraries

### Binary Exploitation:
- Binary Ninja, Ghidra, IDA Pro
- GDB debugging
- Format string exploitation techniques

### Forensics:
- Steghide for steganography
- Mount utilities for disk images
- Archive extraction tools

### Web Security:
- Burp Suite
- SQL injection techniques
- URL encoding/decoding tools

### Network Security:
- Wireshark for PCAP analysis
- Network protocol analyzers
- Traffic pattern analysis tools

## Disclaimer
These writeups are for educational purposes. Please respect the competition rules and don't use these solutions while the CTF is active.

## Contact
Feel free to reach out for questions or discussions about the solutions.

---
**Repository:** [N0Juan/CBCTF25](https://github.com/N0Juan/CBCTF25)  
*Last Updated: 1st September 2025*
