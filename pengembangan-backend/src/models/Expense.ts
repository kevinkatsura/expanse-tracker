import mongoose, { Schema, Document } from "mongoose";

export interface IExpense extends Document {
  category: string;
  amount: number;
  date: Date;
  note?: string;
}

const ExpenseSchema: Schema = new Schema<IExpense>(
  {
    category: { type: String, required: true, trim: true },
    amount: { type: Number, required: true, min: 0 },
    date: { type: Date, required: true },
    note: { type: String, trim: true, maxlength: 200 },
  },
  { timestamps: true }
);

export default mongoose.model<IExpense>("Expense", ExpenseSchema);
