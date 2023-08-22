const express = require("express");
const mongoose = require("mongoose");
const User = require("./models/User");
const cookieParser = require("cookie-parser");

(async () => {
  try {
    const app = express();
    app.use(express.json());
    app.use(express.urlencoded({ extended: true }));
    app.set("view engine", "ejs");
    app.use(cookieParser());

    await mongoose.connect("mongodb://db:27017/ctf");
    console.log("connected");

    let exist = await User.findOne({ username: "admin" });
    if (!exist) {
      const admin = new User({
        username: "admin",
        password:
          "0dfd72fc3836be6f3aa06748e4cf626c9157d9410f8289226438cbde1477a5d4243abbf48a3a5c6f",
        flag: "ingeniums{1t_w4s_4_n0sql1_4ft3r_4ll}",
      });
      admin.save();
    }

    app.listen(3000, () => {
      console.log("listening on 3000");
    });

    app.get("/", (req, res) => {
      res.render("login", { error: null });
    });

    app.post("/login", async (req, res) => {
      const q = {
        username: req.body.username,
        password: req.body.password,
      };

      const user = await User.findOne(q);
      if (!user) {
        return res.json({ error: "user not found :(" });
      }
      try {
        res.cookie("flag", user.flag, { httpOnly: true });
        return res.json({ success: true, flag: user.flag });
      } catch (error) {
        console.log(error);
      }
    });

    app.get("/home", (req, res) => {
      if (!req.cookies.flag) {
        return res.redirect("/");
      }
      return res.render("home", { flag: req.cookies.flag });
    });
  } catch (error) {
    console.log(error);
  }
})();
