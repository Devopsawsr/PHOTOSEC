import boto3
 
def trigger_glue_job(glue_job_name):
    """
    Triggers an AWS Glue job.
 
    Parameters:
    - glue_job_name: Name of the AWS Glue job to trigger.
 
    Returns:
    - run_id: ID of the triggered job run.
    """
    # Create a Glue client
    glue_client = boto3.client('glue')
    # Trigger the Glue job
    response = glue_client.start_job_run(
        JobName=glue_job_name
    )
 
    # Extract the run ID from the response
    run_id = response['JobRunId']
    return run_id
 
if __name__ == "__main__":
    # Replace 'your_glue_job_name' with the actual name of your Glue job
    job_name = 'your_glue_job_name'
    run_id = trigger_glue_job(job_name)
    print("Started Glue job run with ID:", run_id)
