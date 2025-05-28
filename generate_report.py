import pandas as pd
from fpdf import FPDF

def load_data(file_path):
    return pd.read_csv(file_path)

def analyze_data(df):
    total_sales = df["Sales"].sum()
    average_sales = df["Sales"].mean()
    sales_by_region = df.groupby("Region")["Sales"].sum().to_dict()
    return total_sales, average_sales, sales_by_region

def generate_pdf_report(total_sales, average_sales, sales_by_region, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Sales Report", ln=True, align="C")

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Total Sales: ${total_sales}", ln=True)
    pdf.cell(0, 10, f"Average Sales: ${average_sales:.2f}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Sales by Region:", ln=True)

    pdf.set_font("Arial", "", 12)
    for region, sales in sales_by_region.items():
        pdf.cell(0, 10, f" - {region}: ${sales}", ln=True)

    pdf.output(output_file)

def main():
    file_path = r"C:\\Users\\User\Desktop\\Intership tasks\\Task 2\\data.csv"
    output_pdf = "sales_report.pdf"
    
    print("Reading data...")
    df = load_data(file_path)

    print("Analyzing data...")
    total_sales, average_sales, sales_by_region = analyze_data(df)

    print("Generating PDF report...")
    generate_pdf_report(total_sales, average_sales, sales_by_region, output_pdf)

    print(f"Report generated: {output_pdf}")

if __name__ == "__main__":
    main()
