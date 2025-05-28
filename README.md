# 📄 Automated Report Generation

**COMPANY**: CODTECH IT SOLUTION

**NAME**: ALLEN SAM AJI

**INTERN ID**: CT08DL1122

**DURATION**: 8 WEEKS

**MENTOR**: NEELA SANTOSH

---

## Overview  
This project demonstrates how to automate the process of data analysis and report generation using Python. The goal was to read sales data from a CSV file, perform basic analysis such as calculating total and average sales and grouping by region, and then generate a professional-looking PDF report using the **FPDF** library. This task mimics real-world scenarios where businesses frequently need to automate reporting pipelines without relying on spreadsheets or manual formatting.

---

## 🚀 Features  
- 📁 Reads structured data from a `.csv` file  
- 📊 Performs aggregate analysis: total, average, and grouped values  
- 📝 Automatically generates a clean, formatted PDF report  
- 🧩 Designed for easy extension with additional metrics or styling  
- ✅ Compatible with any system (no emoji issues like previous task)  

---

## 🛠 Technologies Used  
- **Python 3**  
- **Pandas** – for data handling and analysis  
- **FPDF** – for creating PDF documents  
- **CSV** – for storing and loading tabular data  

---

## 🧪 How to Run  

1. Clone the repo or download the script.
2. Place a file named `data.csv` in the same folder as the script.  
3. Use this sample structure for the CSV:
   ```csv
   Name,Sales,Region
   Alice,300,North
   Bob,450,South
   Charlie,200,East
   David,350,West
   Eva,500,North
   
4. Install the required libraries:
   ```bash
   pip install pandas fpdf

5. Run the script:
   ```bash
   python generate_report.py

---

## Objective
The objective was to simulate a typical business scenario where regular reports need to be created automatically from structured data. Instead of manually copying data into Excel or Word, the script performs this end-to-end—reading raw data, computing analytics, and exporting a readable, shareable PDF report. This kind of automation is commonly used in corporate dashboards, performance summaries, and client-facing documentation.

---

## Implementation Process
The process began by designing a structure for the input data. A sample CSV file was created containing names, sales values, and regions. Pandas was used to read the CSV into a DataFrame and to calculate the total sales, average sales, and regional breakdowns. These operations were chosen as they are representative of common business KPIs (Key Performance Indicators).

We then moved on to the PDF generation. The FPDF library was chosen due to its simplicity and control over layout. After adding a title to the report, the script wrote each analysis result as a new line in the PDF. A clear distinction was made between overall metrics (total and average sales) and group-level analytics (sales by region).

Special attention was given to layout, font sizes, and spacing to make the document both readable and professional. The script was written to be reusable; the file path and output name can easily be customized.

During development, we faced some terminal compatibility issues—especially Unicode-related errors due to emojis (like magnifying glass and checkmarks) not rendering properly in Windows' default encoding (cp1252). This was resolved by removing emojis from print statements, ensuring the script runs on any system regardless of encoding.

Additionally, a file path error (FileNotFoundError) occurred when the CSV file was missing or incorrectly referenced. This was resolved by using an absolute path with raw string syntax (r"..."), or by ensuring the file exists in the working directory.

---

## Conclusion
This task provided hands-on experience with data automation, file handling, and report generation using Python. It not only covered technical aspects like using pandas and fpdf, but also reflected real-life problems such as encoding errors and file I/O issues. The script is a foundational template for any scenario where automated reporting is needed.

Whether you’re working in sales, marketing, operations, or analytics, this solution can be adapted to generate regular reports—saving time and reducing human error. The project also reinforces the power of Python as a tool for both data processing and user-friendly output formatting.

---

## Output
A sample output PDF is generated named sales_report.pdf with the following content:

Title: Sales Report

Total Sales

Average Sales

Sales grouped by region

You can open the PDF using any standard reader (Adobe, browser, etc.).

![Image](https://github.com/user-attachments/assets/44dab0f2-6020-47c1-8b41-37bcebe6c149)

---

## License
This project is open for educational use and modification. Attribution appreciated but not required.
   
