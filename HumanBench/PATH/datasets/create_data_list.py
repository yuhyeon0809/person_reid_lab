import os
import glob

base_path = "/home/youhyun/Volume/research/reid_lab/person_reid_lab/HumanBench/PATH/datasets/market1501/Market-1501"
query_path = os.path.join(base_path, "query")
gallery_path = os.path.join(base_path, "bounding_box_test")
output_dir = os.path.join(base_path, "data_list")

os.makedirs(output_dir, exist_ok=True)

query_files = glob.glob(os.path.join(query_path, "*.jpg"))
with open(os.path.join(output_dir, "query_list.txt"), "w") as f:
    for img_path in query_files:
        filename = os.path.basename(img_path)
        parts = filename.split('_')
        person_id = int(parts[0])
        camera_id = int(parts[1][1])
        
        f.write(f"{img_path} {person_id} {camera_id}\n")

gallery_files = glob.glob(os.path.join(gallery_path, "*.jpg"))
gallery_files = [f for f in gallery_files if not os.path.basename(f).startswith("-1")]  
with open(os.path.join(output_dir, "gallery_list.txt"), "w") as f:
    for img_path in gallery_files:
        filename = os.path.basename(img_path)
        parts = filename.split('_')
        person_id = int(parts[0])
        camera_id = int(parts[1][1])
        
        f.write(f"{img_path} {person_id} {camera_id}\n")

print(f"생성 완료: {os.path.join(output_dir, 'query_list.txt')}")
print(f"생성 완료: {os.path.join(output_dir, 'gallery_list.txt')}")