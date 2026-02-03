## Workflow Orchestration: Homework

**Question 1.** Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?               


<img width="1013" height="104" alt="image" src="https://github.com/user-attachments/assets/e99cca2f-036e-40b5-aeee-bd2ac08b231a" />      

---

**Question 2.** What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?                          

**Solution:** : `green_tripdata_2020-04.csv`           

---
 
**Question 3.** How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?                            

**Solution**: Similar to question 4           

---
 
Question 4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?     

**Solution:**
Used backfill to load all the data for green taxi for the year 2020    
<img width="1471" height="490" alt="image" src="https://github.com/user-attachments/assets/a4015996-defa-4558-b48e-87b4e5dcd057" />
<img width="411" height="187" alt="image" src="https://github.com/user-attachments/assets/2b2f8269-a82d-4346-9950-c7daa87ebfb9" />

---
**Question 5.** How many rows are there for the Yellow Taxi data for the March 2021 CSV file?      

**Solution**: Similar to question 4   

---        
**Question 6**. How would you configure the timezone to New York in a Schedule trigger?       
**Solution**: Add a timezone property set to America/New_York in the Schedule trigger configuration
