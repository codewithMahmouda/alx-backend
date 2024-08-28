/*
* Subscribes to a redis channel
 */
import { createClient } from 'redis';
const redisPort = 6379;
const redisHost = 'localhost';
const client = createClient(redisPort, redisHost);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle any connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.SUBSCRIBE('holberton school channel');
client.on('message', (_err, message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  } else {
    console.log(message);
  }
});
