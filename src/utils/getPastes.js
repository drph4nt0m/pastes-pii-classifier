const mongoose = require('mongoose');
const fs = require('fs');
const config = require('../config');
const logger = require('./logger');

// MongoDB

try {
  mongoose.connect(config.mongodb.uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true
  });
  logger.info('MongoDB connected', { type: 'database' });
} catch (error) {
  logger.error('MongoDB Connection Error', { type: 'database' });
}

const PasteSchema = new mongoose.Schema(
  {
    id: { type: String, required: true, unique: true },
    site_id: { type: String, required: true },
    paste: {
      id: { type: String, required: true },
      url: { type: String, required: true },
      title: { type: String, required: true },
      author: { type: String, required: true },
      createdOn: { type: Date, required: true },
      body: { type: String, required: true },
      md5: { type: String, required: true }
    }
  },
  { timestamps: true }
);

const pasteModel = mongoose.model('paste', PasteSchema);

module.exports = async () => {
  try {
    logger.info(`Getting pastes...`, { type: 'database' });
    const pastes = await pasteModel.find({});
    logger.info(`Got pastes`, { type: 'database' });
    logger.info('Saving pastes to pastes.json', { type: 'database' });
    const pastesJson = JSON.stringify(pastes, null, 2);
    fs.writeFileSync('./pastes.json', pastesJson);
    logger.info('Saved pastes to pastes.json', { type: 'database' });
    return pastes;
  } catch (error) {
    logger.error(error, { type: 'database' });
    return [];
  }
};
