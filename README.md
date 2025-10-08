# Captcha Detection Project

This project provides a complete pipeline for collecting, labeling, and training models to detect and solve captchas from websites. It includes tools for scraping captcha images, labeling them, and building an OCR/CRNN model for automated recognition.

## Project Workflow

1. **Scrape Captcha Images**
	- Use the provided scraper script to collect captcha images from the target website.
	- Images are saved in `data/images/`.

2. **Label Captcha Images**
	- Use the labeling tool to annotate the collected images with their correct text.
	- Labeling progress is tracked in `data/labeling_state.csv`.

3. **Train OCR/CRNN Model**
	- Use labeled images to train an OCR/CRNN model for captcha recognition.
	- Model files and training scripts are located in the `model/` and `scripts/` folders.

4. **Evaluate and Improve**
	- Test the trained model on new captchas and refine the pipeline as needed.

## Setup Instructions

1. Clone the repository:
	```cmd
	git clone https://github.com/MAA5524/captcha_detection.git
	```

2. Install required Python packages:
	```cmd
	pip install -r requirements.txt
	```

3. Configure scraping and labeling settings in the `config/` folder.

## Usage Guide

### 1. Scraping Captchas
Run the scraper script to download captcha images:
```cmd
python scripts/scraper.py
```

### 2. Labeling Images
Run the labeling tool to annotate images:
```cmd
python tools/labeler.py
```

### 3. Training the Model
Train the OCR/CRNN model using labeled data. See scripts in `model/` and `scripts/` for details.

## Folder Structure

- `config/` — Configuration files
- `data/images/` — Raw captcha images
- `data/labeling_state.csv` — Labeling progress
- `data/processed/` — Processed data
- `model/` — Model files and checkpoints
- `scripts/` — Scraper and training scripts
- `tools/` — Labeling tool
- `utils/` — Utility functions

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the MIT License.