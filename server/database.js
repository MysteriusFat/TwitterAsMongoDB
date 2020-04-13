const twitter = require('twitter');

const DATA_BASE_SCREEAN_NAME = 'JoseRam04272499';
const DATA_BASE_USER_ID = '1249434535269294080';

const cliente = new twitter({
  consumer_key : 'r4q9ZTdev9x5rEvve82NGDo1g',
  consumer_secret : '9EXv8SrRjgShdysinMwTweNAPry7dIPWspPgxHhRJ541CeF8sR',
  access_token_key : '1249434535269294080-dTvrnBoyLSuJ1glINHMAzXNO0AbpHp',
  access_token_secret : 'IUMOCcgDpoF8VISreuxbgBZP70njXAJkuwx6jOWZoDV4I'
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
