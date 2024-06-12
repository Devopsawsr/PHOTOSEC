import sys
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
    if len(sys.argv) < 2:
        print("Usage: python trigger_glue_job.py <glue_job_name>")
        sys.exit(1)

    job_name = sys.argv[1]
    run_id = trigger_glue_job(job_name)
    print("Started Glue job run with ID:", run_id)
