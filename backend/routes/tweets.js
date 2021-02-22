const router = require('express').Router();
let Tweet = require('../models/tweet.model.js');

// GET ALL
router.route('/').get((req, res) => {
    Tweet.find()
    .then(tweets => res.json(tweets))
    .catch(err => res.status(400).json('Error: ' + err));
});

// POST A TWEET
router.route('/add').post((req, res) => { 
    const contents = req.body.contents;
    const label = req.body.label;

    const newTweet = new Tweet({
        contents,
        label
    });

    newTweet.save()
    .then(() => res.json('New Tweet Added!'))
    .catch(err => res.status(400).json('Error: ' + err));
});

// GET BY ID
router.route('/:id').get((req, res) => { 
    Tweet.findById(req.params.id)
    .then(tweet => res.json(tweet))
    .catch(err => res.status(400).json('Error: ' + err));
});

// DELETE BY ID
router.route('/:id').delete((req, res) => { 
    Tweet.findByIdAndDelete(req.params.id)
    .then(() => res.json('Tweet Deleted'))
    .catch(err => res.status(400).json('Error: ' + err));
});

// UDPATE BY ID
router.route('/update/:id').post((req, res) => { 
    Tweet.findById(req.params.id)
    .then(tweet => {
        tweet.contents = req.body.contents;
        tweet.label = req.body.label;

        newTweet.save()
        .then(() => res.json('New Tweet Added!'))
        .catch(err => res.status(400).json('Error: ' + err));
    })
    .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;