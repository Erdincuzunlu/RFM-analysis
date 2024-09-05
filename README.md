# RFM-analysis
customer-segmentation-with-rfm
Customer Segmentation with RFM

Project Overview

This project focuses on segmenting customers for an e-commerce company using RFM (Recency, Frequency, Monetary) analysis. By categorizing customers into different segments, the company can tailor its marketing strategies more effectively.

Problem Statement

The e-commerce company aims to segment its customers based on their purchasing behavior and develop targeted marketing strategies. The main goal is to maximize customer engagement and increase sales.

Dataset

The dataset used is called “Online Retail II”, which contains transactions from an online retail store based in the UK. The data covers the period between 01/12/2009 and 09/12/2011.

Variables:

	•	InvoiceNo: Unique invoice number for each transaction.
	•	StockCode: Unique product code.
	•	Description: Product description.
	•	Quantity: Number of products per transaction.
	•	InvoiceDate: Date of the transaction.
	•	UnitPrice: Unit price of each product.
	•	CustomerID: Unique identifier for each customer.
	•	Country: Country of the customer.

Analysis Steps

	1.	Business Understanding: Understanding the purpose of the project and business goals.
	2.	Data Understanding: Exploring and cleaning the dataset.
	3.	Data Preparation: Handling missing values and outliers, preparing the data for analysis.
	4.	Calculating RFM Metrics: Computing Recency, Frequency, and Monetary values for each customer.
	5.	Calculating RFM Scores: Assigning scores based on quantiles for R, F, and M metrics.
	6.	Creating and Analyzing RFM Segments: Segmenting customers and analyzing the results.

Results

Customers were segmented into groups such as Champions, At Risk, and New Customers, allowing for targeted marketing approaches to each segment.

Requirements

To run the code, you’ll need the following Python packages:

	•	pandas
	•	numpy
	•	datetime

git clone https://github.com/yourusername/customer-segmentation-rfm.git

2.	Run the Jupyter notebook or Python script to see the full analysis.

File Structure

	•	customer_segmentation.ipynb: Jupyter notebook containing the complete analysis.
	•	new_customers.csv: CSV file containing the list of new customers identified during the analysis.

Future Work

	•	Expand the segmentation to other periods.
	•	Test different methods for customer segmentation.



