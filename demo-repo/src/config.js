// Configuration file
const config = {
  apiUrl: 'https://api.example.com',
  apiKey: 'HS_DEMO_KEY_ABC1234567890XYZ',  // ISSUE: Exposed secret
  databaseUrl: 'postgresql://user:password@localhost/db',  // ISSUE: Hardcoded credentials
  slackWebhook: 'https://hooks.slack.com/services/T12345678/B12345678/abcdefghijklmnopqrstuvwx'
};

module.exports = config;
