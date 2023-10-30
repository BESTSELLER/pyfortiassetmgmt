from pyfortiassetmgmt.core.fortiassetmgmt import FortiAssetMgmt


class Folders(FortiAssetMgmt):
    """API class for folders.
    """

    def __init__(self, **kwargs):
        super(Folders, self).__init__(**kwargs)

    def all(self):
        """Retrieves all or a single folder.

        Returns:
            dict: JSON data.
        """

        return self.post(endpoint="/folders/list", data={})

    def create(self, name: str=None, parentFolderId: int=None):
        """Creates a folder.

        Args:
            name (str): Name of the folder to create.
            parentFolderId (int, optional): Optional id of a parent folder.

        Returns:
            dict: JSON data.
        """

        data = {
            "folderName": name
        }

        # Optional fields
        if parentFolderId:
            data['parentFolderId'] = parentFolderId

        return self.post(endpoint="/folders/create", data=data)
    

    def delete(self, folderId: int=None):
        """Deletes a folder.

        Args:
            folderId (int): ID of the folder to delete.

        Returns:
            dict: JSON data.
        """

        data = {
            "folderId": folderId
        }

        return self.post(endpoint="/folders/delete", data=data)