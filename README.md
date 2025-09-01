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
| **CRYPTO** | [Journey Home](CRYPTO/Journey-Home/) | TBD | Easy | ✅ **SOLVED** | Image cryptography |
| **CRYPTO** | [Time Is Gold](CRYPTO/Time-Is-Gold/) | TBD | Hard | ✅ **SOLVED** | Timestamp-based AES decryption |
| **EXPLOIT** | [Operation Echo](EXPLOIT/Operation-Echo/) | 50 | Medium | ✅ **SOLVED** | Format string vulnerability |
| **EXPLOIT** | [The Last Spark](EXPLOIT/The-Last-Spark/) | TBD | Hard | ✅ **SOLVED** | Memory dump XOR decryption |
| **EXPLOIT** | [Gandalf](EXPLOIT/Gandalf/) | TBD | TBD | ❌ **UNSOLVED** | Binary crackme analysis required |
| **FORENSIC** | A Peculiar TV Show | 75 | Medium | ✅ **Pending Writeups** | ??? |
| **FORENSIC** | [Photogrammetry](FORENSIC/Photogrammetry/) | 100 | Medium | ✅ **Pending Writeups** | Archive analysis required |
| **FORENSIC** | [Operation LC](FORENSIC/Operation-LC/) | TBD | Medium | ✅ **SOLVED** | USB forensics + steganography |
| **MISC** | Sanity Check | 25 | Easy | ✅ **SOLVED** | Flag in Discord |
| **MISC** | Share | 50 | Easy | ✅ **Pending Writeups** | Pastebin |
| **MISC** | [Operation Gatecrash](MISC/Gatecrash/) | 75 | Easy | ✅ **Pending Writeups** | Image analysis required |
| **NETWORK** | [Command-n-Control](NETWORK/Command-n-Control/) | TBD | TBD | ✅ **Pending Writeups** | PCAP analysis required |
| **NETWORK** | [Encoded Message](NETWORK/Encoded-Message/) | TBD | TBD | ✅ **Pending Writeups** | MorseCode |
| **NETWORK** | [MITRE](NETWORK/MITRE/) | TBD | TBD | ✅ **Pending Writeups** | ATT&CK framework analysis required |
| **WEB** | [Warming Up](WEB/Warming-Up/) | TBD | Easy/Medium | ✅ **SOLVED** | SQLi + IDOR combination |
| **WEB** | [Secure Archive](WEB/Secure-Archive/) | TBD | Medium | ✅ **SOLVED** | LFI with double URL encoding |
| **WEB** | ??? | TBD | Hard | ❌ **UNSOLVED** | ??? |

## Progress Summary

### By Category:
- **CRYPTO:** 3/3 solved
- **EXPLOIT:** 2/3 solved
- **FORENSIC:** 3/3 solved
- **MISC:** 3/3 solved
- **NETWORK:** 3/3 solved
- **WEB:** 2/3 solved

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

## Disclaimer
These writeups are for educational purposes. Please respect the competition rules and don't use these solutions while the CTF is active.

## Contact
Feel free to reach out for questions or discussions about the solutions.

---
**Repository:** [N0Juan/CBCTF25](https://github.com/N0Juan/CBCTF25)  
*Last Updated: 1st September 2025*
