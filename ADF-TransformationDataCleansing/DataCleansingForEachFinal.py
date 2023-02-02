{
  "name": "DataCleansingPipeline",
  "properties": {
    "activities": [
      {
        "type": "ForEach",
        "typeProperties": {
          "items": {
            "value": "@pipeline().parameters.inputFiles",
            "type": "Expression"
          },
          "activities": [
            {
              "type": "Copy",
              "name": "CleanseData",
              "dependsOn": [],
              "policy": {
                "timeout": "7.00:00:00",
                "retry": 0,
                "retryIntervalInSeconds": 30,
                "secureOutput": false,
                "secureInput": false
              },
              "typeProperties": {
                "source": {
                  "type": "AzureDataLakeStore",
                  "recursive": true,
                  "fileName": "@{item().value}"
                },
                "sink": {
                  "type": "AzureSQL",
                  "table": "IoTData",
                  "connectionString": "Server=<your-server-name>;Database=<your-database-name>;User ID=<your-user-id>;Password=<your-password>;"
                },
                "transformer": [
                  {
                    "type": "Filter",
                    "filter": {
                      "type": "Expression",
                      "expression": "Temperature >= 0"
                    }
                  },
                  {
                    "type": "DerivedColumn",
                    "columns": [
                      {
                        "name": "TemperatureF",
                        "expression": "((Temperature * 9) / 5) + 32"
                      }
                    ]
                  }
                ]
              }
            }
          ]
        },
        "error": [
          {
            "type": "Copy",
            "name": "LogError",
            "dependsOn": [
              {
                "activity": "CleanseData",
                "dependencyConditions": [
                  "Failed"
                ]
              }
            ],
            "policy": {
              "timeout": "7.00:00:00",
              "retry": 0,
              "retryIntervalInSeconds": 30,
              "secureOutput": false,
              "secureInput": false
            },
            "typeProperties": {
              "source": {
                "type": "Expression",
                "expression": "{ \"ErrorMessage\": \"@{activity('CleanseData').error.message}\", \"FileName\": \"@{item().value}\" }"
              },
              "sink": {
                "type": "AzureDataLakeStore",
                "fileName": "error-logs.json"
              }
            }
          }
        ]
      }
    ],
    "parameters": {
      "inputFiles": {
"type": "Array",
"defaultValue": []
}
}
}
}
