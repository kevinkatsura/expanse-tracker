import { Router } from "express";
import {
  createExpense,
  getExpenses,
  getSummary,
  deleteExpense,
} from "../controllers/expenseController.js";

const router = Router();

router.post("/", createExpense);
router.get("/", getExpenses);
router.get("/summary", getSummary);
router.delete("/:id", deleteExpense);

export default router;
