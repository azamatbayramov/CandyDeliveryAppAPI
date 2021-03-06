from fastapi import APIRouter, status, Depends
from services.couriers import CouriersService
from models.couriers import CouriersPostRequest, CourierGetResponse, CourierItem

router = APIRouter(prefix="/couriers")


@router.post("", status_code=status.HTTP_201_CREATED)
def import_couriers(couriers: CouriersPostRequest, service: CouriersService = Depends()):
    return service.import_couriers(couriers)


@router.get("/{courier_id}")
def get_courier_info(courier_id: int, service: CouriersService = Depends()):
    return CourierItem(**CourierItem.from_orm(service.get_courier(courier_id)).dict()).get_getresponse()
