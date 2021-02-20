import React, { Component } from 'react';

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

        console.log(tweetURL);

        // send request to Twitter API

        // redirect somewhere with results
    }

    render() {
        return (
            <div>
                <br></br>
                <form onSubmit={this.onSubmit}>
                    <input type ="url"
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