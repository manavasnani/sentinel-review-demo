const express = require('express');
const { exec } = require('child_process');

const app = express();

app.get('/ping', (req, res) => {
    const host = req.query.host || '127.0.0.1';
    exec(`ping -c 1 ${host}`, (err, stdout) => {
        if (err) return res.status(500).send('failed');
        res.send(stdout);
    });
});

app.listen(3000);