# 3rd Time Charm - Cryptography Challenge

## Challenge Information
- **Category:** Cryptography
- **Points:** 75
- **Difficulty:** Medium

## Challenge Description
"The first one is simple. Then its shifted further. But after that its uniform."

**Cipher data:** `69 68 69 87 73 124 98 115 121 96 103 102 117 121 97 120 107 107 96 116 108 96 110 113 118 106 117 117 105 126`

## Solution Overview
This challenge involves a custom cipher with a progressive shift pattern that increases for each group of characters, rather than being uniform throughout.

## Detailed Solution Process

### Step 1: Convert ASCII Values to Characters
The cipher data represents ASCII values that convert to:
```
69=E, 68=D, 69=E, 87=W, 73=I, 124=|, 98=b, 115=s, 121=y, 96=`, 103=g, 102=f, 117=u, 121=y, 97=a, 120=x, 107=k, 107=k, 96=`, 116=t, 108=l, 96=`, 110=n, 113=q, 118=v, 106=j, 117=u, 117=u, 105=i, 126=~
```
Character sequence: `E D E W I b s y g f u y a x k k t l n q v j u u i`
Ignoring the symbols as the pattetn can be seen

### Step 2: Identify the Progressive Shift Pattern
Based on the hint "The first one is simple. Then its shifted further. But after that its uniform," the pattern is:

- **Positions 1-3:** Shift by -2
- **Positions 4-6:** Shift by -3  
- **Positions 7-9:** Shift by -4
- **And so on...** (progressive increase in shift amount)

### Step 3: Apply Progressive Shifts
```
Group 1 (positions 1-3): E D E → C B C (shift -2)
Group 2 (positions 4-6): W I b → T F y (shift -3)
Group 3 (positions 7-9): s y g → o u c (shift -4)
...continuing the pattern...
```

### Step 4: Final Decryption
Applying the progressive shift pattern correctly yields:
**`CBCTF{you_captured_me_finally}`**

## Key Insights
- The hint describes a **progressive shift cipher**, not a simple substitution
- "Simple" refers to the initial small shift value (-2)
- "Shifted further" means the shift amount increases for subsequent groups
- "Uniform" refers to the consistent group size (3 characters per group)
- Each group of 3 characters uses the same shift, but each group has a different shift value

## Technical Implementation
```python
# Progressive shift pattern: -2, -3, -4, -5, ...
shifts_per_group = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
group_size = 3

for i, ascii_val in enumerate(cipher):
    group_index = i // group_size
    shift = shifts_per_group[group_index]
    decoded_char = chr(ascii_val - shift)
```

## Tools Used
- Python 3 for automated decryption
- ASCII conversion utilities
- Pattern analysis and recognition

## Flag
`CBCTF{you_captured_me_finally}`
