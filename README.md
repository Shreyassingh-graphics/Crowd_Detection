# Crowd_Detection

## Author
**Name:** Shreyas Singh  
**Roll Number:** B220032CS  

---

## Overview

This project implements a complete pipeline for **Crowd Detection and Counting** in movie scenes using the **YOLOv5** object detection framework.  
The workflow includes:

- Extracting frames from `.mov` video files
- Annotating frames using Roboflow with Smart Label
- Training a custom YOLOv5 model on the annotated dataset
- Running inference on new scenes to detect and count people
- Saving and visualizing results as labeled videos/images

---

## Technologies Used

- Python 3.10 (virtual environment: `crowd_env`)
- OpenCV for video processing
- YOLOv5 (Ultralytics)
- Roboflow for annotation
- VS Code and Jupyter Notebook for development and testing

---

## Folder Structure

```
Crowd_Detection/
├── scenes/                             # Input .mov video scenes
├── frames/                             # Extracted frames per video
├── all_frames/                         # Combined extracted frames
├── Crowd_Detection_in_movie_scenes/    # YOLOv5 dataset (exported from Roboflow)
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│   └── data.yaml                       # Dataset config file
├── yolov5/                             # YOLOv5 repo (cloned from GitHub)
│   └── runs/
│       └── train/
│           └── crowd_yolov5s*/         # Training logs and weights
│       └── detect/
│           └── crowd_detect/           # Inference results
├── result_videos/                      # Final output videos with detection
├── crowd.py                            # Script to extract frames
├── README.md                           # Project documentation
```

---

## Instructions to Run

### 1. Extract Frames from Videos

Run the Python script to extract frames from all `.mov` videos in the `scenes/` folder.

```bash
python crowd.py
```

This will create:
- `frames/` folder with subfolders for each scene
- `all_frames/` folder containing all extracted images

---

### 2. Annotate Using Roboflow

1. Upload images from `all_frames/` to [Roboflow](https://app.roboflow.com).
2. Use Smart Label to annotate people in the frames.
3. Export the dataset in **YOLOv5 PyTorch format**.
4. Download and extract it into: `Crowd_Detection_in_movie_scenes/`.

---

### 3. Train the YOLOv5 Model

Clone the YOLOv5 repository and install dependencies:

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

Start training:

```bash
python train.py \
  --img 640 \
  --batch 16 \
  --epochs 50 \
  --data ../Crowd_Detection_in_movie_scenes/data.yaml \
  --weights yolov5s.pt \
  --name crowd_yolov5s
```

Trained weights will be saved in:

```
yolov5/runs/train/crowd_yolov5s/weights/best.pt
```

---

### 4. Run Inference

Run detection on new images or scene videos:

```bash
python detect.py \
  --weights runs/train/crowd_yolov5s/weights/best.pt \
  --source ../frames \
  --conf 0.25 \
  --save-txt \
  --save-conf \
  --project runs/detect \
  --name crowd_detect
```

Predicted videos/images are saved in:

```
yolov5/runs/detect/crowd_detect/
```

You can also copy them to the `result_videos/` folder if needed.

---

## Training Results

- Training duration: ~2.77 hours on CPU
- Epochs: 50
- Best mAP@0.5: ~64.6%
- Best mAP@0.5:0.95: ~34.3%
- Precision: 70.1%
- Recall: 57.0%

Visual metrics are available at:
```
yolov5/runs/train/crowd_yolov5s/results.png
```

---

## Output Samples

- Output result videos with bounding boxes are saved in the `result_videos/` folder.
- Sample detections show effective crowd detection across various scene types like rallies, markets, and gatherings.

---

## Conclusion

This project successfully demonstrates:
- End-to-end video processing
- Custom dataset generation and annotation
- Training a YOLOv5 object detector on specific data
- Real-world inference for crowd detection

It can be extended for real-time analysis, safety surveillance, or public space monitoring.

---

## Acknowledgments

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- [Roboflow](https://roboflow.com) for annotation tools
```

---

Let me know if you'd like me to generate this as a downloadable `.md` file or convert it into PDF/Word for submission.
