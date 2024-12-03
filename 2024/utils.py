def get_file_output(filename):
    with open(f"input/{filename}", 'r') as f:
        return f.readlines()
