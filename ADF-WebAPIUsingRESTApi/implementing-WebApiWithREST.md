To implement the step-by-step code for Web API data being ingested into ADF using REST API calls:

1. Create a REST API endpoint that returns the data to be ingested into ADF. This endpoint should be able to accept parameters for filtering and sorting the data as required.

2. In Azure Data Factory, create a new pipeline and add a REST API activity to it. This activity should call the REST API endpoint created in step 1.

3. In the REST API activity, specify the endpoint URL, the HTTP method to be used (e.g. GET), and any headers or parameters required to access the data.

4. Use the data returned from the REST API endpoint as the input to the next activity in the pipeline. For example, you might use the data to create a new data flow that performs transformations and enriches the data.

5. In the final step, use the output from the previous activity to load the transformed data into a data lake or data warehouse for analysis. This can be done using an Azure Data Factory Copy Activity or a custom activity that writes the data to the desired destination