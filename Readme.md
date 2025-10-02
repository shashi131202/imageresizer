---

# 🖼️ Image Resizer Tool (Simple Version)

A simple Python script to **resize and convert multiple images** in a folder using **Pillow (PIL)**.
This tool always **regenerates the output folder** whenever it runs, so changing the width, height, or format in the script will automatically update the results.

---

## 🚀 Features

* 📂 Reads all images from an **input folder**
* ✂️ Resizes images to **given width & height**
* 🔄 Converts images to **desired format (JPG, PNG, etc.)**
* 💾 Saves processed images in an **output folder**
* ♻️ Clears old outputs each run → always reflects latest script settings

---

## 📂 Project Structure

```
image-resizer/
│── image_resizer.py   # main script
│── images/            # input folder (put your images here)
│── output/            # auto-created output folder (resized images saved here)
│── README.md
```

---

## ⚙️ Installation & Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/image-resizer.git
   cd image-resizer
   ```

2. Install dependencies:

   ```bash
   pip install pillow
   ```

3. Place your images in the `images/` folder.

4. Run the script:

   ```bash
   python image_resizer.py
   ```

---

## 📝 Configuration

In **`image_resizer.py`**, update these values to change output:

```python
resize_images(input_folder="images",
              output_folder="output",
              width=400,
              height=400,
              output_format="PNG")
```

* `width` → Target width in pixels
* `height` → Target height in pixels
* `output_format` → Output format (`JPEG`, `PNG`, etc.)

💡 Every time you change these values, the script clears `output/` and regenerates the resized images.

---

## 🛠 Tech Stack

* **Python 3**
* **Pillow (PIL) library**
* **os, shutil** (for file handling)

---

## 📸 Example

* Input: `images/pic1.jpg` (2000x1500)
* Output: `output/pic1.png` (400x400)

---