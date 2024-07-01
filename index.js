const { exec } = require('child_process');
const path = require('path');

// Adjust the path to your main Python script
const scriptPath = path.join(__dirname, 'app.py');

exec(`python ${scriptPath}`, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
});
