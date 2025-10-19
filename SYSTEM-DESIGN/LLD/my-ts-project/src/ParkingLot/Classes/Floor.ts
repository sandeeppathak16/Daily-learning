import { ParkingSpot } from "./ParkingSpot.js";
import {
  ParkingSpotType,
  ROW_PER_FLOOR,
  COLUMN_PER_FLOOR,
  TOTAL_FLOOR,
} from "../Constants.js";

function getRandomParkingSpotType(): ParkingSpotType {
  const values = Object.values(ParkingSpotType);
  const randomIndex = Math.floor(Math.random() * values.length);
  return values[randomIndex] as ParkingSpotType;
}

class Entrance {
  getTicket() {
    console.log("get ticket");
  }
}

class Exit {
  validateExit() {
    console.log("validate exit");
  }
}

type CellType =
  | ParkingSpot
  | Entrance
  | Exit
  | { type: "Stairs"; up: number | null; down: number | null };

export class Floor {
  floor: number;
  rows: number;
  columns: number;
  spots: CellType[][];

  constructor(
    floor: number,
    totalFloors: number,
    rows: number,
    columns: number
  ) {
    this.floor = floor;
    this.rows = rows;
    this.columns = columns;
    this.spots = this.initializeGrid(totalFloors);
  }

  private initializeGrid(totalFloors: number): CellType[][] {
    const grid: CellType[][] = [];

    for (let r = 0; r < this.rows; r++) {
      const row: CellType[] = [];
      for (let c = 0; c < this.columns; c++) {
        if (r === 0 && c === 0) {
          row.push(new Entrance());
        } else if (
          this.floor === 0 &&
          r === this.rows - 1 &&
          c === this.columns - 1
        ) {
          row.push(new Exit());
        } else if (r === 0 && c === this.columns - 1) {
          const up = this.floor < totalFloors - 1 ? this.floor + 1 : null;
          const down = this.floor > 0 ? this.floor - 1 : null;
          row.push({ type: "Stairs", up, down });
        } else {
          const parkingType = getRandomParkingSpotType();
          row.push(new ParkingSpot(parkingType));
        }
      }
      grid.push(row);
    }

    return grid;
  }
}

export class ParkingBuilding {
  floors: Floor[] = [];

  addFloor(): boolean {
    const totalFloor = this.floors.length;

    if (totalFloor >= TOTAL_FLOOR) {
      console.log("Reached Max floor limit");
      return false;
    }

    const floor = new Floor(
      totalFloor,
      totalFloor + 1,
      ROW_PER_FLOOR,
      COLUMN_PER_FLOOR
    );
    this.floors.push(floor);
    console.log(`Added floor ${totalFloor + 1}`);
    return true;
  }
}
