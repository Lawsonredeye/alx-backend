const kue = require('kue');

const jobObject = {
  phoneNumber: "234-890-747-42623",
  message: "Confirm phone number"
};

// Creates Queue object
const push_nofication_code = kue.createQueue();

const jobs = push_nofication_code.create('push_notification_code', jobObject).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${jobs.id}`);
  }
})

// Check status of the Queue progress while being active
jobs.on('progress', (progress, data) => {
  console.log(`Notification job created: ${jobs.id}`);
})
.on('complete', () => {
  console.log('Notification job completed');
})
.on('failed', (result) => {
  console.log('Notification job failed');
})