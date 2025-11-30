MAGIC_NUMBERS = {
    b'\x50\x4B\x03\x04': 'zip',
    b'\xFF\xD8\xFF\xDB': 'jpg',
    b'\xFF\xD8\xFF\xE0': 'jpg',
    b'\xFF\xD8\xFF\xEE': 'jpg',
    b'\xFF\xD8\xFF\xE1': 'jpg',
    b'\x89PNG\r\n\x1a\n': 'png',
    b'GIF87a': 'gif',
    b'GIF89a': 'gif',
    b'II*\x00': 'tif',       # little‑endian TIFF
    b'MM\x00\x2A': 'tif',    # big‑endian TIFF
    b'BZh': 'bz2',
    b'\x1F\x8B': 'gz',
    b'Rar!\x1A\x07\x00': 'rar',
    b'Rar!\x1A\x07\x01\x00': 'rar',
    b'\x7FELF': None,        # ELF executable / binary (various extensions)
    b'MZ': 'exe',
    b'\x50\x4B\x05\x06': 'zip',   # empty ZIP archive
    b'\x50\x4B\x07\x08': 'zip',   # spanned ZIP archive
    b'%PDF-': 'pdf',
    b'\x00\x00\x01\x00': 'ico',
    b'\x00\x00\x02\x00': 'cur',
    b'RIFF': 'wav',
    b'OggS': 'ogg',
    b'fLaC': 'flac',
    b'ID3': 'mp3',
    b'\x00\x00\x00\x14ftyp': 'mp4',
    b'ftyp': 'mp4',            # generic MP4/MOV
    b'7z\xBC\xAF\x27\x1C': '7z',
    b'<?xml': 'xml',
    b'<!DOCTYPE html': 'html',
    b'MThd': 'midi',
    b'PK\x03\x04\x14\x00': 'docx',  # also xlsx, pptx
}
