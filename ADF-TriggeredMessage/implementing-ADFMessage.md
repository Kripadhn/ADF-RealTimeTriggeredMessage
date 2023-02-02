Here is a step-by-step code for implementing an Azure Data Factory (ADF) pipeline that is triggered by a message arriving in the IoT Hub and extracts the data from the message:

1. Create an Azure Data Factory:
az datafactory create --name {DataFactoryName} --resource-group {ResourceGroupName}

2. Create a pipeline that includes the following activities:
IoT Hub Trigger: to trigger the pipeline when a message arrives in the IoT Hub.
IoT Hub Source: to extract data from the message in the IoT Hub.
Data Transformation: to perform transformations on the data, such as data cleansing and enrichment, if necessary.
Data Sink: to load the transformed data into a data lake or data warehouse, such as Azure Data Lake Storage or Azure Synapse Analytics.


3. Create the data lake storage account:
az data lake store account create --name {DataLakeStoreAccountName} --resource-group {ResourceGroupName}


4. Save the pipeline definition to the data factory:
az datafactory pipeline create --definition "$(< pipeline-definition.json)" --name IoT_Data_Ingestion_Pipeline --resource-group {ResourceGroupName} --data-factory {DataFactoryName}


5. Create a trigger in the IoT Hub that starts the pipeline whenever a new message arrives:
az iot hub trigger create --hub-name {IoTHubName} --name IoT_Data_Ingestion_Pipeline_Trigger --resource-group {ResourceGroupName} --source-type "Microsoft.DataFactory/datafactories/pipelines" --source-path "{DataFactoryName}/pipelines/IoT_Data_Ingestion_Pipeline"


6. Test the pipeline by sending a message to the IoT Hub:
az iot hub device-to-cloud-message send --device-id {DeviceId} --hub-name {IoTHubName} --message "Hello from IoT device!" --resource-group {ResourceGroupName}


7. Monitor the pipeline run to ensure that it is executing successfully:
az datafactory pipeline run show --name IoT_Data_Ingestion_Pipeline --resource-group {ResourceGroupName} --data-factory {DataFactoryName}


8. Verify the data in the data lake to ensure that the data is being loaded successfully:
az data lake store file show --account {DataLakeStoreAccountName} --path {DataLakeFilePath}


That's it! You have successfully implemented an Azure Data Factory pipeline that is triggered by a message arriving in the IoT Hub and extracts the data from the message. The transformed data is now available in Azure Data Lake Storage for further analysis and insights.


Here is a sample pipeline in YAML format that performs the data extraction and transformation: