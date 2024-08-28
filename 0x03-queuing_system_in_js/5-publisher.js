/*
* Publishes to a redis channel
 */
import { createClient } from 'redis';
const redisPort = 6379;
const redisHost = 'localhost';
const client = createClient(redisPort, redisHost);

// Handle any connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const publishMessage = (message, time) => {
  console.log(`About to send ${message}`);
  setInterval(() => {
    client.publish('holberton school channel', message);
  }, time);
};
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
