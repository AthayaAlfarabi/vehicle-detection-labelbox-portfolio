# 🚗 Vehicle Detection Dataset - Labelbox Portfolio

## 📋 Overview
This project involves the creation of a custom vehicle detection dataset using **Labelbox**. The dataset consists of **2,357 dashcam images** captured from Indonesian roads, annotated with a multi-class ontology to support object detection models like YOLOv8.

## 🎯 Project Goals
- Build a high-quality annotated dataset for vehicle detection in local traffic conditions.
- Implement a robust annotation workflow using Labelbox's ontology features.
- Provide a clean, structured dataset ready for training computer vision models.

## ️ Annotation Schema
We used a **flat multi-class approach** with 4 distinct vehicle types for optimal model performance:

| Class | Bounding Box Color | Description |
|-------|-------------------|-------------|
| `Car` | 🔵 Blue | Sedans, hatchbacks, SUVs, sports |
| `Bus` | 🟢 Green | Public transport buses, minibus |
| `Truck` | 🟡 Yellow | Cargo trucks, container trucks, pickups |

### Why Flat Classes?
- Better compatibility with standard models (YOLO, Faster R-CNN)
- Easier visual quality control during labeling
- Granular evaluation metrics per class

## 📊 Dataset Statistics
- **Total Images:** 2,357
- **Annotation Format:** COCO JSON / YOLO TXT (available in `/data/annotations`)
- **Class Distribution:**
  - Car: ~XX% *(Update after labeling)*
  - SUV: ~XX%
  - Bus: ~XX%
  - Truck: ~XX%

## 🛠️ Tools & Technologies
- **Annotation Tool:** Labelbox
- **Dataset Source:** Dashcam footage
- **Export Format:** COCO, YOLO
- **Analysis:** Python, Pandas, Matplotlib

## 📁 Repository Structure
```text
vehicle-detection-labelbox-portfolio/
├── data/
│   └── annotations/          # Folder berisi file export JSON dari Labelbox
│       └── export_coco.json  # File anotasi utama (format NDJSON/COCO)
├── docs/
│   └── annotation_guidelines.pdf # Dokumentasi aturan labeling (Ontology & Rules)
── images/
│   ├── Pias (526).jpg        # Sample gambar asli untuk visualisasi
│   ├── Pias (520).jpg
│   ── visualization_result.png # Hasil output script visualisasi bounding box
├── notebooks/
│   └── eda_labelbox.ipynb    # Notebook untuk analisis statistik dataset (EDA)
├── scripts/
│   ── visualize_annotations.py # Script Python untuk memvisualisasikan hasil label
├── .gitignore                # Konfigurasi file/folder yang diabaikan oleh Git
└── README.md                 # Dokumentasi utama proyek ini
