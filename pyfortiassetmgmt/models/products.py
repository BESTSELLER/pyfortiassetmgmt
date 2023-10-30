from datetime import datetime
from pyfortiassetmgmt.core.fortiassetmgmt import FortiAssetMgmt


class Products(FortiAssetMgmt):
    """API class for products.
    """

    def __init__(self, **kwargs):
        super(Products, self).__init__(**kwargs)

    def all(self, serialNumber: str=None, expireBefore: str=None):
        """Retrieves all or a single product.

        Args:
            serialNumber (str, optional): Serial number of a specific product.
            expireBefore (str, optional): Support package expiration date in ISO 8601 format. Example: 2019-01-20T10:11:11-8:00

        Returns:
            dict: JSON data.
        """

        # If expireBefore is not set, use current date + 100 years
        if not expireBefore:
            expireBefore = datetime.now().isoformat().replace(str(datetime.now().year), str(datetime.now().year+100))

        data = {
            "serialNumber": serialNumber,
            "expireBefore": expireBefore
        }

        return self.post(endpoint="/products/list", data=data)
    
    def decommission(self, serialNumbers: list):
        """Decommissions a list of products.

        Args:
            serialNumbers (list): A list of all serial numbers to be decommissioned.

        Returns:
            dict: JSON data.
        """

        # Convert serialNumbers to a list, if its a str.
        if type(serialNumbers) == str:
            serialNumbers = [serialNumbers]

        data = {
            "serialNumbers": serialNumbers
        }

        return self.post(endpoint="/products/decommission", data=data)
    
    def details(self, serialNumber: str):
        """Retrieves all details for a single product, including active support coverage and associated licenses.

        Args:
            serialNumber (str): Serial number of product.

        Returns:
            dict: JSON data.
        """

        data = {
            "serialNumber": serialNumber
        }

        return self.post(endpoint="/products/details", data=data)
    
    def register(self, serialNumber: str, cloudKey: str=None, isGovernment: bool=False, contractNumber: str=None, folderId: int=None, description: str=None, assetGroupIds: str=None, replacedSerialNumber: str=None, additionalInfo: str=None):
        """Registers a product.

        Args:
            serialNumber (str): Product serial number.
            cloudKey (str): Cloud key to be used in product registration.
            isGovernment (bool): Whether the product will be used for government or not.
            contractNumber (str, optional): Register contract with product.
            folderId (int, optional): Asset folder id. If not provided it will use My Assets folder.
            description (str, optional): Set product description during registration process.
            assetGroupIds (str, optional): Register product under certain asset group, multiple asset group allowed.
            replacedSerialNumber (str, optional): Used for product RMA registration for replaced product serial number.
            additionalInfo (str, optional): Store extra info for certain product registration, for example system ID, IP address etc..
    
        Returns:
            dict: JSON data.
        """

        data = {
            "registrationUnits":
            [
                {
                    "serialNumber": serialNumber,
                    "cloudKey": cloudKey,
                    "isGovernment": isGovernment
                }
            ]
        }

        # Optional fields
        if contractNumber:
            data['contractNumber'] = contractNumber

        if folderId:
            data['folderId'] = folderId

        if description:
            data['description'] = description

        if assetGroupIds:
            data['assetGroupIds'] = assetGroupIds

        if replacedSerialNumber:
            data['replacedSerialNumber'] = replacedSerialNumber

        if additionalInfo:
            data['additionalInfo'] = additionalInfo

        return self.post(endpoint="/products/register", data=data)
    
    def update_description(self, serialNumber: str, description: str):
        """Update description of a product using the serial number.

        Args:
            serialNumber (str): Product serial number.
            description (str): Description for product.

        Returns:
            dict: JSON data.
        """

        data = {
            "serialNumber": serialNumber,
            "description": description
        }

        return self.post(endpoint="/products/description", data=data)
    
    def update_folder(self, serialNumbers: list, folderId: int):
        """Update folder of one or more products.

        Args:
            serialNumbers (list): A list of all serial numbers to be moved. Ex. ["FGT90D1234567890", "FGT90D1234567891"].
            folderId (int): Target asset folder id.

        Returns:
            dict: JSON data.
        """

        # Convert serialNumbers to a list, if its a str.
        if type(serialNumbers) == str:
            serialNumbers = [serialNumbers]

        data = {
            "serialNumbers": serialNumbers,
            "folderId": folderId
        }

        return self.post(endpoint="/products/folder", data=data)