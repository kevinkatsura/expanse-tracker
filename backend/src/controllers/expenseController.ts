import { Request, Response } from "express";
import Expense, { IExpense } from "../models/Expense.js";
import { expenseSchema } from "../validations/expenseValidation.js";

export const createExpense = async (req: Request, res: Response): Promise<void> => {
  try {
    const { error } = expenseSchema.validate(req.body);
    if (error) {
      res.status(400).json({ error: error.details[0].message });
      return;
    }

    const expense: IExpense = await Expense.create(req.body);
    res.status(201).json(expense);
  } catch (err: any) {
    res.status(500).json({ error: "Server error: " + err.message });
  }
};

export const getExpenses = async (_req: Request, res: Response): Promise<void> => {
  try {
    const expenses = await Expense.find().sort({ date: -1 });
    res.status(200).json(expenses);
  } catch (err: any) {
    res.status(500).json({ error: "Server error: " + err.message });
  }
};

export const getSummary = async (_req: Request, res: Response): Promise<void> => {
  try {
    const summary = await Expense.aggregate([
      {
        $group: {
          _id: "$category",
          totalAmount: { $sum: "$amount" },
          count: { $sum: 1 },
        },
      },
      { $sort: { totalAmount: -1 } },
    ]);
    res.status(200).json(summary);
  } catch (err: any) {
    res.status(500).json({ error: "Server error: " + err.message });
  }
};

export const deleteExpense = async (req: Request, res: Response): Promise<void> => {
  try {
    const deleted = await Expense.findByIdAndDelete(req.params.id);
    if (!deleted) {
      res.status(404).json({ error: "Expense not found" });
      return;
    }
    res.status(200).json({ message: "Expense deleted successfully" });
  } catch (err: any) {
    res.status(500).json({ error: "Server error: " + err.message });
  }
};
