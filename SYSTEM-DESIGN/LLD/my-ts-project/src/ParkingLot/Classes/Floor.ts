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

export class Entrance {
  getTicket() {
    console.log("get ticket");
  }
}

export class Exit {
  validateExit() {
    console.log("validate exit");
  }
}

type CellType =
  | ParkingSpot
  | Entrance
  | Exit
  | { type: "Stairs"; up: number; down: number };

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
          const up = this.floor < totalFloors - 1 ? this.floor + 1 : 0;
          const down = this.floor > 0 ? this.floor - 1 : 0;
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

type Position = { floor: number; row: number; col: number };

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
      TOTAL_FLOOR,
      ROW_PER_FLOOR,
      COLUMN_PER_FLOOR
    );
    this.floors.push(floor);
    console.log(`Added floor ${totalFloor + 1}`);
    return true;
  }

  /**
   * Finds the nearest available parking spot to an entrance or exit.
   * Uses multi-source BFS to guarantee the shortest path.
   */
  getNearestParkingSpot(type: ParkingSpotType): ParkingSpot | null {
    const queue: { pos: Position; distance: number }[] = [];
    const visited = new Set<string>();

    // Step 1: Collect all entrances and exits as BFS starting points
    for (let f = 0; f < this.floors.length; f++) {
      const floor = this.floors[f];
      if (!floor) continue;

      for (let r = 0; r < floor.rows; r++) {
        for (let c = 0; c < floor.columns; c++) {
          const cell = floor.spots[r][c];
          if (cell instanceof Entrance || cell instanceof Exit) {
            queue.push({ pos: { floor: f, row: r, col: c }, distance: 0 });
            visited.add(`${f},${r},${c}`);
          }
        }
      }
    }

    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];

    while (queue.length > 0) {
      const { pos, distance } = queue.shift()!;
      const { floor, row, col } = pos;
      const cell = this.floors[floor].spots[row][col];

      if (cell instanceof ParkingSpot && cell.type === type && !cell.vehicle) {
        console.log(
          `Found nearest ${type} spot at Floor ${floor}, Row ${row}, Col ${col}, Distance ${distance}`
        );
        return cell;
      }

      for (const [dr, dc] of directions) {
        const nr = row + dr;
        const nc = col + dc;
        if (
          nr >= 0 &&
          nc >= 0 &&
          nr < this.floors[floor].rows &&
          nc < this.floors[floor].columns
        ) {
          const key = `${floor},${nr},${nc}`;
          if (!visited.has(key)) {
            visited.add(key);
            queue.push({
              pos: { floor, row: nr, col: nc },
              distance: distance + 1,
            });
          }
        }
      }
      
      if ((cell as any).type === "Stairs") {
        const stairs = cell as {
          type: "Stairs";
          up: number | null;
          down: number | null;
        };
        if (stairs.up !== null) {
          const key = `${stairs.up},${row},${col}`;
          if (!visited.has(key)) {
            visited.add(key);
            queue.push({
              pos: { floor: stairs.up, row, col },
              distance: distance + 1,
            });
          }
        }
        if (stairs.down !== null) {
          const key = `${stairs.down},${row},${col}`;
          if (!visited.has(key)) {
            visited.add(key);
            queue.push({
              pos: { floor: stairs.down, row, col },
              distance: distance + 1,
            });
          }
        }
      }
    }

    console.log(`No available ${type} spot found near entrance/exit.`);
    return null;
  }
}
