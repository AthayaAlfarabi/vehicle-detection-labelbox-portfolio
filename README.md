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
│   └── annotations/          # Contains exported annotation files from Labelbox
│       └── export_coco.json  # Main annotation file in NDJSON/COCO format
── docs/
│   └── annotation_guidelines.pdf # Comprehensive guidelines for labeling consistency (Ontology & Rules)
├── images/
│   ├── Pias (526).jpg        # Sample raw images used for visualization demo
│   ├── Pias (520).jpg
│   └── visualization_result.png # Output image showing bounding boxes on sample data
├── notebooks/
│   └── eda_labelbox.ipynb    # Jupyter Notebook for Exploratory Data Analysis (EDA) and class distribution stats
├── scripts/
│   └── visualize_annotations.py # Python script to parse JSON and visualize bounding boxes on images
├── .gitignore                # Git configuration to exclude large raw datasets and temporary files
└── README.md                 # Main documentation file for the project