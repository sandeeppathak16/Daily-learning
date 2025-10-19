import { Vehicle } from "./Vehicle.js";
import { ParkingSpotType, VehicleToSpotMapping } from "../Constants.js";

export class ParkingSpot {
  vehicle?: Vehicle;
  type: ParkingSpotType;

  constructor(type: ParkingSpotType) {
    this.type = type;
  }

  addVehicle(vehicle: Vehicle): boolean {
    if (!this.vehicle) {
      console.log("parking spot is occupied");
      return false;
    }
    if (!VehicleToSpotMapping[vehicle.type].includes(this.type)) {
      console.log(
        `you can not park ${vehicle.type} on ${this.type} parking spot.`
      );
      return false;
    }

    this.vehicle = vehicle;
    return true;
  }

  removeVehicle(): boolean {
    if (!this.vehicle) {
      console.log("No vehicle to remove.");
      return false;
    }
    console.log(`Vehicle ${this.vehicle.type} removed.`);
    this.vehicle = undefined;
    return true;
  }
}
