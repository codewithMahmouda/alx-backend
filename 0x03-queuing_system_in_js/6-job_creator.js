/*
* JOb creator
 */

import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '+2349072894396',
  message: 'Job Alert'
};
queue.on('error', (err) => {
  console.error('Kue Error:', err);
});

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

// Event handler for when the job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for when the job fails
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the Job to the queue
job.save((err) => {
  if (err) {
    console.error(`Error creating job: ${err}`);
  } else {
    console.log('Job saved to the queue');
  }
});
