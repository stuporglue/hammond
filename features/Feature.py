class Feature:

    def __init__(self,orgb_client):
        self.orgb_client = orgb_client
        self.device = self.orgb_client.get_devices_by_name(self.device)[0]
        self.zone = self.device.zones[self.zone]
