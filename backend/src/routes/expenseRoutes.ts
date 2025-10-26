import { Router } from "express";
import {
  createExpense,
  getExpenses,
  getSummary,
  deleteExpense,
} from "../controllers/expenseController.js";

const router = Router();

/**
 * @swagger
 * tags:
 *   name: Expenses
 *   description: ExpensesAPI endpoints untuk ngatur keuangan kamu
 */

/**
 * @swagger
 * /api/expenses:
 *   post:
 *     summary: Menambah data pengeluaran baru
 *     tags: [Expenses]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - category
 *               - amount
 *               - date
 *             properties:
 *               category:
 *                 type: string
 *                 example: Makanan
 *               amount:
 *                 type: number
 *                 example: 15000
 *               date:
 *                 type: string
 *                 format: date
 *                 example: 2025-10-26
 *               note:
 *                 type: string
 *                 example: Makan bareng bestie di Gion
 *     responses:
 *       201:
 *         description: Expense created successfully
 *       400:
 *         description: Validation error
 */
router.post("/", createExpense);

/**
 * @swagger
 * /api/expenses:
 *   get:
 *     summary: Mendapatkan seluruh data pengeluaran
 *     tags: [Expenses]
 *     responses:
 *       200:
 *         description: Daftar seluruh pengeluaran
 */
router.get("/", getExpenses);

/**
 * @swagger
 * /api/expenses/summary:
 *   get:
 *     summary: Mendapatkan total pengeluaran per kategori
 *     tags: [Expenses]
 *     responses:
 *       200:
 *         description: Ringkasan total pengeluaran per kategori
 */
router.get("/summary", getSummary);

/**
 * @swagger
 * /api/expenses/{id}:
 *   delete:
 *     summary: Menghapus data pengeluaran berdasarkan ID
 *     tags: [Expenses]
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: string
 *         description: Expense ID
 *     responses:
 *       200:
 *         description: Expense deleted successfully
 *       404:
 *         description: Expense not found
 */
router.delete("/:id", deleteExpense);

export default router;
