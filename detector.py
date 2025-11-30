from magic_dic import MAGIC_NUMBERS

def detect_file_type(file_bytes):
    if not file_bytes:
        return 'Unknown'
    for magic, ftype in MAGIC_NUMBERS.items():
        if file_bytes.startswith(magic):
            return ftype 
    return 'unknown'