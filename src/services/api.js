const express = require('express');
const app = express();
const jwt = require('jsonwebtoken');
app.use(express.json());

const mockInventory = [
  { id: 1, name: 'Item A', price: '$10' },
  { id: 2, name: 'Item B', price: '$20' }
];

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  if (username === 'user' && password === 'password') {
    const token = jwt.sign({ username }, 'secret_key');
    res.json({ token });
  } else {
    res.status(401).json({ message: 'Invalid credentials' });
  }
});

app.post('/api/chat', (req, res) => {
  const { message } = req.body;
  const reply = `You asked about: ${message}. Here's a suggestion: ${mockInventory[0].name}`;
  res.json({ reply });
});

app.listen(5000, () => {
  console.log('Server running on port 5000');
});
