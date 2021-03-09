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

        // break apart URL
        const tweet_id = this.state.tweetURL.match(/status\/(\d+)$/); // regex is one or more digits at the end of the URL followed by status/

        if( tweet_id != null)
        {
            axios.get('http://localhost:5001/tweet_id/' + tweet_id[1])
            .then(res => {
                console.log(res.data)
                
                // redirect somewhere with results
            })
            .catch(err => this.setState({ tweetURL: 'Failed to Find Tweet' }));
        }
        else
        {
            this.setState({
                tweetURL: 'Invalid URL'
            })
        }

    }

    render() {
        return (
            <div>
                <br></br>
                <form onSubmit={this.onSubmit}>
                    <input type ="text"
                    placeholder="https://twitter.com/username/status/12345"
                    required
                    value={this.state.tweetURL}
                    onChange={this.onChangeTweetURL}
                    />
                </form>
            </div>
        )
    }
}