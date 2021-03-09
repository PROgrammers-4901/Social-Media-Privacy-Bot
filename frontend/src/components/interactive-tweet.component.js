import axios from 'axios';
import React, { Component } from 'react';

export default class ContactForm extends Component {
    constructor(props) {
        super(props);

        this.onSpam = this.onSpam.bind(this);
        this.onHam = this.onHam.bind(this);
        this.onNext = this.onNext.bind(this);

        this.state = {
            tweet  : '',
            label  : false,
            answer : false
        }
    }

    
    componentDidMount() {
        this.refreshTweet();
    }

    onNext(e) {
        e.preventDefault();

        this.refreshTweet();
    }

    onSpam(e) {
        e.preventDefault();

        this.testFor(true);
    }

    onHam(e) {
        e.preventDefault();

        this.testFor(false);
    }

    refreshTweet() {
        axios.get('http://localhost:5000/tweets/rand')
            .then(res => {
                this.setState({
                    tweet : res.data.contents,
                    label : res.data.label
                });
            })
            .catch(err => console.log("Cannot reach Database API: " + err));
    }

    testFor(bool) {
        if(this.state.label == bool)
        {
                this.setState({
                tweet: 'GOOD JOB!'
            });
            const timer = setTimeout(() => {this.refreshTweet()}, 2000);

            return () => clearTimeout(timer);
        }
        else
        {
                this.setState({
                tweet: 'WRONG!'
            });

            const timer = setTimeout(() => {this.refreshTweet()}, 5000);

            return () => clearTimeout(timer);
        }
    }

    render() {
        return (
            <div>
                <div>
                    <textarea placeholder="Example Tweet" 
                    rows="4" 
                    cols="50" 
                    id="Interactive-Tweets" 
                    name="interactiveTweets" 
                    readOnly
                    value={this.state.tweet}></textarea>
                </div>
                <div>
                    <button onClick={this.onSpam}> SPAM </button>
                    <button onClick={this.onHam}> HAM </button>
                    <button onClick={this.onNext}> NEXT </button>
                </div>
            </div>
        )
    }
}