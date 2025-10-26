import mongoose from "mongoose";

const connectDB = async (): Promise<void> => {
  try {
    await mongoose.connect(process.env.MONGO_URI as string);
    console.log("MongoDB connected successfully");
  } catch (error: any) {
    console.error("MongoDB connection failed: ", error.message);
    process.exit(1);
  }
};

// console.log(process.env)
// await connectDB();

export default connectDB;
