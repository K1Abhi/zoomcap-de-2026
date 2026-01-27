#### Question 1. What's the version of pip in the python:3.13 image?

```shell
> docker run -it --entrypoint=bash python:3.13

root@97bc649207fe:/# pip -V
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```
- Solution is : **pip 25.3**
---

#### Question 2. Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?
<img width="391" height="577" alt="image" src="https://github.com/user-attachments/assets/ba6930c3-07f0-4704-bad7-cf872066abac" />  <br>
- Solution is : `postgres:5432`
---
#### Question 3. For the trips in November 2025 (`lpep_pickup_datetime between '2025-11-01' and '2025-12-01'`, exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?
```sql
select count(*) from public.green_taxi_data
where lpep_pickup_datetime between '2025-11-01' and '2025-12-01'
and trip_distance <=1
```
- Solution is: **8007**'
---
#### Question 4. Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).
```sql
select date(lpep_pickup_datetime), max(trip_distance) from public.green_taxi_data
where trip_distance <100
group by 1
order by 2 desc
```
- Solution is: **2025-11-14**'
---
#### Question 5 Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?
```sql
select b.zone,sum(total_amount)from public.green_taxi_data a
left join public.taxi_zones b
on a."PULocationID" = b.location_id
where date(lpep_pickup_datetime) = '2025-11-18'
group by 1
order by 2 desc
```
- Solution is: **East Harlem North**'
---
#### Question 6. For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

```sql
select  b.zone, max(tip_amount) from public.green_taxi_data a
left join public.taxi_zones b
on a. "DOLocationID" = b.location_id
left join public.taxi_zones c
on a. "PULocationID" = c.location_id
where date(lpep_pickup_datetime) between '2025-11-01' and '2025-12-01'
and c.zone = 'East Harlem North'
group by 1
order by 2 desc
```
- Solution is: **Yorkville West**'
