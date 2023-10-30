# pyfortiassetmgmt
Python API client library for Fortinet's [Asset Management](https://support.fortinet.com).

The Asset Management API provides:
- Contract management (Retrieve)
- Folder management (Retrieve, create, delete)
- License management (Retrieve, register, download)
- Product management (Register, retrieve, decommission)
- Service management (Register)

> **Note:** This library has been built and tested for API v3.

## Installation
To install run `pip install pyfortiassetmgmt`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Quick Start
To begin, import pyfortiassetmgmt and instantiate the API.

We need to provide our API credentials to our FortiCloud account.

Optionally, its possible to set the following settings:
- `client_id` which defaults to `assetmanagement`.
- `forticloud_host` which defaults to `https://customerapiauth.fortinet.com`
- `fortiasset_host` which defaults to `https://support.fortinet.com`

**Code**
```
fortiassetmgmt = pyfortiassetmgmt.api(
    userid = "<your forticloud userid>",
    password = "<your forticloud password>"
)
```

## Examples
### Retrieve a product.
**Code**
```
products = fortiassetmgmt.products.all(serialNumber="FGT60FTK1234ABCD")
print(products)
```

**Output**
```
{
    "build": "1.0.0",
    "error": null,
    "message": "Request processed successfully",
    "status": 0,
    "token": "<token>",
    "version": "3.0",
    "assets": [
        {
            "description": "Test FortiGate",
            "entitlements": [
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 5,
                    "levelDesc": "Advanced HW",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 1,
                    "typeDesc": "Hardware"
                },
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 6,
                    "levelDesc": "Web/Online",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 2,
                    "typeDesc": "Firmware & General Updates"
                },
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 20,
                    "levelDesc": "Premium",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 11,
                    "typeDesc": "Enhanced Support"
                },
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 20,
                    "levelDesc": "Premium",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 12,
                    "typeDesc": "Telephone Support"
                },
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 6,
                    "levelDesc": "Web/Online",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 21,
                    "typeDesc": "Advanced Malware Protection"
                },
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 6,
                    "levelDesc": "Web/Online",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 22,
                    "typeDesc": "NGFW"
                },
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 6,
                    "levelDesc": "Web/Online",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 41,
                    "typeDesc": "Web & Video Filtering"
                },
                {
                    "endDate": "2024-07-31T00:00:00",
                    "level": 6,
                    "levelDesc": "Web/Online",
                    "startDate": "2021-08-01T00:00:00",
                    "type": 51,
                    "typeDesc": "AntiSpam"
                }
            ],
            "isDecommissioned": false,
            "productModel": "FortiGate 60F",
            "registrationDate": "2023-01-09T00:37:25",
            "serialNumber": "FGT60FTK1234ABCD",
            "warrantySupports": null,
            "assetGroups": [],
            "contracts": [
                {
                    "contractNumber": "<contractNumber>",
                    "sku": "FC-10-0060F-123-45-67",
                    "terms": [
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "Hardware"
                        },
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "Firmware & General Updates"
                        },
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "Enhanced Support"
                        },
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "Telephone Support"
                        }
                    ]
                },
                {
                    "contractNumber": "<contractNumber>",
                    "sku": "FC-10-0060F-123-45-67",
                    "terms": [
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "Advanced Malware Protection"
                        }
                    ]
                },
                {
                    "contractNumber": "<contractNumber>",
                    "sku": "FC-10-0060F-108-02-36",
                    "terms": [
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "NGFW"
                        }
                    ]
                },
                {
                    "contractNumber": "<contractNumber>",
                    "sku": "FC-10-0060F-112-02-36",
                    "terms": [
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "Web & Video Filtering"
                        }
                    ]
                },
                {
                    "contractNumber": "<contractNumber>",
                    "sku": "FC-10-0060F-114-02-36",
                    "terms": [
                        {
                            "endDate": "2024-07-31T00:00:00",
                            "startDate": "2021-08-01T00:00:00",
                            "supportType": "AntiSpam"
                        }
                    ]
                }
            ],
            "productModelEoR": null,
            "productModelEoS": null,
            "status": "Registered"
        }
    ],
    "pageNumber": 1,
    "totalPages": 1
}
```

### Retrieve a contract.
**Code**
```
contracts = fortiassetmgmt.contracts.all(contractNumber="1234AB123456")
print(contracts)
```

**Output**
```
{
    "build": "1.0.0",
    "error": null,
    "message": "Success",
    "status": 0,
    "token": "<token>",
    "version": "3.0",
    "contracts": [
        {
            "contractNumber": "1234AB123456",
            "contractSKU": "FC-10-0060E-123-45-67",
            "status": "Registered"
        }
    ]
}
```

### Register a product.
**Code**
```
register = fortiassetmgmt.products.register(
    serialNumber = "FGT60FTK1234ABCD",
    cloudKey = "80X4LSN3"
)
print(register)
```

**Output**
```
{
    "build": "1.0.0",
    "error": {
        "errorCode": 301,
        "message": "Failed"
    },
    "message": "Failed",
    "status": 2,
    "token": "<token>",
    "version": "3.0",
    "assets": [
        {
            "description": null,
            "entitlements": null,
            "isDecommissioned": false,
            "productModel": null,
            "registrationDate": null,
            "serialNumber": "FGT60FTK1234ABCD",
            "warrantySupports": null,
            "assetGroups": null,
            "contracts": null,
            "productModelEoR": null,
            "productModelEoS": null,
            "additionalInfo": null,
            "contractNumber": null,
            "contractTerms": null,
            "location": null,
            "message": "Product-> Product already registered, but no contract associated with request. Please check again.",
            "sku": null,
            "status": 2,
            "folderId": 0,
            "folderPath": null
        }
    ]
}
```