import os 

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower().replace('.','')


def compare_extension_and_type(file_path, detect_type):
    ext = get_file_extension(file_path)
    if detect_type.lower() !=ext:
        print(f"Warning: Extension '{ext}' does not match detected type '{detect_type}'")
    else:
        print(f"Approval: Extension '{ext}' does match detected type '{detect_type}'")


