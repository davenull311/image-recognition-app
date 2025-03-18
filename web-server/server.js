// Import required modules
const express = require('express');
const multer = require('multer');
const axios = require('axios');
const path = require('path');
const fs = require('fs');
const FormData = require('form-data');

// Initialize Express app
const app = express();

// Configure multer for file uploads, storing files temporarily
const upload = multer({ dest: 'uploads/' });

// Serve static files (HTML, CSS, JS) from 'views' directory
app.use(express.static(path.join(__dirname, 'views')));

// Root route: serve main HTML file
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// Endpoint for handling image uploads and sending them to ML API
app.post('/classify', upload.single('image'), async (req, res) => {
    try {
        const image = req.file;

        // Prepare FormData to send image to ML backend
        const formData = new FormData();
        formData.append('image', fs.createReadStream(image.path));

        // Make HTTP POST request to ML API
        const response = await axios.post('http://ml-api:8000/predict', formData, {
            headers: formData.getHeaders()
        });

        // Return classification results to client
        res.json(response.data);
    } catch (error) {
        // Handle errors
        res.status(500).json({ error: error.message });
    }
});

// Start Node.js server on port 3000
app.listen(3000, () => {
    console.log('Node.js Server running on port 3000');
});
