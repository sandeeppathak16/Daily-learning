import { VehicleType } from "../Constants.js";
import { Payment } from "./Payment.js";

export class ParkingTicket {
  ticketNo: number;
  entryTime: Date;
  exitTime?: Date;
  amount?: number;
  status: string;
  payment?: Payment;
}

export class Vehicle {
  licenseNo: string;
  type: VehicleType;

  constructor(licenseNo: string, type: VehicleType) {
    this.licenseNo = licenseNo;
    this.type = type;
  }
}
