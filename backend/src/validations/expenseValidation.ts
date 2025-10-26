import Joi from "joi";

export const expenseSchema = Joi.object({
  category: Joi.string().required(),
  amount: Joi.number().positive().required(),
  date: Joi.date().required(),
  note: Joi.string().max(200).allow("", null),
});
