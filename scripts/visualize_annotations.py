import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
import urllib.request

# --- KONFIGURASI PATH ---
BASE_DIR = Path(__file__).parent.parent
ANNOTATION_FILE = BASE_DIR / "data" / "annotations" / "export_coco.json"
OUTPUT_DIR = BASE_DIR / "images"

# --- WARNA UNTUK TIAP KELAS ---
COLORS = {
    'Car': '#FF0000',   # Merah
    'Truck': '#FFFF00', # Kuning
    'Bus': '#008000'    # Hijau
}

def load_ndjson_annotations(json_path):
    """Memuat file anotasi NDJSON dari Labelbox"""
    data_rows = []
    with open(json_path, 'r') as f:
        for line in f:
            if line.strip():
                data_rows.append(json.loads(line))
    return data_rows

def visualize_sample_images(data_rows, num_samples=3):
    """
    Menampilkan sample gambar beserta bounding box-nya menggunakan URL dari Labelbox.
    """
    if not data_rows:
        print("Tidak ada data anotasi yang ditemukan.")
        return

    # Ambil beberapa data row pertama sebagai sampel
    samples = data_rows[:num_samples]
    
    fig, axes = plt.subplots(1, len(samples), figsize=(15, 5))
    if len(samples) == 1:
        axes = [axes]

    for idx, row in enumerate(samples):
        # Ambil URL gambar dari data_row
        img_url = row['data_row']['row_data']
        external_id = row['data_row'].get('external_id', f'Image_{idx}')
        
        try:
            # Download gambar dari URL Labelbox
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                image_bytes = np.asarray(bytearray(response.read()), dtype=np.uint8)
                image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(f"Gagal memuat gambar {external_id}: {e}")
            continue
            
        axes[idx].imshow(image)
        axes[idx].set_title(f"Sample {idx+1}: {external_id}", fontsize=10)
        axes[idx].axis('off')
        
        # Proses Labels (Objects)
        labels = row.get('labels', [])
        if not labels:
            continue
            
        # Ambil label terbaru (biasanya index terakhir jika ada review)
        latest_label = labels[-1]
        objects = latest_label.get('objects', [])
        
        for obj in objects:
            # Ambil koordinat bounding box
            bbox = obj.get('bounding_box', {})
            if not bbox:
                continue
                
            x = bbox.get('left', 0)
            y = bbox.get('top', 0)
            w = bbox.get('width', 0)
            h = bbox.get('height', 0)
            
            # Dapatkan nama kelas
            class_name = obj.get('name', 'Unknown')
            color = COLORS.get(class_name, '#FFFFFF')
            
            # Buat rectangle patch
            rect = patches.Rectangle((x, y), w, h, linewidth=2, edgecolor=color, facecolor='none')
            axes[idx].add_patch(rect)
            
            # Tambahkan label teks
            axes[idx].text(x, y - 5, class_name, color=color, fontweight='bold', fontsize=8, 
                           bbox=dict(facecolor='white', alpha=0.7))

    plt.tight_layout()
    output_path = OUTPUT_DIR / "visualization_result.png"
    plt.savefig(output_path, dpi=300)
    plt.show()
    print(f"Visualisasi berhasil disimpan di: {output_path}")

if __name__ == "__main__":
    if not ANNOTATION_FILE.exists():
        print(f"Error: File anotasi tidak ditemukan di {ANNOTATION_FILE}")
    else:
        print("Memuat data anotasi NDJSON...")
        data_rows = load_ndjson_annotations(ANNOTATION_FILE)
        print(f"Berhasil memuat {len(data_rows)} data rows.")
        
        if len(data_rows) > 0:
            visualize_sample_images(data_rows, num_samples=3)
        else:
            print("File JSON kosong atau tidak memiliki data valid.")