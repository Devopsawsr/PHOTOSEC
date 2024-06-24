
FROM amazonlinux:2
 
RUN yum install -y python3-pip && \

    pip3 install pandas
 
COPY .github/scripts/trigger_glue_job.py  /etl_script.py
 
ENTRYPOINT ["python3", "/etl_script.py"]

 
