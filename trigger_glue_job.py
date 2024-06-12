import os
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
    # Get the Glue job name from the environment variable
    job_name = os.environ.get('GITHUB_JOB_NAME')

    if not job_name:
        print("Error: Environment variable GITHUB_JOB_NAME is not set.")
        sys.exit(1)

    # Trigger the Glue job
    run_id = trigger_glue_job(job_name)

    # Print the job run ID
    print("Started Glue job run with ID:", run_id)
