import json
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# --- KONFIGURASI PATH ---
# Sesuaikan path ini dengan struktur folder kamu
BASE_DIR = Path(__file__).parent.parent  # Mengacu ke folder utama proyek
ANNOTATION_FILE = BASE_DIR / "data" / "annotations" / "export_coco.json"
IMAGE_DIR = BASE_DIR / "images"  # Folder tempat gambar sampel disimpan

# --- WARNA UNTUK TIAP KELAS (Agar konsisten dengan README) ---
COLORS = {
    'Car': '#FF0000',   # Merah
    'Truck': '#FFFF00', # Kuning
    'Bus': '#008000'    # Hijau
}

def load_annotations(json_path):
    """Memuat file anotasi COCO dari Labelbox"""
    with open(json_path, 'r') as f:
        return json.load(f)

def visualize_sample_images(data, num_samples=3):
    """
    Menampilkan sample gambar beserta bounding box-nya.
    """
    images = data['images']
    annotations = data['annotations']
    categories = {cat['id']: cat['name'] for cat in data['categories']}
    
    # Ambil beberapa gambar pertama sebagai sampel
    sample_images = images[:num_samples]
    
    fig, axes = plt.subplots(1, num_samples, figsize=(15, 5))
    
    for idx, img_info in enumerate(sample_images):
        img_filename = img_info['file_name']
        img_path = IMAGE_DIR / img_filename
        
        # Cek apakah file gambar ada di folder images
        if not img_path.exists():
            print(f"Gambar {img_filename} tidak ditemukan di folder {IMAGE_DIR}")
            continue
            
        # Baca gambar menggunakan OpenCV
        image = cv2.imread(str(img_path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Konversi BGR ke RGB untuk Matplotlib
        
        axes[idx].imshow(image)
        axes[idx].set_title(f"Sample {idx+1}: {img_filename}", fontsize=10)
        axes[idx].axis('off')
        
        # Cari semua anotasi untuk gambar ini
        img_id = img_info['id']
        img_annotations = [ann for ann in annotations if ann['image_id'] == img_id]
        
        for ann in img_annotations:
            # Ambil koordinat bounding box [x, y, width, height]
            x, y, w, h = ann['bbox']
            
            # Dapatkan nama kelas
            class_name = categories.get(ann['category_id'], 'Unknown')
            color = COLORS.get(class_name, '#FFFFFF') # Default putih jika kelas tidak terdaftar
            
            # Buat rectangle patch
            rect = patches.Rectangle((x, y), w, h, linewidth=2, edgecolor=color, facecolor='none')
            axes[idx].add_patch(rect)
            
            # Tambahkan label teks di atas kotak
            axes[idx].text(x, y - 5, class_name, color=color, fontweight='bold', fontsize=8, 
                           bbox=dict(facecolor='white', alpha=0.7))

    plt.tight_layout()
    plt.savefig(BASE_DIR / "images" / "visualization_result.png", dpi=300)
    plt.show()
    print("Visualisasi berhasil disimpan di folder images/")

if __name__ == "__main__":
    # Cek apakah file anotasi ada
    if not ANNOTATION_FILE.exists():
        print(f"Error: File anotasi tidak ditemukan di {ANNOTATION_FILE}")
        print("Silakan export data dari Labelbox terlebih dahulu dan simpan di data/annotations/export_coco.json")
    else:
        print("Memuat data anotasi...")
        data = load_annotations(ANNOTATION_FILE)
        print(f"Berhasil memuat {len(data['images'])} gambar dan {len(data['annotations'])} anotasi.")
        
        # Jalankan visualisasi
        visualize_sample_images(data, num_samples=3)