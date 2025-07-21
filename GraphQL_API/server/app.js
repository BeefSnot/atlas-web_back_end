const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const schema = require('./schema/schema');
const mongoose = require('mongoose');

const app = express();

mongoose.connect('mongodb+srv://jameshamby:BAUO958AUZAvXslx@cluster0.eqictx2.mongodb.net/graphql-db?retryWrites=true&w=majority');

mongoose.connection.once('open', () => {
  console.log('connected to database');
});

mongoose.connection.on('error', (err) => {
  console.log('Database connection error:', err);
});

app.use('/graphql', graphqlHTTP({
  schema,
  graphiql: true
}));

app.listen(4000, () => {
  console.log('now listening for request on port 4000');
});