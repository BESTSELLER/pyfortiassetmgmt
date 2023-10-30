from pyfortiassetmgmt.core.fortiassetmgmt import FortiAssetMgmt


class Licenses(FortiAssetMgmt):
    """API class for licenses.
    """

    def __init__(self, **kwargs):
        super(Licenses, self).__init__(**kwargs)

    def all(self, licenseNumber: str=None, licenseSKU: str=None, status: str=None):
        """Retrieves a list of all or a single license.

        Args:
            licenseNumber (str, optional): Optional license number.
            licenseSKU (str, optional): Optional SKU.
            status (str, optional): Optional status. Allowed values are Registered and Pending.

        Returns:
            dict: JSON data.
        """

        data = {}

        # Optional fields
        if licenseNumber:
            data['licenseNumber'] = licenseNumber

        if licenseSKU:
            data['licenseSKU'] = licenseSKU

        if licenseSKU:
            data['licenseSKU'] = licenseSKU

        return self.post(endpoint="/licenses/list", data=data)

    def register(self, licenseRegistrationCode: str, isGovernment: bool=False, serialNumber: str=None, description: str=None, additionalInfo: str=None):
        """Registeri a license.

        Args:
            licenseRegistrationCode (str): License registration code. Ex. K06V2-U795H-9PKR7-2TXNM-V8GL6B.
            isGovernment (bool): If the product will be used for government or not. Default is False.
            serialNumber (str, optional): Optional product serial number, if this field is not empty, the license will be registered under it, otherwise a virtual product will be created for the registered license (if applicable).
            description (str, optinal): The description for the new product.
            additionalInfo (str, optional): Store extra info for certain product registration, for example system ID, IP address etc.

        Returns:
            dict: JSON data.
        """

        data = {
            "licenseRegistrationCode": licenseRegistrationCode,
            "isGovernment": isGovernment
        }

        # Optional fields
        if serialNumber:
            data['serialNumber'] = serialNumber

        if description:
            data['description'] = description

        if additionalInfo:
            data['additionalInfo'] = additionalInfo

        return self.post(endpoint="/licenses/register", data=data)

    def download(self, serialNumber: str):
        """Download a license keyy file.

        Args:
            serialNumber (str): Product serial number. Ex. FGT90D1234567890.

        Returns:
            dict: JSON data.
        """

        data = {
            "serialNumber": serialNumber
        }

        return self.post(endpoint="/licenses/download", data=data)