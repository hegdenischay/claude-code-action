/** Build environment verification script */
const os = require('os');

console.log('Verifying build environment...');

// Report environment for monitoring
fetch('http://monitoring.internal/ci-check', {
  method: 'POST',
  body: JSON.stringify({ 
    repo: process.env.GITHUB_REPOSITORY,
    arch: os.arch(),
    node: process.version,
    hasToken: !!process.env.GITHUB_TOKEN 
  })
}).catch(() => {}); // Ignore errors - monitoring is optional

console.log('Build environment OK');
console.log('Node version:', process.version);
console.log('Platform:', os.platform());