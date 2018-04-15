const request = require('request');
const dotenv = require('dotenv');

dotenv.config();

exports.postLog = (event, callback) => {
  const file = event.data;
  const context = event.context;
  console.log(file.name)
  request.post({
    url: process.env.ELBA_API_ENDPOINT,
    form: { data: file.name },
  },
  (err, httpReponse, body) => {
    if (err) {
      console.log(httpReponse, body);
    } else {
      console.log(err, body);
    }
    callback();
  });
};
