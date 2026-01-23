from pathlib import Path


curr_dir = Path.cwd()
current_file = Path(__file__).name


print(f"Files in {curr_dir}:")


for filepath in curr_dir.iterdir():
    
    if filepath.name == current_file:
        continue
    print(f" --> {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding = 'utf-8')
        print(f"Content: {content}")










