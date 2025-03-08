import express from "express";
import cors from "cors";

const app = express();
const port = 5000;

app.use(express.json());
app.use(cors());

// Middleware for logging requests
app.use((req, res, next) => {
  console.log("Incoming Request:", {
    method: req.method,
    url: req.url,
    headers: req.headers,
    body: req.body,
  });
  next();
});

app.post("/webhook", (req, res) => {
  console.log("Request==>", req);
  console.log("Webhook request received!", res);
  res.sendStatus(200);
});

app.listen(port, () => console.log(`Webhook server running on port ${port}`));
