from pyfortiassetmgmt.core.fortiassetmgmt import FortiAssetMgmt


class Services(FortiAssetMgmt):
    """API class for services.
    """

    def __init__(self, **kwargs):
        super(Services, self).__init__(**kwargs)

    def all(self, contractNumber: str, description: str=None, additionalInfo: str=None, isGovernment: bool=False):
        """Register a subscription contract (e.g. VM-S) to generate serial number.

        Args:
            contractNumber (str): Contract number to register.
            isGovernment (bool): Whether the product will be used for government or not.
            description (str, optional): Set product description during registration process.
            additionalInfo (str, optional): Store extra info for certain product registration, for example system ID, IP address etc.

        Returns:
            dict: JSON data.
        """

        data = {
            "contractNumber": contractNumber,
            "isGovernment": isGovernment
        }

        # Optional fields
        if description:
            data['description'] = description

        if additionalInfo:
            data['additionalInfo'] = additionalInfo

        return self.post(endpoint="/services/register", data=data)