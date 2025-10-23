import { ParkingBuilding } from "./Floor.js";

export class ParkingManager {
  private static instance: ParkingManager;
  private building?: ParkingBuilding;

  private constructor() {}

  public static getInstance(): ParkingManager {
    if (!ParkingManager.instance) {
      ParkingManager.instance = new ParkingManager();
      ParkingManager.instance.setBuilding(5);
    }
    return ParkingManager.instance;
  }

  public setBuilding(numberOfFloor: number): void {
    const building = new ParkingBuilding();
    this.building = building;

    for (let i = 0; i < numberOfFloor; i++) {
      building.addFloor();
    }
  }

  public getBuilding(): ParkingBuilding | undefined {
    return this.building;
  }
}

export const parkingManager = ParkingManager.getInstance();
