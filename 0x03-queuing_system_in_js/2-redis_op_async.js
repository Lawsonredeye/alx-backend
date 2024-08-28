// import { createClient, print } from 'redis';
// // const util = require('util')

// const client = createClient();

// try {
//   client.connect()
//   console.log('Redis client connected to the server');   
// } catch (error) {
//   console.log('Redis client not connected to the server:', error);
// }

// function setNewSchool(schoolName, value, callback) {
//   try {
//     client.set(schoolName, value, print);
//   } catch (error) {
//     console.log('I didnt connect')
//   }
// }

// async function displaySchoolValue(schoolName) {
//   client.get(schoolName, (err, reply) => {
//     if (err) {
//       console.error(err);
//     } else {
//       console.log(reply);
//     }
//   }).then((data) => console.log(data));
// }

// displaySchoolValue('Holberton');
// setNewSchool('HolbertonSanFrancisco', '100');
// displaySchoolValue('HolbertonSanFrancisco');

import { createClient } from 'redis';
const util = require('util')

const client = createClient();

client.connect().then(() => {
  console.log('Redis client connected to the server');
}).catch((err) => {
  console.log('Redis client not connected to the server:', err);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value);
}

async function displaySchoolValue(schoolName) {
  try {
    const getAsyc = util.promisify(client.get)
    const value = getAsyc(schoolName);
    console.log(value)
    // const value = await client.get(schoolName);
    // console.log(`Value for ${schoolName}: ${value}`);
  } catch (error) {
    console.error('Error fetching value:', error);
  }
}

async function main() {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();