# Snapchat Memories Downloader

This Python script automates the downloading of Snapchat Memories from a locally saved HTML file. It simulates clicking on `<a>` tags within the HTML file to download all media files listed.

## Prerequisites

### 1. **Snapchat Memories Data**
   To use this script, you must first request your Snapchat Memories data from Snapchat's official website. This data will include the `memories_history.html` file needed for the script to work.

### 2. **Python Setup**
   You will need:
   - **Python 3.x** installed on your computer.
   - **Google Chrome** installed on your computer.
   - **ChromeDriver** compatible with your Chrome version.

---

## Step 1: Request Your Snapchat Data

1. **Log in to Snapchat's Account Portal**:
   - Open your browser and go to [https://accounts.snapchat.com/v2/download-my-data](https://accounts.snapchat.com/v2/download-my-data).
   - Log in with your Snapchat credentials.

2. **Select Data Types**:
   - Scroll down and ensure the checkbox that is selected is for **"Memories and Other Media"** .

3. **Request Data**:
   - Follow the next steps on the page (e.g. selecting date range, confirming email etc.), until you can click the **Submit Request/Export** button. Snapchat will notify you that your request is being processed.

4. **Wait for the Email**:
   - Snapchat will email you a link to download your data. This can take anywhere from minutes to several hours or even days, depending on the size of your data.

5. **Download the Data**:
   - When you receive the email, click the link to download the ZIP file containing your data.

6. **Extract the ZIP File**:
   - Extract the ZIP file. Inside, you'll find a folder named something like `mydata ~ [date]`.

7. **Locate the HTML File**:
   - Navigate to the `html` folder within the extracted data.
   - Inside the `html` folder, find the file named `memories_history.html`.

---

## Step 2: Install Python and Required Tools

### 1. **Install Python**:
   - Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - During installation, check the box to **"Add Python to PATH"**.

### 2. **Install Selenium**:
   Open a terminal and run the following command:
   ```bash
   pip install selenium
   ```

### 3. **Download ChromeDriver**:
   - Visit the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Download the version of ChromeDriver that matches your version of Google Chrome.
   - Extract the `chromedriver.exe` file and note its location.

---

## Step 3: Run the Python Script

1. **Download the Script**:
   - Download the Python script provided in this repository, or copy it into a file on your computer named `snapchat-memories-download-script.py`.

2. **Prepare Your Paths**:
   - Locate the following:
     - The **Google Chrome executable** (usually `C:\Program Files\Google\Chrome\Application\chrome.exe`).
     - The **ChromeDriver executable** (where you saved `chromedriver.exe`).
     - The `memories_history.html` file (inside the `html` folder extracted from your Snapchat data).

3. **Run the Script**:
   Open a terminal and navigate to the folder where you saved the script. For example:
   ```bash
   cd C:\Users\YourUsername\Documents
   ```

   Run the script:
   ```bash
   python snapchat-memories-download-script.py
   ```

4. **Provide the Paths**:
   The script will ask you for the following:
   - The full path to your **Google Chrome executable**:
     ```plaintext
     Enter the full path to your Chrome browser executable (e.g., C:\Program Files\Google\Chrome\Application\chrome.exe):
     ```
   - The full path to your **ChromeDriver executable**:
     ```plaintext
     Enter the full path to your ChromeDriver executable (e.g., C:\path\to\chromedriver.exe):
     ```
   - The full path to your `memories_history.html` file:
     ```plaintext
     Enter the full path to the HTML file you want to open (e.g., C:\path\to\file.html):
     ```

5. **Let the Script Run**:
   - The script will open Google Chrome, load the `memories_history.html` file, and begin clicking on the download links for all media files.
   - **Do not close the browser or the terminal** while the script is running.
   - The downloads will continue until all links have been processed.

---

## Step 4: Check Your Downloads

Once the script has finished running:
- All downloaded media files will be in your browser’s default download folder (e.g., `C:\Users\YourUsername\Downloads` on Windows).

---

## Notes and Troubleshooting

1. **Keep the Browser Open**:
   - Do not close Google Chrome or the terminal while the script is running, as this will interrupt the downloading process.

2. **Large Data Sets**:
   - If you have a lot of media, the script might take a long time to process all links. Let it run until it completes.

3. **Chrome Version Mismatch**:
   - If the script fails due to a mismatch between your Chrome version and ChromeDriver, download the correct version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

4. **Headless Mode** (Optional):
   - If you don’t want the browser window to be visible, you can enable **headless mode** by modifying the script:
     ```python
     options.add_argument("--headless")
     ```

5. **Errors**:
   - If the script encounters an error, check the terminal for the error message. Most issues are related to incorrect paths or missing dependencies.

---

## Conclusion

By following these steps, you can automate the process of downloading all your Snapchat Memories from the HTML file provided by Snapchat. This script saves time and ensures that all media files are downloaded without manual effort.

If you encounter any issues, feel free to open an issue 
For Improvements, feel free to open an pull request

---

