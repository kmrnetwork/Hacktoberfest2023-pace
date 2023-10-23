import express from "express";
import mongoose from "mongoose";
import dotenv from "dotenv";
import cors from "cors";
import todoRoute from "./routes/todoRoute.js";

const app=express()
const PORT=process.env.port || 3000

app.use(express.json());
app.use(cors());



mongoose.connect(process.env.MONGODB_URL).then(()=>console.log(`connected to MongoDB`)).catch((err)=>console.log(err))

app.use(todoRoute);

app.listen(PORT,()=>console.log(`listening on port ${PORT}`))



