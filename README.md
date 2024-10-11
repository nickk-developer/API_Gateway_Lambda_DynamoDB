# API Gateway with Lambda and DynamoDB Integration

## Project Overview
In this project, we created a serverless API using **API Gateway**, **AWS Lambda**, and **DynamoDB**. The API allows clients to make requests, and the Lambda function fetches data from a DynamoDB table based on the request parameters.

## Steps Covered
1. **SS1.png**: Created a Lambda function (`MyAPIFunction`).
2. **SS2.png**: Deployed the Lambda function with a simple handler.
3. **SS3.png**: Created an API and integrated it with the Lambda function using API Gateway.
4. **SS4.png**: Created two stages in API Gateway (`testing` and `prod`).
5. **SS5.png**: Deployed the API across both the testing and production environments.
6. **SS6.png**: Successfully invoked the API in the testing environment.
7. **SS7.png**: Successfully invoked the API in the production environment.
8. **SS8.png**: Created a table (`MyTable`) in DynamoDB with a primary key (`pri_key`).
9. **SS9.png**: Updated the Lambda function to integrate with DynamoDB and retrieve data based on `pri_key`.
10. **SS10.png**: Invoked the API in the testing environment after integrating DynamoDB, successfully returning data from the table.
11. **SS11.png**: Invoked the API in the production environment after integrating DynamoDB, successfully returning data from the table.

## Tools Used
- **API Gateway**: To expose a RESTful API.
- **AWS Lambda**: To process the requests.
- **DynamoDB**: To store and retrieve data.
- **AWS CloudWatch**: To monitor and debug the Lambda function and API Gateway.

## Key Endpoints
1. **GET /MyAPIFunction**: Fetches data from the DynamoDB table.
    - Query Parameter: `pri_key` (Primary Key)

## Example Request and Response

- **Request**:
    ```bash
    curl "https://<api-id>.execute-api.us-east-1.amazonaws.com/prod/MyAPIFunction?pri_key=nick"
    ```

- **Response**:
    ```json
    {
      "pri_key": "nick",
      "foreign_key": "sunflower"
    }
    ```

## DynamoDB Schema
- **Table Name**: `MyTable`
- **Primary Key**: `pri_key` (String)

## How to Run the Project
1. Deploy the provided Lambda function in AWS Lambda.
2. Create an API Gateway to integrate with the Lambda function.
3. Set up DynamoDB with the schema provided.
4. Deploy API Gateway stages for testing and production.
5. Invoke the API using the URLs provided by API Gateway.

## Issues and Troubleshooting
- Ensure the Lambda function has the correct IAM roles to access DynamoDB.
- Make sure the security settings in API Gateway allow public access for testing.

## Screenshots
All screenshots of the steps are available in the `screenshots/` directory.

1. **SS1.png**: Created a Lambda function.
2. **SS2.png**: Deployed the Lambda function.
3. **SS3.png**: Created an API and integrated it with the Lambda function.
4. **SS4.png**: Created stages (testing and production).
5. **SS5.png**: Deployed the API on both stages.
6. **SS6.png**: Successfully invoked the API in testing.
7. **SS7.png**: Successfully invoked the API in production.
8. **SS8.png**: Created a DynamoDB table.
9. **SS9.png**: Updated Lambda to integrate with DynamoDB.
10. **SS10.png**: Invoked the API in testing after DynamoDB integration.
11. **SS11.png**: Invoked the API in production after DynamoDB integration.
