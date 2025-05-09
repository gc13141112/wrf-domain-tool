import os

def add_init_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        if '__pycache__' in dirpath:
            continue
        if '__init__.py' not in filenames:
            init_path = os.path.join(dirpath, '__init__.py')
            open(init_path, 'a').close()
            print(f"Created: {init_path}")

# 替换为你的代码目录
add_init_files('wrf_domain_tool')
