import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the client.get method to use with async/await
const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to get a value using async/await
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (err) {
    console.error(`Error fetching value for ${schoolName}:`, err);
  }
}

// Call the functions as required
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
