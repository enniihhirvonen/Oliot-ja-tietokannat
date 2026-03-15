#!/bin/bash
source .venv/bin/activate
cat > rot18-encrypt << 'EOF'
#!/usr/bin/env python3
import sys

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot18(text):
    out = ""
    for ch in text:
        if ch in LOWER:
            out += LOWER[(LOWER.index(ch) + 13) % 26]
        elif ch in UPPER:
            out += UPPER[(UPPER.index(ch) + 13) % 26]
        elif ch.isdigit():
            out += str((int(ch) + 5) % 10)
        else:
            out += ch
    return out

if __name__ == "__main__":
    message = " ".join(sys.argv[1:])
    print(rot18(message))
EOF

cat > rot18-decrypt << 'EOF'
#!/usr/bin/env python3
import sys

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot18(text):
    out = ""
    for ch in text:
        if ch in LOWER:
            out += LOWER[(LOWER.index(ch) + 13) % 26]
        elif ch in UPPER:
            out += UPPER[(UPPER.index(ch) + 13) % 26]
        elif ch.isdigit():
            out += str((int(ch) + 5) % 10)
        else:
            out += ch
    return out

if __name__ == "__main__":
    message = " ".join(sys.argv[1:])
    print(rot18(message))
EOF

chmod +x rot18-encrypt
chmod +x rot18-decrypt