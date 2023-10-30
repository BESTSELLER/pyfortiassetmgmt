from pyfortiassetmgmt.core.fortiassetmgmt import FortiAssetMgmt


class Contracts(FortiAssetMgmt):
    """API class for contracts.
    """

    def __init__(self, **kwargs):
        super(Contracts, self).__init__(**kwargs)

    def all(self, contractNumber: str=None, contractSKU: str=None, status: str=None):
        """Retrieves all or a single contract.

        Args:
            contractNumber (str, optional): Specific contract number. Ex. 6119MV986329.
            contractSKU (str, optional): Specific contract SKU. Ex. FC-10-0040F-950-02-12.
            status (str, optional): Optional status. Allowed values are Registered and Pending.

        Returns:
            dict: JSON data.
        """

        data = {}

        # Optional fields
        if contractNumber:
            data['contractNumber'] = contractNumber

        if contractSKU:
            data['contractSKU'] = contractSKU

        if status:
            data['status'] = status

        return self.post(endpoint="/contracts/list", data=data)