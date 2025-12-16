# Folder File Organizer Automation

## Problem
Many users keep all files in a single folder (such as Downloads or Desktop),
which makes file management difficult, time-consuming, and unorganized.

## Solution
This Python automation script organizes files into separate folders
based on their file types (PDFs, Images, Documents, Videos, etc.).
It helps users keep their folders clean and structured automatically.

1. Installation Section:
## Installation

No external packages required! Uses only Python standard library.

```bash
python --version  # Python 3.6+

**2. Example Output:**
```markdown
## Example Output
Organizing files...
✓ Moved: photo1.jpg → Images/
✓ Moved: document.pdf → Documents/
✓ Moved: video.mp4 → Videos/
✓ Moved: report.docx → Documents/
Summary:
Images: 2 files
Documents: 2 files
Videos: 1 file
Organization complete!

3. Supported File Types:
## Supported File Types

| Category | Extensions |
|----------|------------|
| Images | .jpg, .png, .jpeg, .gif, .bmp |
| Documents | .pdf, .docx, .txt, .xlsx, .pptx |
| Videos | .mp4, .mkv, .avi, .mov |
| Audio | .mp3, .wav, .flac |
| Archives | .zip, .rar, .7z |
| Code | .py, .js, .html, .css |

## Tools Used
- Python
- os / shutil

## How to Run
1. Place the script inside the target folder
2. Run the command: python organizer.py
3. Files will be automatically organized into folders

## Use Cases
- Office staff handling daily files
- Freelancers managing project files
- Students organizing study materials
- Small businesses managing documents

## Future Improvements
- Custom folder rules
- GUI-based version

## Screenshots

### Before Automation
![Before](screenshots/before_run.jpg)

### After Automation
![After](screenshots/after_run.jpg)
