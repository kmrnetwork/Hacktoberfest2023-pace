import mongoose from "mongoose";


export async function connectDB(){
    try{
        await mongoose.connect(process.env.MONGODB_URL);
        console.log("connected to MongoDB");
    }
    catch(err){
        console.log(err);
    }
}