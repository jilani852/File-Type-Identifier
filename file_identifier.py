import sys

SIGNATURES = [
    # (name, extension, magic_bytes)
    ("JPEG Image",      ".jpg",  [0xFF, 0xD8, 0xFF]),
    ("PNG Image",       ".png",  [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
    ("PDF Document",    ".pdf",  [0x25, 0x50, 0x44, 0x46]),
    ("ZIP Archive",     ".zip",  [0x50, 0x4B, 0x03, 0x04]),
    ("GIF Image",       ".gif",  [0x47, 0x49, 0x46, 0x38]),
    ("MP3 Audio",       ".mp3",  [0x49, 0x44, 0x33]),
    ("ELF Executable",  ".elf",  [0x7F, 0x45, 0x4C, 0x46]),
    ("Windows EXE",     ".exe",  [0x4D, 0x5A]),
    ("BMP Image",       ".bmp",  [0x42, 0x4D]),
    ("7-Zip Archive",   ".7z",   [0x37, 0x7A, 0xBC, 0xAF, 0x27, 0x1C]),
]

def read_header(file_path):
    with open(file_path,"rb") as f:
        header = f.read(16)
    return header

def comparasion(header,SIGNATURES):
    header = list(header)
    test = False
    for name,extension,signature in SIGNATURES:
        sig_length = len(signature)
        if header[:sig_length] == signature:
            print("File type :",name)
            print("File extension :",extension)
            test = True
            break
    if not test:
        print("Unrecognized file type")
    




if len(sys.argv)<2:
    print("Usage: python file_identifier.py <file_path>")
    sys.exit(1)
file_path = sys.argv[1]
header = read_header(file_path)
comparasion(header,SIGNATURES)