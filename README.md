# Twitter Hashtag Analysis Using MapReduce

## **Project Overview**
This mini project applies basic analysis on a **2.7 TB dataset** containing geotagged tweets, monitoring **coronavirus-related social media activity**. Using a **MapReduce** procedure, the primary goal of this project was to **parallelize data extraction for efficiency**.

Extracting the **country, language, and hashtags** from each tweet, I consolidate the data into **<50KB summarized JSON files**, then generate a series of visualizations using `visualize.py` and `alternative_reduce.py`.

Below are the **Top 10 countries and languages for `#coronavirus` and `#코로나바이러스`**, along with a **time series graph** showing the number of tweets for each hashtag over time.

---

## **Results**
### 🔹 **Top 10 Languages for `#coronavirus`**
![Top 10 Languages for #coronavirus](output/coronavirus_all_lang.json.png)

### 🔹 **Top 10 Languages for `#코로나바이러스`**
*(Note: Matplotlib does not fully support Korean text, so some characters may not display correctly.)*  
![Top 10 Languages for #코로나바이러스](output/코로나바이러스_all_lang.json.png)

### 🔹 **Top 10 Countries for `#coronavirus`**
![Top 10 Countries for #coronavirus](output/coronavirus_all_country.json.png)

### 🔹 **Top 10 Countries for `#코로나바이러스`**
![Top 10 Countries for #코로나바이러스](output/코로나바이러스_all_country.json.png)

### 🔹 **Hashtag Trends Over Time**
This line chart shows the daily number of tweets containing #coronavirus and #flu, demonstrating social media trends over time throughout 2020. The trend reflects how frequently each hashtag appeared over the course of the year.
![Hashtag Trends](output/hashtag_trend.png)

---

## **How to Run the Pipeline**
### **1️⃣ Run the Mapper**
```bash
nohup ./run_maps.sh > run_maps_master.log 2>&1 &
```
This processes all dataset files in parallel and saves results in `output/`.

### **2️⃣ Run the Reducer**
```bash
python3 src/reduce.py --input_paths output/*.lang --output_path output/all_lang.json
python3 src/reduce.py --input_paths output/*.country --output_path output/all_country.json
```
This consolidates extracted language and country data into summarized JSON files.

### **3️⃣ Generate Visualizations**
```bash
python3 src/visualize.py --input_path output/all_lang.json --key "#coronavirus"
python3 src/visualize.py --input_path output/all_lang.json --key "#코로나바이러스"
python3 src/visualize.py --input_path output/all_country.json --key "#coronavirus"
python3 src/visualize.py --input_path output/all_country.json --key "#코로나바이러스"
```
This generates **bar charts** for the most frequently used **languages and countries** for each hashtag.

### **4️⃣ Generate Alternative Reduce Analysis**
```bash
python3 src/alternative_reduce.py --hashtags "#coronavirus" "#flu" --output_path output/hashtag_trend.png
```
This creates a **time series line plot** showing how frequently each hashtag appears over time.

---

## **Key Features**
- **MapReduce-inspired architecture** for processing Twitter data efficiently.
- **Parallel processing using `nohup`** to handle large datasets.
- **Summarized JSON output** (<50KB per file) for easy analysis.
- **Visualizations of social media trends** in multiple languages and countries.

---

