def read_file_bytes(file_path,num_bytes = 8):
    try:
        with open(file_path, 'rb') as f:
            file_header = f.read(num_bytes)
        return file_header
    except Exception as e:
        print(f"Error reading file {file_path}:{e}")
        return None