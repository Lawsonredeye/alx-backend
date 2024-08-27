import { createClient } from 'redis';

async function nodeRedis() {
  try {
    const client = createClient();
    await client.connected;
    console.log('Redis client connected to the server');    
  } catch (error) {
    console.log('Redis client not connected to the server:', error);
  }
}

nodeRedis()