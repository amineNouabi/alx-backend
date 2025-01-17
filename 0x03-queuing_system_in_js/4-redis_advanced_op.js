#!/usr/bin/node

import { createClient, print } from "redis";

const client = createClient();

client.on("error", err => console.log(`Redis client not connected to the server: ${err.message}`));
client.on("connect", () => console.log("Redis client connected to the server"));

client.hset("ALX", "Portland", "50", print);
client.hset("ALX", "Seattle", "80", print);
client.hset("ALX", "New York", "20", print);
client.hset("ALX", "Bogota", "20", print);
client.hset("ALX", "Cali", "40", print);
client.hset("ALX", "Paris", "2", print);

client.hgetall("ALX", (err, hashSet) => {
  if (err) throw err;
  console.log(hashSet);
});
