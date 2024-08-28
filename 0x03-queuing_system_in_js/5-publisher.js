import { createClient, redis } from 'redis';

const client = createClient();

async function runRedis() {
  await client.on('connect', () => console.log(`Redis client connected to the server`))
  await client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));
  await client.connect(); 
}


// async function publishMessage(message, time) {
//   console.log(`About to send ${message}`);
//   setTimeout(async () => {
//     await client.publish('holberton school channel', message);
//   }, time);
// }

async function publishMessage(message, time) {
  console.log(`About to send ${message}`);
  setTimeout(async () => {
    await client.publish('holberton school channel', message);
  }, time);
}


runRedis()
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
