Question 1:
Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.

What's the version of pip in the image?Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.

What's the version of pip in the image?

Answer 1:
pip 24.3.1

Question 2:
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

Answer 2:
localhost:5432

Question 3:
During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, respectively, happened:

    Up to 1 mile
    In between 1 (exclusive) and 3 miles (inclusive),
    In between 3 (exclusive) and 7 miles (inclusive),
    In between 7 (exclusive) and 10 miles (inclusive),
    Over 10 miles

Answer 3:
Up to 1 mile - 1048,38
In between 1 (exclusive) and 3 miles (inclusive) - 1990,13
In between 3 (exclusive) and 7 miles (inclusive) - 109,645
In between 7 (exclusive) and 10 miles (inclusive) - 27,688
Over 10 miles - 35,202

Question 4:
Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

Answer 4:
2019-10-31 - 515,89

Question 5:
Which were the top pickup locations with over 13,000 in total_amount (across all trips) for 2019-10-18?

Answer 5:
select 
gt.total_amount,
zl."Zone"
from green_taxi as gt
inner join
zone_lookup as zl
on gt."PULocationID" = zl."LocationID"
where cast(gt.lpep_pickup_datetime as date) = '2019-10-18'
group by 
gt.total_amount,
zl."Zone"
having sum(gt.total_amount) > 13000;

Queston 6:
For the passengers picked up in October 2019 in the zone named "East Harlem North" which was the drop off zone that had the largest tip?

Answer 6:
select 
gt.tip_amount,
gt."DOLocationID",
zl."Zone"
from green_taxi as gt
inner join
zone_lookup as zl
on gt."DOLocationID" = zl."LocationID"
group by gt.tip_amount, gt."DOLocationID", zl."Zone"
having zl."Zone" = 'East Harlem North'
order by gt.tip_amount
desc;

Question 7:
Which of the following sequences, respectively, describes the workflow for:

    Downloading the provider plugins and setting up backend,
    Generating proposed changes and auto-executing the plan
    Remove all resources managed by terraform`

Answer 7:
terraform init, terraform apply -auto-approve, terraform destroy
