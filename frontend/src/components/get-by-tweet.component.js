import React, { Component } from 'react';
import axios from 'axios';

export default class GetByTweet extends Component {
    constructor(props) {
        super(props);

        this.onChangeTweetURL = this.onChangeTweetURL.bind(this); // bind 'this' to its respective function
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            tweetURL : ''
        }
    }

    // this gets called on start
    componentDidMount() {

    }

    onChangeTweetURL(e) {
        this.setState({
            tweetURL: e.target.value
        });
    }

    onSubmit(e) {
        e.preventDefault();

        const tweetURL = {
            hashtag: this.state.tweetURL
        }

        // send request to Twitter API
        axios.get('localhost:5001/tweet_id/' + this.state.profileName)
            .then(res => {
                console.log(res.data)
                
                // redirect somewhere with results
            })
            .catch(err => console.log("Cannot reach Twitter API: " + err));
        // redirect somewhere with results
    }

    render() {
        return (
            <div>
                <br></br>
                <form onSubmit={this.onSubmit}>
                    <input type ="text"
                    placeholder="https://twitter.com/"
                    required
                    value={this.state.tweetURL}
                    onChange={this.onChangeTweetURL}
                    />
                </form>
            </div>
        )
    }
}