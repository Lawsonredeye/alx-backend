import { createClient, redis } from 'redis';

const client = createClient();
async function runRedis() {
  client.on('connect', () => console.log(`Redis client connected to the server`))
  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  await client.connect();
  await client.subscribe('holberton school channel', (message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe('holberton school channel')
      client.quit();
    }
  });
}

runRedis()

// await client.on('message', (channel = 'holberton school channel', message) => {
//   console.log(message);
//   if (message === 'KILL_SERVER') {
//     console.log('Received KILL_SERVER message, quitting...');
//     client.unsubscribe(channel);
//     client.quit()
//   }
// });