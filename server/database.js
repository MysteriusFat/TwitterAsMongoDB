const twitter = require('twitter');

const DATA_BASE_SCREEAN_NAME = 'JoseRam04272499';
const DATA_BASE_USER_ID = '1249434535269294080';

const cliente = new twitter({
  consumer_key : '',
  consumer_secret : '',
  access_token_key : '',
  access_token_secret : ''
});

cliente.get('statuses/user_timeline', {user_id: DATA_BASE_USER_ID}, function (err, data, res){
  var tweet = data[0];

  var tweet_id = tweet.id_str;
  var from = tweet.user.screen_name;

  var new_tweet = {
    status: 'reply ',
    in_reply_to_status_id: tweet_id
  }
  cliente.post('statuses/update', new_tweet , function(err, data, res ){
    console.log(data)
  });
});

/*
var param = {
  status: 'reply',
  in_reply_to_status_id: 1249508579905875968,
  username: '@JoseRam04272499'
}

*/
