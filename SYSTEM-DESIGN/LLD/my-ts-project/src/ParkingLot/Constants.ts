export const MAX_VEHICHAL_SUPPORT: number = 40000;
export const TOTAL_FLOOR: number = 8;
export const CAPACITY_PER_FLOOR: number = MAX_VEHICHAL_SUPPORT / TOTAL_FLOOR;
export const ROW_PER_FLOOR: number = 50;
export const COLUMN_PER_FLOOR: number = 100;

export enum VehicleType {
  Car = "Car",
  Truck = "Truck",
  Van = "Van",
  Motorcycle = "Motorcycle",
}

export enum ParkingSpotType {
  Accessible = "Accessible",
  Compact = "Compact",
  Large = "Large",
}

export const VehicleToSpotMapping: Record<VehicleType, ParkingSpotType[]> = {
  [VehicleType.Car]: [ParkingSpotType.Compact, ParkingSpotType.Accessible],
  [VehicleType.Truck]: [ParkingSpotType.Large],
  [VehicleType.Van]: [ParkingSpotType.Large, ParkingSpotType.Accessible],
  [VehicleType.Motorcycle]: [ParkingSpotType.Compact],
};


export enum TicketStatus {
    Issued,
    InUse,
    Paid,
    Validated,
    Canceled,
    Refunded
}

export enum HourlyRate {
  Large = 100,
  Compack = 80,
  Motorcycle = 50,
  Accessible = 30,
}

export enum SecondHourRate {
  Large = 80,
  Compack = 60,
  Motorcycle = 40,
  Accessible = 20,
}

export enum RemainingHourRate {
  Large = 50,
  Compack = 30,
  Motorcycle = 20,
  Accessible = 10,
}


export enum PaymentStatus {
    Completed,
    Failed,
    Pending,
    Unpaid,
    Refunded
}
