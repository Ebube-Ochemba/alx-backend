import kue from 'kue';

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);  // Track initial progress

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Continue processing
  job.progress(50, 100);  // Update progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();  // Complete the job
};

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs from the queue 'push_notification_code_2', with 2 jobs processed simultaneously
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
