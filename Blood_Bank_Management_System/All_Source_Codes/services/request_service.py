from models.blood_request import BloodRequest
from utils.decorator import log_activity
from utils.exception import (
    BloodStockNotAvailableError
)


class RequestService:

    def __init__(self, inventory_service):

        self.requests = []
        self.inventory_service = inventory_service

    # -------------------------
    # Create Blood Request
    # -------------------------
    @log_activity
    def create_request(
            self,
            request_id,
            hospital_name,
            blood_group,
            quantity):

        request = BloodRequest(
            request_id,
            hospital_name,
            blood_group,
            quantity
        )

        self.requests.append(request)

        request.create_request()

    # -------------------------
    # Approve Request
    # -------------------------
    @log_activity
    def approve_request(
            self,
            request_id):

        for request in self.requests:

            if request.request_id == request_id:

                available = self.inventory_service\
                    .inventory\
                    .blood_units\
                    .get(
                        request.blood_group,
                        0
                    )

                if available < request.quantity:
                    raise BloodStockNotAvailableError()

                self.inventory_service.remove_stock(
                    request.blood_group,
                    request.quantity
                )

                request.approve_request()

                return

        print("Request Not Found")

    # -------------------------
    # Reject Request
    # -------------------------
    @log_activity
    def reject_request(
            self,
            request_id):

        for request in self.requests:

            if request.request_id == request_id:

                request.reject_request()

                return

        print("Request Not Found")

    # -------------------------
    # Search Request
    # -------------------------
    def search_request(
            self,
            request_id):

        for request in self.requests:

            if request.request_id == request_id:
                return request

        return None

    # -------------------------
    # View All Requests
    # -------------------------
    def view_all_requests(self):

        if not self.requests:
            print("No Requests Available")
            return

        print("\n===== REQUEST LIST =====")

        for request in self.requests:
            print(request)

    # -------------------------
    # Sort Requests
    # Lambda Function
    # -------------------------
    def sort_requests(self):

        sorted_requests = sorted(
            self.requests,
            key=lambda request:
            request.quantity,
            reverse=True
        )

        print("\n===== SORTED REQUESTS =====")

        for request in sorted_requests:
            print(request)