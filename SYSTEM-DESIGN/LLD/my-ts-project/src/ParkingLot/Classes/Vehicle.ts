import { VehicleType, PaymentStatus } from "../Constants.js";
import { Payment } from "./Payment.js";

export class ParkingTicket {
  ticketNo: number;
  entryTime: Date;
  exitTime?: Date;
  amount?: number;
  status: PaymentStatus;
  payment?: Payment;
  
  constructor(ticketNo: number, entryTime: Date, status?: PaymentStatus) {
    this.ticketNo = ticketNo;
    this.entryTime = entryTime;
    this.status = status ? status : PaymentStatus.Pending;
  }

  update(exitTime?: Date, amount?: number, status?: PaymentStatus, payment?: Payment) {
    if (exitTime) {
      this.entryTime = exitTime;
    }

    if (amount) {
      this.amount = amount;
    }

    if (status) {
      this.status = status;
    }

    if (payment) {
      this.payment = payment;
    }
  }
}

export class Vehicle {
  licenseNo: string;
  type: VehicleType;

  constructor(licenseNo: string, type: VehicleType) {
    this.licenseNo = licenseNo;
    this.type = type;
  }
}


