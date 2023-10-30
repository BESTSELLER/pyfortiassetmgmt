from datetime import datetime, timedelta
import requests


class FortiAssetMgmt(object):
    """API class for FortiAssetMgmt login management.
    """

    def __init__(self, api, **kwargs):
        self.api = api

    def login(self):
        """Login to FortiCloud.
        """

        # Payload
        data = {
            "username": self.api.userid,
            "password": self.api.password,
            "client_id": self.api.client_id,
            "grant_type": "password",
        }

        # Send our request to the API
        response = requests.post(f"{self.api.forticloud_host}/oauth/token/", json=data, verify=self.api.verify)

        # HTTP 200 OK
        if response.status_code == 200:
            if response.json():
                self.api.access_token = response.json()['access_token']
                self.api.expires_in = response.json()['expires_in']
                self.api.refresh_token = response.json()['refresh_token']
                self.api.timestamp = datetime.now()
            else:
                self.api.access_token = None
                self.api.expires_in = None
                self.api.refresh_token = None
                self.api.timestamp = None

    def refresh_token(self):
        """Refreshes our login token to FortiCloud.
        """

        # Make sure we have a refresh token
        if self.api.refresh_token:
        
            # Payload
            data = {
                "refresh_token": self.api.refresh_token,
                "client_id": self.api.client_id,
                "grant_type": "password",
            }

            # Send our request to the API
            response = requests.post(f"{self.api.forticloud_host}/oauth/token/", json=data, verify=self.api.verify)

            # HTTP 200 OK
            if response.status_code == 200:
                if response.json():
                    self.api.access_token = response.json()['access_token']
                    self.api.expires_in = response.json()['expires_in']
                    self.api.refresh_token = response.json()['refresh_token']
                    self.api.timestamp = datetime.now()
                else:
                    self.login()
            else:
                self.login()
        
    def login_check(self):
        """Checks if we have a valid login session.
        """

        # Make sure we have valid token credentials
        if self.api.access_token and self.api.expires_in and self.api.refresh_token and self.api.timestamp:

            # Check if our token has expired
            if datetime.now() > self.api.timestamp+timedelta(seconds=self.api.expires_in):
                self.refresh_token()
            else:
                pass

        # Fallback to login
        else:
            self.login()

    def post(self, endpoint: str, data: dict):
        """Executes a POST request to the FortiCare API.

        Args:
            endpoint (str): API endpoint url.
            data (dict): JSON data to send with the request.

        Returns:
            dict: JSON data.
        """

        self.login_check()

        response = requests.post(self.api.fortiasset_host + endpoint, headers={'Authorization': 'Bearer ' + self.api.access_token}, json=data, verify=self.api.verify)

        # Check if JSON serializable
        if response.json():
            return response.json()
        else:
            return response