import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def create_invalidation(distribution_id, paths):
    """
    Creates an invalidation in the specified CloudFront distribution.

    :param distribution_id: The ID of the CloudFront distribution.
    :param paths: A list of paths to invalidate (e.g., ['/index.html', '/images/*']).
    """
    # Initialize the CloudFront client
    cloudfront_client = boto3.client('cloudfront')

    try:
        # Create the invalidation request
        response = cloudfront_client.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': len(paths),
                    'Items': paths
                },
                'CallerReference': str(hash(frozenset(paths)))  # Unique reference for each invalidation
            }
        )

        # Output the invalidation ID
        invalidation_id = response['Invalidation']['Id']
        print(f"Invalidation created successfully. Invalidation ID: {invalidation_id}")

    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage

    # Replace with your CloudFront distribution ID
    DISTRIBUTION_ID = "E2AO23OOLGI43X"

    # Replace with the paths you want to invalidate
    PATHS_TO_INVALIDATE = [
        "/index.html"
    ]

    create_invalidation(DISTRIBUTION_ID, PATHS_TO_INVALIDATE)
