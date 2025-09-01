#!/usr/bin/env python3

# Cipher from the challenge
cipher = [69, 68, 69, 87, 73, 124, 98, 115, 121, 96, 103, 102, 117, 121, 97, 120, 107, 107, 96, 116, 108, 96, 110, 113, 118, 106, 117, 117, 105, 126]

# Expected flag format starts with CBCTF{
# C = 67, B = 66, C = 67, T = 84, F = 70, { = 123

def try_decode():
    results = []
    
    # Try different shift patterns based on the hint:
    # "The first one is simple. Then its shifted further. But after that its uniform."
    
    # Let's assume:
    # - First char: shift by 2 (simple)
    # - Second char: shift by 2 (simple) 
    # - Third char: shift by 2 (simple)
    # - Fourth char: shift by 3 (shifted further)
    # - Fifth char: shift by 4 (shifted further)
    # - Rest: uniform shift
    
    for uniform_shift in range(1, 26):
        decoded = []
        
        # Pattern: 2, 2, 2, 3, 4, then uniform
        shifts = [2, 2, 2, 3, 4] + [uniform_shift] * (len(cipher) - 5)
        
        for i, (val, shift) in enumerate(zip(cipher, shifts)):
            decoded_char = val - shift
            if 32 <= decoded_char <= 126:  # printable ASCII
                decoded.append(chr(decoded_char))
            else:
                decoded.append(f'[{decoded_char}]')
        
        result = ''.join(decoded)
        if result.startswith('CBCTF'):
            results.append((shifts[:5], uniform_shift, result))
    
    return results

# Try the basic pattern
results = try_decode()
if results:
    print("Found potential solutions:")
    for pattern, uniform, result in results:
        print(f"Pattern {pattern} + uniform {uniform}: {result}")
else:
    print("No solutions found with basic pattern. Trying more variations...")
    
    # Try different initial patterns
    for shift1 in range(1, 10):
        for shift2 in range(1, 10):
            for shift3 in range(1, 10):
                for uniform_shift in range(1, 26):
                    decoded = []
                    
                    # Pattern: shift1, shift2, shift3, then uniform
                    shifts = [shift1, shift2, shift3] + [uniform_shift] * (len(cipher) - 3)
                    
                    valid = True
                    for i, (val, shift) in enumerate(zip(cipher, shifts)):
                        decoded_char = val - shift
                        if 32 <= decoded_char <= 126:  # printable ASCII
                            decoded.append(chr(decoded_char))
                        else:
                            valid = False
                            break
                    
                    if valid:
                        result = ''.join(decoded)
                        if result.startswith('CBCTF'):
                            print(f"Pattern [{shift1}, {shift2}, {shift3}] + uniform {uniform_shift}: {result}")