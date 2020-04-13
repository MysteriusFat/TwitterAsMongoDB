const express = require('express');
const cors = require('cors');

const app = express()

app.use(express.json());
app.use(cors());

app.get('/', function (req, res) {
  res.json({
    'message' : 'Meow',
  });
})

function isValidMew(mew){
  return mew.name && mew.name.toString().trim() != '' &&
    mew.content && mew.content.toString().trim() != '';
}

app.post('/mews', (req, res) => {
  if (isValidMew(req.body)){
    const mew = {
      name: req.body.name.toString(),
      content : req.body.content.toString()
    };
    console.log(mew);
  }else{
    res.status();
    res.json({
      message: "Hey! Name and content are required!"
    });
  }
});

app.listen(5000, function(){
  console.log('[*] Listen on port: 5000' );
});
