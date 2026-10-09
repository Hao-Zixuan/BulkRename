# '''用完记得注释'''

# from pathlib import Path

# base_dir = Path("Images") / "新建文件夹"     #改文件夹名
# i = 1          #如有必要，改初始页码

# for path in sorted(base_dir.glob("*.jpg")):         #如有必要，改文件类型
#     new_path = base_dir / f"The_Farthest_Land_{i:05d}.jpg"      #改文件名
#     path.rename(new_path)
#     i += 1