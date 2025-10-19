import * as readline from "readline";
import {
  PaymentStatus,
  HourlyRate,
  SecondHourRate,
  RemainingHourRate,
} from "../Constants.js";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

abstract class ParkingRate {
  abstract calculateTotal(totalHours: number): number;
}

class HourlyParkingRate extends ParkingRate {
  hourlyRate: HourlyRate;

  constructor(hourlyRate: HourlyRate) {
    super();
    this.hourlyRate = hourlyRate;
  }

  calculateTotal(totalHours: number): number {
    return totalHours * this.hourlyRate;
  }
}

class IncrementalParkingCharge extends ParkingRate {
  firstHourCharge: HourlyRate;
  secondHourCharge: SecondHourRate;
  remainingHourCharge: RemainingHourRate;

  constructor(
    firstHourCharge: HourlyRate,
    secondHourCharge: SecondHourRate,
    remainingHourCharge: RemainingHourRate
  ) {
    super();
    this.firstHourCharge = firstHourCharge;
    this.secondHourCharge = secondHourCharge;
    this.remainingHourCharge = remainingHourCharge;
  }

  calculateTotal(totalHour: number): number {
    let total = 0;

    if (totalHour <= 1) {
      return this.firstHourCharge;
    }

    if (totalHour > 1) {
      total = this.firstHourCharge;
      totalHour = totalHour - 1;
    }

    if (totalHour > 2) {
      total += this.secondHourCharge;
      totalHour = totalHour - 2;
    }

    total = total + totalHour * this.remainingHourCharge;
    return total;
  }
}

let totalCollection = 0;

abstract class PaymentMode {
  abstract collectCash(totalAmount: number): boolean;
}

class CashMode extends PaymentMode {
  collectCash(totalAmount: number): boolean {
    totalCollection += totalAmount;
    return true;
  }
}

class CardMode extends PaymentMode {
  collectCash(totalAmount: number): boolean {
    rl.question("please enter 4 digit pin: ", (pin: string) => {
      console.log("varification successfull");
      rl.close();
    });
    totalCollection += totalAmount;
    return true;
  }
}

export class Payment {
  mode: PaymentMode;
  rate: ParkingRate;
  status: PaymentStatus;

  constructor(mode?: PaymentMode, rate?: ParkingRate) {
    this.mode = mode ?? new CashMode();
    this.rate = rate ?? new HourlyParkingRate(50);
    this.status = PaymentStatus.Pending;
  }
}
