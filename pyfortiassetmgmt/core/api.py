from pyfortiassetmgmt.models.contracts import Contracts
from pyfortiassetmgmt.models.folders import Folders
from pyfortiassetmgmt.models.licenses import Licenses
from pyfortiassetmgmt.models.products import Products
from pyfortiassetmgmt.models.services import Services


class Api(object):
    """Base API class.
    """

    def __init__(self, userid: str, password: str, client_id: str="assetmanagement", forticloud_host: str="https://customerapiauth.fortinet.com", fortiasset_host: str="https://support.fortinet.com", verify: bool=True, **kwargs):
        self.userid = userid
        self.password = password
        self.client_id = client_id
        self.forticloud_host = forticloud_host + "/api/v1"
        self.fortiasset_host = fortiasset_host + "/ES/api/registration/v3"
        self.verify = verify
        self.access_token = None
        self.expires_in = None
        self.refresh_token = None
        self.timestamp = None

    @property
    def contracts(self):
        """Endpoints related to contract management.
        """
        return Contracts(api=self)
    
    @property
    def folders(self):
        """Endpoints related to folder management.
        """
        return Folders(api=self)

    @property
    def licenses(self):
        """Endpoints related to license management.
        """
        return Licenses(api=self)

    @property
    def products(self):
        """Endpoints related to product management.
        """
        return Products(api=self)

    @property
    def services(self):
        """Endpoints related to service management.
        """
        return Services(api=self)