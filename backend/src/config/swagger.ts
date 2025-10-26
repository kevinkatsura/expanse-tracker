import swaggerJSDoc from "swagger-jsdoc";
import path from "path";
import { fileURLToPath } from "url";

// ✅ Define __dirname in ESM scope
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = process.env.PORT || 5000;

const options: swaggerJSDoc.Options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "Expense Tracker API",
      version: "1.0.0",
      description:
        "API documentation for the Expense Tracker backend service built with Express, TypeScript, and MongoDB.",
    },
    servers: [
      {
        url: process.env.SERVER_URL || `http://localhost:${PORT}`,
        description: "API Server",
      },
    ],
  },
  // ✅ Works for both dev (.ts) and prod (.js)
  apis: [path.resolve(__dirname, "../routes/*.{ts,js}")],
};

const swaggerSpec = swaggerJSDoc(options);

export default swaggerSpec;
